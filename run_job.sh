#!/bin/bash
set -uo pipefail
cd "$(dirname "$0")"

. venv/bin/activate
. .env

logf="cache/`date '+%Y-%m-%d'`.log"

echo "======================== scenarios run at $(date '+%Y-%m-%d %H:%M:%S') ===========================" >> $logf
python main.py --token ${REFRESH_TOKEN} --kvauth ${KV_AUTH} --kvurl ${KV_URL} -k --venus --pushmongo --mongouri ${MONGO_URI} 2>&1 | tee -a $logf

echo "=== run git push ===" >> $logf
./git_push.sh ${GIT_KEY_LOCATION} 2>&1 | tee -a $logf

rm -f "cache/need_update.txt"
rm -rf "cache/update_master"
