#!/usr/bin/env python3
"""Print every video URL in a public or unlisted YouTube playlist, one per line.

Usage: youtube_playlist.py <playlist-id-or-url>
"""
import json, os, re, sys, urllib.parse, urllib.request


def main():
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    arg = sys.argv[1]
    m = re.search(r"list=([A-Za-z0-9_-]+)", arg)
    pid, token = (m.group(1) if m else arg), ""
    while True:
        params = {"part": "contentDetails", "playlistId": pid, "maxResults": 50, "pageToken": token}
        if os.environ.get("YOUTUBE_API_KEY"):
            params["key"] = os.environ["YOUTUBE_API_KEY"]
        url = "https://www.googleapis.com/youtube/v3/playlistItems?" + urllib.parse.urlencode(params)
        with urllib.request.urlopen(url, timeout=30) as r:
            d = json.load(r)
        for it in d["items"]:
            print("https://www.youtube.com/watch?v=" + it["contentDetails"]["videoId"])
        token = d.get("nextPageToken")
        if not token:
            break


if __name__ == "__main__":
    main()
