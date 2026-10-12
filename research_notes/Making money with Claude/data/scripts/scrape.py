#!/usr/bin/env python3
"""Fallback discovery: YouTube web search (public results page + continuation) because
Data API search quota (100 search calls/day) was exhausted. Only video IDs are taken;
metadata is then fetched from the official Data API videos endpoint."""
import json, os, re, sys, time, hashlib, requests

DATA = "/home/user/AI-STUFF/research_notes/Making money with Claude/data"
CACHE = os.path.join(DATA, "raw_web_search_cache")
os.makedirs(CACHE, exist_ok=True)
sys.path.insert(0, os.path.dirname(__file__))
from collect import QUERIES

EXTRA = [
    "how to make money with claude code", "claude code money", "claude code passive income",
    "claude code side hustle 2026", "claude cowork", "claude cowork side hustle", "claude skills sell",
    "claude code agency clients", "claude code freelance", "claude ai make money fast",
    "claude ai online business", "claude code build apps sell", "claude ganar dinero", "ganar dinero con claude",
    "claude ai paise kaise kamaye", "claude ai se paise kamaye", "ganhar dinheiro com claude", "claude code dinheiro",
    "claude ai faceless channel", "claude ai youtube automation", "claude ai kindle", "claude ai etsy digital products",
    "claude code trading bot", "claude polymarket bot", "claude ai stock trading", "claude ai sell websites",
    "claude ai web design business", "claude code saas revenue", "claude code mrr", "built with claude code revenue",
    "claude ai agency", "claude ai consulting business", "claude ai $1000 a day", "claude ai $100 a day",
    "claude code $5k month", "claude ai millionaire", "claude ai money printer", "anthropic claude business",
    "claude mcp business", "claude ai notion templates sell", "claude ai prompts business", "claude ai voice agent",
    "claude ai receptionist", "claude code chatbot business", "claude ai cold outreach", "claude ai ugc",
    "claude ai tiktok money", "claude ai instagram money", "claude ai content business", "claude artifacts business",
    "claude code mobile app revenue", "claude code ios app", "claude code games money", "claude ai newsletter business",
    "vibe coding side hustle", "vibe coding business", "vibe coding saas", "vibe coding agency", "claude vs chatgpt business",
    "claude ai skool", "claude ai course", "claude code course make money", "claude opus 4 business", "claude fable money",
    "claude ai entrepreneur", "claude ai small business", "claude ai real estate", "claude ai seo agency",
    "claude ai printables", "claude ai children's book", "claude ai side hustle beginners",
]
ALLQ = list(dict.fromkeys([q.lower() for q in QUERIES] + EXTRA))
VARIANTS = [(None, 6), ("CAM%3D", 5), ("CAI%3D", 3), ("EgIIBQ%3D%3D", 3), ("CAMSAggF", 4)]

S = requests.Session()
S.headers.update({"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
                  "Accept-Language": "en-US,en;q=0.9"})
CLIENT_VER = "2.20240101.00.00"
VISITOR = ""

def cached(key, fn):
    fp = os.path.join(CACHE, hashlib.md5(key.encode()).hexdigest() + ".json")
    if os.path.exists(fp):
        return json.load(open(fp))
    d = fn()
    if d is not None:
        json.dump(d, open(fp, "w"))
    time.sleep(0.2)
    return d

def walk(o, out, conts):
    if isinstance(o, dict):
        if "videoRenderer" in o:
            vr = o["videoRenderer"]
            if vr.get("videoId"):
                out.append(vr["videoId"])
        if "reelWatchEndpoint" in o and o["reelWatchEndpoint"].get("videoId"):
            out.append(o["reelWatchEndpoint"]["videoId"])
        if "continuationItemRenderer" in o:
            t = o["continuationItemRenderer"].get("continuationEndpoint", {}).get("continuationCommand", {}).get("token")
            if t: conts.append(t)
        for v in o.values():
            walk(v, out, conts)
    elif isinstance(o, list):
        for v in o:
            walk(v, out, conts)

def first_page(q, sp):
    global CLIENT_VER, VISITOR
    url = "https://www.youtube.com/results"
    params = {"search_query": q, "hl": "en", "gl": "US"}
    if sp: params["sp"] = requests.utils.unquote(sp)
    r = S.get(url, params=params, timeout=60)
    if r.status_code != 200:
        print("HTTP", r.status_code, q, file=sys.stderr); return None
    m = re.search(r'"INNERTUBE_CLIENT_VERSION":"([^"]+)"', r.text)
    if m: CLIENT_VER = m.group(1)
    m = re.search(r'"VISITOR_DATA":"([^"]+)"', r.text)
    if m: VISITOR = m.group(1)
    m = re.search(r"var ytInitialData = (\{.*?\});</script>", r.text, re.S)
    if not m:
        print("no initial data", q, file=sys.stderr); return None
    data = json.loads(m.group(1))
    ids, conts = [], []
    walk(data, ids, conts)
    return {"ids": list(dict.fromkeys(ids)), "cont": conts[0] if conts else None}

def next_page(token):
    body = {"context": {"client": {"clientName": "WEB", "clientVersion": CLIENT_VER, "hl": "en", "gl": "US", "visitorData": VISITOR}}, "continuation": token}
    r = S.post("https://www.youtube.com/youtubei/v1/search?prettyPrint=false", json=body, timeout=60, headers={"X-Goog-Visitor-Id": VISITOR})
    if r.status_code != 200:
        print("HTTP cont", r.status_code, file=sys.stderr); return None
    ids, conts = [], []
    walk(r.json(), ids, conts)
    return {"ids": list(dict.fromkeys(ids)), "cont": conts[0] if conts else None}

def main():
    hits = {}
    k = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    for qi, q in enumerate(ALLQ):
        if qi % n != k: continue
        for sp, pages in VARIANTS:
            pg = cached(f"{q}|{sp}|0", lambda: first_page(q, sp))
            for p in range(pages):
                if not pg: break
                for vid in pg["ids"]:
                    hits.setdefault(vid, []).append([q, sp or "relevance", "web"])
                if not pg.get("cont") or p == pages - 1: break
                tok = pg["cont"]
                pg = cached(f"{q}|{sp}|{p+1}|{tok[:40]}", lambda: next_page(tok))
        print(qi, q, "unique so far", len(hits), flush=True)
    json.dump(hits, open(os.path.join(DATA, f"web_search_hits_{k}of{n}.json"), "w"))
    print("DONE", len(hits))

if __name__ == "__main__":
    main()
