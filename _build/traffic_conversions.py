#!/usr/bin/env python3
"""Traffic with conversions for the 11870 test blog.

Visits each article like wp-traffic-generator.py (same devices and referrers),
scrolls to the end, and in a share of visits fills the sidebar newsletter box and
clicks its button, which runs compass.trackConversion("CTA Newsletter").

Every visit runs in a fresh browser context, so each one is a new user.

Usage:
    python3 _build/traffic_conversions.py --rounds 3 --concurrency 3
    python3 _build/traffic_conversions.py --conversion-rate 0.3
"""

import argparse
import asyncio
import os
import random
import sys

from playwright.async_api import async_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (label, user-agent, viewport), same set as wp-traffic-generator.py
DEVICES = [
    ("iPhone",
     "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 "
     "(KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
     {"width": 390, "height": 844}),
    ("Samsung",
     "Mozilla/5.0 (Linux; Android 14; SM-S918B) AppleWebKit/537.36 "
     "(KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
     {"width": 412, "height": 915}),
    ("iPad",
     "Mozilla/5.0 (iPad; CPU OS 17_5 like Mac OS X) AppleWebKit/605.1.15 "
     "(KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
     {"width": 820, "height": 1180}),
    ("Desktop Chrome",
     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
     "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
     {"width": 1440, "height": 900}),
    ("Desktop Firefox",
     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
     {"width": 1440, "height": 900}),
]

REFERRERS = [
    "https://www.google.com/",
    "https://t.co/",
    "https://www.facebook.com/",
    "https://www.instagram.com/",
    "https://www.reddit.com/",
    "",  # direct
]

NAMES = ["lucia", "pablo", "marta", "javi", "nuria", "sergio", "elena", "dani", "laura", "oscar"]


def read_urls(path):
    with open(path) as f:
        urls = [u.strip() for u in f if u.strip() and not u.startswith("#")]
    # conversions live on article pages only, skip the home
    return [u for u in urls if u.rstrip("/").count("/") > 3]


async def scroll_to_bottom(page):
    for _ in range(8):
        await page.mouse.wheel(0, 700)
        await page.wait_for_timeout(350)


async def visit(browser, sem, rnd, url, device, referrer, action, dwell_ms, log_hits):
    label, ua, viewport = device
    slug = url.rstrip("/").split("/")[-1][:30]
    ref = referrer or "direct"
    async with sem:
        ctx = await browser.new_context(
            user_agent=ua,
            viewport=viewport,
            extra_http_headers=({"Referer": referrer} if referrer else {}),
        )
        hits = []
        try:
            page = await ctx.new_page()
            if log_hits:
                page.on("request", lambda r: hits.append(r.url) if "newsroom.bi" in r.url else None)
            await page.goto(url, wait_until="domcontentloaded", timeout=30000)
            await page.wait_for_timeout(dwell_ms)
            await scroll_to_bottom(page)
            if action == "convert":
                email = f"{random.choice(NAMES)}.test{random.randint(1000, 9999)}@example.com"
                await page.fill(".nl-box input[type=email]", email)
                await page.click(".nl-box .nl-cta")
            # leave time for the SDK to send the conversion
            await page.wait_for_timeout(3000 if action != "view" else 500)
            print(f"OK  r{rnd} {label:15} ref={ref:28} {action:10} {slug}")
            for h in hits:
                print("      hit", h[:160])
            return action
        except Exception as e:  # noqa: BLE001
            print(f"ERR r{rnd} {label:15} {slug}: {e}", file=sys.stderr)
            return None
        finally:
            await ctx.close()


async def run(args):
    urls = read_urls(args.urls_file)
    rng = random.Random(args.seed)
    sem = asyncio.Semaphore(args.concurrency)
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        try:
            tasks = []
            plan = []
            if args.visits:
                # random mode: N visits, random article, device, referrer and dwell
                for _ in range(args.visits):
                    plan.append((1, rng.choice(urls), rng.choice(DEVICES), rng.choice(REFERRERS)))
            else:
                for rnd in range(args.rounds):
                    for i, url in enumerate(urls):
                        plan.append((rnd + 1, url, DEVICES[(rnd + i) % len(DEVICES)],
                                     REFERRERS[(rnd + i) % len(REFERRERS)]))
            for rnd, url, device, referrer in plan:
                action = "convert" if rng.random() < args.conversion_rate else "view"
                dwell = rng.randint(args.dwell_ms, args.dwell_ms * 4) if args.visits else args.dwell_ms
                tasks.append(visit(browser, sem, rnd, url, device, referrer,
                                   action, dwell, args.log_hits))
            results = await asyncio.gather(*tasks)
        finally:
            await browser.close()
    return results


def main():
    ap = argparse.ArgumentParser(description="Traffic with conversions for the 11870 test blog.")
    ap.add_argument("--urls-file", default=os.path.join(ROOT, "urls.txt"))
    ap.add_argument("--rounds", type=int, default=3)
    ap.add_argument("--visits", type=int, default=0,
                    help="Random mode: this many visits to random articles, devices and "
                         "referrers (overrides --rounds).")
    ap.add_argument("--concurrency", type=int, default=3)
    ap.add_argument("--dwell-ms", type=int, default=2500)
    ap.add_argument("--conversion-rate", type=float, default=0.3,
                    help="Share of visits that click the CTA Newsletter button.")
    ap.add_argument("--seed", type=int, default=None)
    ap.add_argument("--log-hits", action="store_true",
                    help="Print the Marfeel requests each visit sends.")
    args = ap.parse_args()

    results = asyncio.run(run(args))
    ok = [r for r in results if r]
    print(f"\nTRAFFIC RESULT: {len(ok)}/{len(results)} visits successful, "
          f"{ok.count('convert')} CTA Newsletter conversions")
    sys.exit(0 if len(ok) == len(results) else 1)


if __name__ == "__main__":
    main()
