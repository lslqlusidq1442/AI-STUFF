#!/usr/bin/env python3
"""Given an Instagram/YouTube URL, print JSON with title, text sources and GitHub repos found.

Usage: find_repos.py <url> [--cookies-from-browser chrome]
YouTube uses the Data API (set YOUTUBE_API_KEY when running outside the cloud proxy).
Instagram and anything else go through yt-dlp.
"""
import json, os, re, subprocess, sys, urllib.parse, urllib.request

GH = re.compile(r"github\.com/([A-Za-z0-9-]+)/([A-Za-z0-9_.-]+)", re.I)
SKIP_OWNERS = {"sponsors", "orgs", "features", "topics", "settings", "marketplace", "about"}


def yt_id(url):
    m = re.search(r"(?:v=|youtu\.be/|shorts/|live/|embed/)([A-Za-z0-9_-]{11})", url)
    return m.group(1) if m else None


def yt_api(path, **params):
    if os.environ.get("YOUTUBE_API_KEY"):
        params["key"] = os.environ["YOUTUBE_API_KEY"]
    url = f"https://www.googleapis.com/youtube/v3/{path}?{urllib.parse.urlencode(params)}"
    with urllib.request.urlopen(url, timeout=30) as r:
        return json.load(r)


def from_youtube(vid):
    v = yt_api("videos", part="snippet", id=vid)["items"]
    if not v:
        raise SystemExit(f"video {vid} not found")
    sn = v[0]["snippet"]
    sources = {"description": sn.get("description", "")}
    try:
        threads = yt_api("commentThreads", part="snippet", videoId=vid, order="relevance", maxResults=50)
        sources["comments"] = "\n".join(
            t["snippet"]["topLevelComment"]["snippet"]["textOriginal"] for t in threads.get("items", []))
    except Exception as e:  # comments disabled
        sources["comments"] = f"(unavailable: {e})"
    return sn["title"], sn.get("channelTitle", ""), sources


def from_ytdlp(url, extra):
    out = subprocess.run(["yt-dlp", "--skip-download", "--dump-single-json", *extra, url],
                         capture_output=True, text=True)
    if out.returncode:
        raise SystemExit(f"yt-dlp failed: {out.stderr.strip().splitlines()[-1:]}")
    d = json.loads(out.stdout)
    return d.get("title", ""), d.get("uploader", ""), {"description": d.get("description") or ""}


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    url, extra = sys.argv[1], sys.argv[2:]
    vid = yt_id(url) if "youtu" in url else None
    title, author, sources = from_youtube(vid) if vid else from_ytdlp(url, extra)
    repos = []
    for text in sources.values():
        for owner, repo in GH.findall(text):
            repo = re.sub(r"(\.git|[.,)]+)$", "", repo)
            slug = f"{owner}/{repo}"
            if owner.lower() not in SKIP_OWNERS and slug not in repos:
                repos.append(slug)
    print(json.dumps({"url": url, "title": title, "author": author,
                      "repos": repos, "sources": sources}, indent=2))


if __name__ == "__main__":
    main()
