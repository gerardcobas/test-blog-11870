#!/bin/sh
# Installs the hourly traffic launchd agent for the current user.
# Weekdays, every hour from 06:00 to 19:00 (hourly.py adds a random 0-40 min delay).
set -e
LABEL=com.test-blog-11870.traffic
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
PLIST="$HOME/Library/LaunchAgents/$LABEL.plist"
LOG="$HOME/Library/Logs/test-blog-11870/traffic.log"
mkdir -p "$(dirname "$LOG")"
/usr/bin/python3 - "$LABEL" "$REPO" "$LOG" "$PLIST" <<'PY'
import plistlib, sys
label, repo, log, out = sys.argv[1:]
plistlib.dump({
    "Label": label,
    "ProgramArguments": ["/usr/bin/python3", f"{repo}/_build/hourly.py"],
    "StartCalendarInterval": [{"Weekday": d, "Hour": h, "Minute": 0}
                              for d in range(1, 6) for h in range(6, 20)],
    "StandardOutPath": log,
    "StandardErrorPath": log,
    "ProcessType": "Background",
}, open(out, "wb"))
PY
launchctl bootout "gui/$(id -u)/$LABEL" 2>/dev/null || true
launchctl bootstrap "gui/$(id -u)" "$PLIST"
echo "installed $LABEL -> $PLIST"
