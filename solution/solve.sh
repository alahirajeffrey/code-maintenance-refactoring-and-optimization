#!/usr/bin/env bash
set -e

cd "$(dirname "$0")/.."

source .venv/bin/activate

export PYTHONPATH=$(pwd)

uv run python -m app.main &
SERVER_PID=$!

sleep 5

STATUS=$(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:5000/health)
if [ "$STATUS" -ne 200 ]; then
  echo "❌ /health returned $STATUS"
  kill $SERVER_PID
  exit 1
fi

echo "✅ /health returned 200"

# Stop the server
kill $SERVER_PID
