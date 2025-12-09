#!/usr/bin/env bash
# cron_schedule: Crontab examples and tips.
set -euo pipefail

cat <<'CRON'
# ┌──────── minute (0 - 59)
# │ ┌────── hour (0 - 23)
# │ │ ┌──── day of month (1 - 31)
# │ │ │ ┌── month (1 - 12)
# │ │ │ │ ┌─ day of week (0 - 6) (Sunday=0)
# │ │ │ │ │
# * * * * *  /path/to/script.sh            # every minute
0 * * * *    /usr/bin/backup.sh            # hourly at minute 0
30 2 * * 1   /usr/bin/cleanup.sh           # Mondays at 02:30
0 5 1 * *    /usr/bin/report.sh            # first of each month at 05:00
0 0 */2 * *  /usr/bin/every_two_days.sh    # every two days at midnight
# Redirect output for logging
15 3 * * *   /usr/bin/rotate_logs.sh >> /var/log/cron.log 2>&1
CRON
