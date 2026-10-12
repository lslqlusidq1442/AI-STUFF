#!/usr/bin/env python3
"""Merge API-search hits (from cache) + web-search hits; fetch details via Data API videos/channels."""
import json, os, glob, sys
sys.path.insert(0, os.path.dirname(__file__))
from collect import get, DATA

hits = {}
n_api_calls = 0
for fp in glob.glob(os.path.join(DATA, "raw_search_cache", "*.json")):
    d = json.load(open(fp))
    if d.get("endpoint") != "search":
        continue
    n_api_calls += 1
    p = d["params"]
    for it in d["resp"].get("items", []):
        vid = it["id"].get("videoId")
        if vid:
            hits.setdefault(vid, []).append([p["q"], p.get("order"), p.get("publishedAfter", ""), "api"])
n_api = len(hits)
for wf in glob.glob(os.path.join(DATA, "web_search_hits_*of8.json")):
    for vid, hs in json.load(open(wf)).items():
        hits.setdefault(vid, []).extend(hs)
print("api search calls", n_api_calls, "api unique", n_api, "total unique", len(hits))
json.dump(hits, open(os.path.join(DATA, "search_hits.json"), "w"))

details = {}
ids = sorted(hits)
for i in range(0, len(ids), 50):
    res = get("videos", {"part": "snippet,statistics,contentDetails", "id": ",".join(ids[i:i + 50]), "maxResults": 50})
    if res:
        for it in res["resp"].get("items", []):
            details[it["id"]] = it
json.dump(details, open(os.path.join(DATA, "video_details.json"), "w"))
chans = sorted({v["snippet"]["channelId"] for v in details.values()})
cdet = {}
for i in range(0, len(chans), 50):
    res = get("channels", {"part": "snippet,statistics", "id": ",".join(chans[i:i + 50]), "maxResults": 50})
    if res:
        for it in res["resp"].get("items", []):
            cdet[it["id"]] = it
json.dump(cdet, open(os.path.join(DATA, "channel_details.json"), "w"))
print("details", len(details), "channels", len(cdet))
