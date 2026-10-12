#!/usr/bin/env python3
"""Collect YouTube search results for 'make money with Claude' queries.
Caches every API response on disk so it can resume after quota errors."""
import json, os, sys, hashlib, time, requests

DATA = "/home/user/AI-STUFF/research_notes/Making money with Claude/data"
CACHE = os.path.join(DATA, "raw_search_cache")
os.makedirs(CACHE, exist_ok=True)
BASE = "https://www.googleapis.com/youtube/v3/"

QUERIES = [
    "make money with Claude", "make money with Claude AI", "Claude Code make money",
    "Claude AI side hustle", "Claude AI passive income", "Claude automation agency",
    "sell Claude skills", "Claude skills make money", "Claude Code SaaS", "Claude MCP make money",
    "Claude Cowork business", "Claude Cowork make money", "Claude AI freelancing", "Claude AI Fiverr",
    "Claude AI Upwork", "Claude faceless YouTube", "Claude KDP book", "Claude AI ebook",
    "Claude AI $10k month", "Claude vs ChatGPT make money", "vibe coding make money",
    "AI agent business Claude", "Claude app build sell", "Claude Code business",
    "Claude Code side hustle", "Claude Code $10k", "Claude Code startup revenue",
    "Claude Code agency", "Claude AI business ideas", "Claude AI income",
    "Claude artifacts make money", "Claude projects business", "Anthropic Claude money",
    "Claude AI digital products", "Claude AI affiliate marketing", "Claude AI blogging SEO",
    "Claude AI newsletter", "Claude AI trading bot", "Claude AI crypto", "Claude AI chatbot business",
    "Claude AI voice agent business", "Claude AI cold email", "Claude AI lead generation",
    "Claude AI website local business", "Claude Code websites clients", "Claude AI course sell",
    "Claude AI Etsy", "Claude AI print on demand", "Claude AI make money online 2026",
    "Claude AI make money 2025", "Claude Code micro SaaS", "Claude Code app store",
    "Claude Code iOS app money", "Claude Code n8n", "Claude AI automation make money",
    "Claude Opus make money", "Claude Sonnet make money", "Claude AI beginners money",
    "Claude AI earn", "Claude AI tutorial make money", "Claude AI social media agency",
    "Claude AI content creation money", "Claude Code chrome extension money",
    "Claude AI prompts sell", "Claude AI templates sell", "Claude Code MRR",
    "Claude AI one person business", "Claude Code solopreneur", "Claude AI hustle",
    "Claude AI writing jobs", "Claude AI copywriting money", "Claude agent SDK business",
]

session = requests.Session()
calls = {"search": 0, "videos": 0, "channels": 0}

def get(endpoint, params):
    key = hashlib.md5((endpoint + json.dumps(params, sort_keys=True)).encode()).hexdigest()
    fp = os.path.join(CACHE, key + ".json")
    if os.path.exists(fp):
        return json.load(open(fp))
    for attempt in range(4):
        r = session.get(BASE + endpoint, params=params, timeout=60)
        if r.status_code == 200:
            d = r.json()
            json.dump({"params": params, "endpoint": endpoint, "resp": d}, open(fp, "w"))
            calls[endpoint] += 1
            return {"params": params, "endpoint": endpoint, "resp": d}
        txt = r.text[:500]
        if "quota" in txt.lower():
            print("QUOTA EXCEEDED", txt, file=sys.stderr)
            raise SystemExit(2)
        print("ERR", r.status_code, txt, file=sys.stderr)
        time.sleep(2 * (attempt + 1))
    return None

PLANS = [  # (order, publishedAfter, pages)
    ("relevance", None, 3),
    ("viewCount", None, 3),
    ("date", None, 2),
    ("relevance", "2025-01-01T00:00:00Z", 2),
    ("viewCount", "2025-01-01T00:00:00Z", 2),
    ("viewCount", "2026-01-01T00:00:00Z", 2),
    ("relevance", "2026-01-01T00:00:00Z", 1),
]

def main():
    hits = {}  # vid -> list of (query, order, after)
    maxq = int(sys.argv[1]) if len(sys.argv) > 1 else len(QUERIES)
    for q in QUERIES[:maxq]:
        for order, after, pages in PLANS:
            token = None
            for p in range(pages):
                params = {"part": "snippet", "q": q, "type": "video", "maxResults": 50, "order": order}
                if after: params["publishedAfter"] = after
                if token: params["pageToken"] = token
                res = get("search", params)
                if not res: break
                d = res["resp"]
                for it in d.get("items", []):
                    vid = it["id"].get("videoId")
                    if vid:
                        hits.setdefault(vid, []).append([q, order, after or ""])
                token = d.get("nextPageToken")
                if not token: break
        print(f"{q!r}: cumulative unique={len(hits)} new_calls={calls}", flush=True)
    json.dump(hits, open(os.path.join(DATA, "search_hits.json"), "w"))
    # fetch details
    ids = list(hits)
    details = {}
    for i in range(0, len(ids), 50):
        batch = ids[i:i + 50]
        res = get("videos", {"part": "snippet,statistics,contentDetails", "id": ",".join(batch), "maxResults": 50})
        if res:
            for it in res["resp"].get("items", []):
                details[it["id"]] = it
    json.dump(details, open(os.path.join(DATA, "video_details.json"), "w"))
    # channels
    chans = sorted({v["snippet"]["channelId"] for v in details.values()})
    cdet = {}
    for i in range(0, len(chans), 50):
        res = get("channels", {"part": "snippet,statistics", "id": ",".join(chans[i:i + 50]), "maxResults": 50})
        if res:
            for it in res["resp"].get("items", []):
                cdet[it["id"]] = it
    json.dump(cdet, open(os.path.join(DATA, "channel_details.json"), "w"))
    print("done", len(hits), len(details), calls)

if __name__ == "__main__":
    main()
