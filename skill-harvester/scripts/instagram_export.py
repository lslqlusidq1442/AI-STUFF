#!/usr/bin/env python3
"""Print saved-post URLs from an Instagram "Download your information" export (JSON format).

Usage: instagram_export.py <export.zip or unzipped folder>
"""
import json, re, sys, zipfile
from pathlib import Path

URL = re.compile(r"https://www\.instagram\.com/(?:p|reel|reels|tv)/[A-Za-z0-9_-]+/?")


def saved_files(src):
    p = Path(src)
    if p.is_file() and p.suffix == ".zip":
        with zipfile.ZipFile(p) as z:
            for n in z.namelist():
                if "saved" in n and n.endswith(".json"):
                    yield z.read(n).decode("utf-8")
    else:
        for f in p.rglob("*saved*.json"):
            yield f.read_text("utf-8")


def main():
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    seen = set()
    for text in saved_files(sys.argv[1]):
        for u in URL.findall(json.dumps(json.loads(text))):
            if u not in seen:
                seen.add(u)
                print(u)


if __name__ == "__main__":
    main()
