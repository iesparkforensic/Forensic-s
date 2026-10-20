#!/bin/bash
# Mac: double-click to open every site in sites.txt, 10 seconds apart.
# Optional: run "./open_sites.command 5" in Terminal for a 5-second interval.
cd "$(dirname "$0")" || exit 1

INTERVAL="${1:-10}"

if [ ! -f sites.txt ]; then
  echo "sites.txt was not found next to this file."
  exit 1
fi

echo "Opening sites from sites.txt, ${INTERVAL} seconds apart. Press Ctrl+C to stop."
count=0
while IFS= read -r line || [ -n "$line" ]; do
  url="$(printf '%s' "$line" | tr -d '\r' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')"
  case "$url" in
    ''|'#'*) continue ;;
    *://*) ;;
    *) url="https://$url" ;;
  esac
  count=$((count + 1))
  [ "$count" -gt 1 ] && sleep "$INTERVAL"
  echo "[$count] $url"
  open "$url"
done < sites.txt

echo "Done."
