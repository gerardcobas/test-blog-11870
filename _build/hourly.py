#!/usr/bin/env python3
"""Hourly random traffic for the 11870 test blog, run by launchd on weekdays.

Each run:
  - skips weekends and anything outside 06:00-20:00 (launchd replays missed runs
    when the Mac wakes up, so a late wake must not generate night traffic)
  - waits a random 0-40 min so visits don't land on the hour
  - sends a random number of visits weighted by hour (morning and evening peaks)
  - uses a random conversion rate (CTA Newsletter) between 10% and 35%

Logs to ~/Library/Logs/test-blog-11870/traffic.log
"""

import datetime as dt
import os
import random
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
START_HOUR, END_HOUR = 6, 20

# relative audience per hour, like a news site: morning peak, lunch, evening
HOUR_WEIGHT = {6: 0.35, 7: 0.7, 8: 1.0, 9: 1.0, 10: 0.85, 11: 0.75, 12: 0.75,
               13: 0.9, 14: 0.85, 15: 0.65, 16: 0.65, 17: 0.7, 18: 0.8, 19: 0.6}


def log(msg):
    print(f"{dt.datetime.now():%Y-%m-%d %H:%M:%S} {msg}", flush=True)


def main():
    now = dt.datetime.now()
    if now.weekday() >= 5 or not (START_HOUR <= now.hour < END_HOUR):
        log(f"skip: outside weekday {START_HOUR}:00-{END_HOUR}:00")
        return 0

    # random delay, finishing well before END_HOUR
    end = now.replace(hour=END_HOUR, minute=0, second=0, microsecond=0)
    max_delay = max(0, min(40 * 60, int((end - now).total_seconds()) - 10 * 60))
    delay = random.randint(0, max_delay)
    visits = max(2, round(random.uniform(6, 24) * HOUR_WEIGHT.get(now.hour, 0.5)))
    rate = round(random.uniform(0.10, 0.35), 2)
    log(f"plan: wait {delay // 60} min, {visits} visits, conversion rate {rate}")
    time.sleep(delay)

    cmd = [sys.executable, os.path.join(HERE, "traffic_conversions.py"),
           "--visits", str(visits), "--conversion-rate", str(rate), "--concurrency", "3"]
    res = subprocess.run(cmd, capture_output=True, text=True)
    summary = [l for l in res.stdout.splitlines() if l.startswith("TRAFFIC RESULT")]
    log(summary[0] if summary else f"no summary, exit {res.returncode}")
    if res.returncode != 0:
        log(res.stderr.strip()[-2000:])
    return res.returncode


if __name__ == "__main__":
    sys.exit(main())
