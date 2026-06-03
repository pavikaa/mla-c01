#!/bin/sh
# Local server for markdown reader (learn.html needs HTTP)
cd "$(dirname "$0")"
PORT="${1:-8080}"
echo "MLA-C01 Study Hub → http://localhost:$PORT"
echo "Press Ctrl+C to stop"
python3 -m http.server "$PORT"
