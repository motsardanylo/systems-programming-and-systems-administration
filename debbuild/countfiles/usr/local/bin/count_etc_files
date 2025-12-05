#!/usr/bin/env bash

set -euo pipefail

TARGET="/etc"

if [ ! -d "$TARGET" ]; then
  echo "Каталог $TARGET не існує." >&2
  exit 2
fi

count=$(find "$TARGET" -maxdepth 1 -type f ! -lname '*' -printf '.' | wc -c)

printf "%s\n" "$count"
