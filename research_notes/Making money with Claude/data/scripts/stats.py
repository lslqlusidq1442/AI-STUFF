#!/usr/bin/env python3
"""Compute summary tables from videos_classified.json -> stats.md (markdown tables)."""
import json, os, re, statistics as st, collections

DATA = "/home/user/AI-STUFF/research_notes/Making money with Claude/data"
rows = json.load(open(os.path.join(DATA, "videos_classified.json")))
hits = json.load(open(os.path.join(DATA, "search_hits.json")))
sys_path = os.path.dirname(__file__)
import sys; sys.path.insert(0, sys_path)
from analyze import METHODS
LABEL = {k: l for k, l, _ in METHODS}
LABEL["unclassified"] = "Unclassified by title (generic 'make money with Claude' / unclear)"
LABEL["multi_method_listicle"] = "Multi-method listicle (e.g. '7 ways to make money with Claude'), no single method in title"
out = []
P = out.append

def med(xs): return st.median(xs) if xs else 0
def pct(a, b): return f"{100*a/b:.1f}%" if b else "n/a"
def fmt(n): return f"{n:,.0f}"

tiers = collections.Counter(r["tier"] for r in rows)
R = [r for r in rows if r["tier"] in ("A1_claude_money_in_title", "B_ai_money_title_no_claude_mention")]
A = [r for r in rows if r["tier"] == "A1_claude_money_in_title"]
P(f"# Stats (generated)\n\nTotal unique video IDs with metadata: {len(rows)}\n")
P("| Tier | n |\n|---|---|")
for k, v in sorted(tiers.items()): P(f"| {k} | {v} |")
src = collections.Counter()
for r in R:
    s = {h[-1] if h[-1] in ("api", "web") else "api" for h in hits.get(r["video_id"], [])}
    src["+".join(sorted(s))] += 1
P(f"\nRelevant set R (A+B) = {len(R)}; Claude-explicit A = {len(A)}. Discovery source in R: {dict(src)}")
P(f"Claude/Anthropic in title (R): {sum(r['claude_in_title'] for r in R)}")
P(f"Shorts (<=60s) in R: {sum(r['is_short_le60'] for r in R)}; <=180s: {sum(r['le180'] for r in R)}")
P(f"Partner/ad-tagged (#...partner, Anzeige, #ad) in R: {sum(r['partner_tag'] for r in R)}")
P(f"Listicle-style multi-method titles in R: {sum(r['listicle'] for r in R)}")
yrs = collections.Counter(r["year"] for r in R)
P("\n## Year distribution (R)\n| Year | n | % |\n|---|---|---|")
for y in sorted(yrs): P(f"| {y} | {yrs[y]} | {pct(yrs[y], len(R))} |")
q = collections.Counter(r["quarter"] for r in R if r["year"] >= "2025")
P("\n| Quarter | n |\n|---|---|")
for k in sorted(q): P(f"| {k} | {q[k]} |")
langs = collections.Counter((r["lang"] or "unset").split("-")[0] for r in R)
P(f"\nAudio/default language (R, top): {langs.most_common(12)}")

def method_table(S, name):
    n = len(S)
    anyc = collections.Counter(m for r in S for m in r["methods"])
    tit = collections.Counter(m for r in S if r["method_src"] == "title" for m in r["methods"])
    prim = collections.Counter(r["primary_method"] for r in S)
    P(f"\n## Method frequency — {name} (n={n})\n")
    P("| Method | any-label n | any % | title-only n | primary n | primary % |\n|---|---|---|---|---|---|")
    keys = sorted(set(anyc) | set(prim), key=lambda k: -(anyc.get(k, 0) or prim.get(k, 0)))
    for k in keys:
        P(f"| {LABEL.get(k,k)} | {anyc.get(k,0)} | {pct(anyc.get(k,0), n)} | {tit.get(k,0)} | {prim.get(k,0)} | {pct(prim.get(k,0), n)} |")
    P(f"\nClassified from title: {sum(r['method_src']=='title' for r in S)} ({pct(sum(r['method_src']=='title' for r in S), n)}); only via description head (low confidence, not used for primary): {sum(r['method_src']=='desc' for r in S)}; no match anywhere: {sum(r['method_src']=='none' for r in S)}")
    fb = collections.Counter(r["primary_method_desc_fallback"] for r in S if r["method_src"] == "desc")
    P(f"Low-confidence description-fallback labels for title-unclassified videos: {fb.most_common()}")

method_table(R, "relevant set R")
method_table(A, "Claude-explicit set A")

def perf_table(S, name, key="primary_method"):
    P(f"\n## Performance by primary method — {name}\n")
    P("| Method | n | total views | median views | mean views | median views/subscriber | median engagement (likes+comments)/views, videos >=1k views | n with >=100k views |\n|---|---|---|---|---|---|---|---|")
    g = collections.defaultdict(list)
    for r in S: g[r[key]].append(r)
    for k, vs in sorted(g.items(), key=lambda kv: -sum(r["views"] for r in kv[1])):
        views = [r["views"] for r in vs]
        vps = [r["views"] / r["subs"] for r in vs if r["subs"] > 0 and not r["subs_hidden"]]
        eng = [((r["likes"] or 0) + (r["comments"] or 0)) / r["views"] for r in vs if r["views"] >= 1000 and r["likes"] is not None]
        P(f"| {LABEL.get(k,k)} | {len(vs)} | {fmt(sum(views))} | {fmt(med(views))} | {fmt(st.mean(views))} | {med(vps):.3f} | {med(eng)*100:.2f}% | {sum(v>=100000 for v in views)} |")
perf_table(R, "R")
perf_table([r for r in R if not r["is_short_le60"]], "R excluding Shorts <=60s")

# any-label performance
P("\n## Performance by any-label method (video counted in each matching method) — R\n")
P("| Method | n | total views | median views | median views/sub |\n|---|---|---|---|---|")
for k, _, _ in METHODS:
    vs = [r for r in R if k in r["methods"]]
    if not vs: continue
    vps = [r["views"] / r["subs"] for r in vs if r["subs"] > 0 and not r["subs_hidden"]]
    P(f"| {LABEL[k]} | {len(vs)} | {fmt(sum(r['views'] for r in vs))} | {fmt(med([r['views'] for r in vs]))} | {med(vps):.3f} |")

# income claims
inc = [r for r in R if r["income_claims_title"]]
P(f"\n## Income claims in titles (R)\nTitles with a currency/income figure: {len(inc)} / {len(R)} ({pct(len(inc), len(R))}); in A: {sum(1 for r in A if r['income_claims_title'])} / {len(A)}")
per = collections.Counter(p for r in inc for p in (r["income_periods"] or ["no period (lump sum / unspecified)"]))
P(f"Periods: {dict(per)}")
for y in ("2024", "2025", "2026"):
    S = [r for r in R if r["year"] == y]
    P(f"- {y}: {sum(1 for r in S if r['income_claims_title'])}/{len(S)} ({pct(sum(1 for r in S if r['income_claims_title']), len(S))})")
P(f"Median views, titles with income claim: {fmt(med([r['views'] for r in inc]))}; without: {fmt(med([r['views'] for r in R if not r['income_claims_title']]))}")
P(f"Median views (non-Shorts), with claim: {fmt(med([r['views'] for r in inc if not r['is_short_le60']]))}; without: {fmt(med([r['views'] for r in R if not r['income_claims_title'] and not r['is_short_le60']]))}")

def amount_usd_month(s):
    s0 = s.lower().replace(",", "")
    if not re.search(r"\$|usd", s0): return None
    m = re.search(r"(\d+(?:\.\d+)?)\s?(k|m|million)?", s0)
    if not m: return None
    v = float(m.group(1)) * {"k": 1e3, "m": 1e6, "million": 1e6, None: 1}[m.group(2)]
    if re.search(r"/\s?d|day|daily", s0): return v * 30
    if re.search(r"week|wk", s0): return v * 4.33
    if re.search(r"/\s?y|year|yr|\barr\b", s0): return v / 12
    if re.search(r"mo|month|mrr", s0): return v
    return None
mon = [(amount_usd_month(c), r) for r in inc for c in r["income_claims_title"]]
mon = [(v, r) for v, r in mon if v]
if mon:
    vals = sorted(v for v, _ in mon)
    P(f"USD claims with explicit period, normalised to $/month: n={len(vals)}, median ${med(vals):,.0f}/mo, p25 ${vals[len(vals)//4]:,.0f}, p75 ${vals[3*len(vals)//4]:,.0f}, max ${vals[-1]:,.0f}")
    buckets = collections.Counter()
    for v in vals:
        b = "<$1k/mo" if v < 1e3 else "$1k-<$10k/mo" if v < 1e4 else "$10k-<$50k/mo" if v < 5e4 else "$50k-<$100k/mo" if v < 1e5 else ">=$100k/mo"
        buckets[b] += 1
    P(f"Buckets: {dict(buckets)}")
P("\nIncome claim by primary method (share of titles with a figure):")
g = collections.defaultdict(list)
for r in R: g[r["primary_method"]].append(r)
for k, vs in sorted(g.items(), key=lambda kv: -len(kv[1])):
    P(f"- {k}: {sum(1 for r in vs if r['income_claims_title'])}/{len(vs)} ({pct(sum(1 for r in vs if r['income_claims_title']), len(vs))})")
P("\nTop-viewed titles with income claims:")
for r in sorted(inc, key=lambda r: -r["views"])[:25]:
    P(f"- {fmt(r['views'])} views | {r['published']} | {r['channel']} | \"{r['title']}\" | claims: {r['income_claims_title']} | {r['url']}")

# time shift
P("\n## Method mix by year (primary method, R)\n")
yrs_l = ["2023", "2024", "2025", "2026"]
P("| Method | " + " | ".join(f"{y} n (%)" for y in yrs_l) + " |\n|---|" + "---|" * len(yrs_l))
ny = {y: [r for r in R if r["year"] == y] for y in yrs_l}
allk = sorted({r["primary_method"] for r in R}, key=lambda k: -sum(1 for r in R if r["primary_method"] == k))
for k in allk:
    P(f"| {k} | " + " | ".join(f"{sum(1 for r in ny[y] if r['primary_method']==k)} ({pct(sum(1 for r in ny[y] if r['primary_method']==k), len(ny[y]))})" for y in yrs_l) + " |")
P("| TOTAL | " + " | ".join(str(len(ny[y])) for y in yrs_l) + " |")
P("\n## Method mix by half-year 2025-2026 (any-label share, R)\n")
halves = [("2025H1", lambda r: r["published"][:7] <= "2025-06" and r["year"] == "2025"), ("2025H2", lambda r: r["year"] == "2025" and r["published"][:7] > "2025-06"),
          ("2026H1", lambda r: r["year"] == "2026" and r["published"][:7] <= "2026-06"), ("2026H2(to Oct12)", lambda r: r["year"] == "2026" and r["published"][:7] > "2026-06")]
hs = {h: [r for r in R if f(r)] for h, f in halves}
P("| Method | " + " | ".join(h for h, _ in halves) + " |\n|---|" + "---|" * len(halves))
for k, _, _ in METHODS:
    P(f"| {k} | " + " | ".join(pct(sum(1 for r in hs[h] if k in r['methods']), len(hs[h])) for h, _ in halves) + " |")
P("| n | " + " | ".join(str(len(hs[h])) for h, _ in halves) + " |")
P("\nClaude product mentions in title by year (R): ")
for y in yrs_l:
    S = ny[y]
    P(f"- {y}: n={len(S)}, 'Claude Code' in title {sum(1 for r in S if re.search(r'claude\s?code', r['title'], re.I))}, 'Cowork' {sum(1 for r in S if re.search(r'cowork', r['title'], re.I))}, 'skill' {sum(1 for r in S if re.search(r'skills?', r['title'], re.I))}, 'MCP' {sum(1 for r in S if re.search(r'\bmcp\b', r['title'], re.I))}, 'vibe cod' {sum(1 for r in S if re.search(r'vibe[\s-]?cod', r['title'], re.I))}, 'artifact' {sum(1 for r in S if re.search(r'artifact', r['title'], re.I))}, income-claim titles {sum(1 for r in S if r['income_claims_title'])}")

# channels
P("\n## Channels (R)\n")
ch = collections.defaultdict(list)
for r in R: ch[r["channel_id"]].append(r)
P(f"Unique channels: {len(ch)}; channels with >=3 videos in R: {sum(1 for v in ch.values() if len(v)>=3)}; with 1 video: {sum(1 for v in ch.values() if len(v)==1)}")
tot = sum(r["views"] for r in R)
topv = sorted(ch.values(), key=lambda vs: -sum(r["views"] for r in vs))
P(f"Top 10 channels' share of total views in R: {pct(sum(sum(r['views'] for r in vs) for vs in topv[:10]), tot)}; top 25: {pct(sum(sum(r['views'] for r in vs) for vs in topv[:25]), tot)}; total views R = {fmt(tot)}")
P("\n### Top 30 channels by total views in R\n| Channel | videos in R | total views | subscribers | median views | sells course/community? (desc signals across its videos) |\n|---|---|---|---|---|---|")
sig_keys = ["skool", "whop", "course_or_academy", "community", "coaching_consult", "affiliate_links", "sponsor", "digital_store"]
def chsig(vs): return [k for k in sig_keys if any(r["desc_" + k] for r in vs)]
for vs in topv[:30]:
    P(f"| {vs[0]['channel']} | {len(vs)} | {fmt(sum(r['views'] for r in vs))} | {fmt(vs[0]['subs'])} | {fmt(med([r['views'] for r in vs]))} | {', '.join(chsig(vs))} |")
P("\n### Top 20 channels by number of videos in R\n| Channel | videos | total views | subs |\n|---|---|---|---|")
for vs in sorted(ch.values(), key=lambda vs: -len(vs))[:20]:
    P(f"| {vs[0]['channel']} | {len(vs)} | {fmt(sum(r['views'] for r in vs))} | {fmt(vs[0]['subs'])} |")
P("\n### Monetisation signals in descriptions\n| Signal | % of videos in R | % of channels in R (any video) | % of top-50-by-views channels |\n|---|---|---|---|")
top50 = topv[:50]
for k in sig_keys:
    P(f"| {k} | {pct(sum(r['desc_'+k] for r in R), len(R))} | {pct(sum(1 for vs in ch.values() if any(r['desc_'+k] for r in vs)), len(ch))} | {pct(sum(1 for vs in top50 if any(r['desc_'+k] for r in vs)), len(top50))} |")
own = lambda r: r["desc_skool"] or r["desc_whop"] or r["desc_course_or_academy"] or r["desc_community"] or r["desc_coaching_consult"] or r["desc_digital_store"]
P(f"| ANY own-offer signal (skool/whop/course/community/coaching/store) | {pct(sum(own(r) for r in R), len(R))} | {pct(sum(1 for vs in ch.values() if any(own(r) for r in vs)), len(ch))} | {pct(sum(1 for vs in top50 if any(own(r) for r in vs)), len(top50))} |")
P(f"| skool OR whop (hard signal) | {pct(sum(r['desc_skool'] or r['desc_whop'] for r in R), len(R))} | {pct(sum(1 for vs in ch.values() if any(r['desc_skool'] or r['desc_whop'] for r in vs)), len(ch))} | {pct(sum(1 for vs in top50 if any(r['desc_skool'] or r['desc_whop'] for r in vs)), len(top50))} |")
nsh = [r for r in R if not r["is_short_le60"]]
P(f"\nAmong non-Shorts in R (n={len(nsh)}): skool.com link {pct(sum(r['desc_skool'] for r in nsh), len(nsh))}; any own-offer {pct(sum(own(r) for r in nsh), len(nsh))}; affiliate {pct(sum(r['desc_affiliate_links'] for r in nsh), len(nsh))}")

# top 30
P("\n## Top 30 most-viewed videos in R\n| # | Views | Published | Channel | Title | Primary method | All methods | Claude in title/desc | URL |\n|---|---|---|---|---|---|---|---|---|")
for i, r in enumerate(sorted(R, key=lambda r: -r["views"])[:30], 1):
    t = r["title"].replace("|", "/")
    P(f"| {i} | {fmt(r['views'])} | {r['published']} | {r['channel']} | {t} | {r['primary_method']} | {', '.join(r['methods'])} | {'Y' if r['claude_any'] else 'N'} | {r['url']} |")
P("\n## Top 30 most-viewed Claude-in-title videos (R)\n| # | Views | Published | Channel | Title | Primary method | URL |\n|---|---|---|---|---|---|---|")
for i, r in enumerate(sorted([r for r in R if r["claude_in_title"]], key=lambda r: -r["views"])[:30], 1):
    t = r["title"].replace("|", "/")
    P(f"| {i} | {fmt(r['views'])} | {r['published']} | {r['channel']} | {t} | {r['primary_method']} | {r['url']} |")
open(os.path.join(DATA, "stats.md"), "w").write("\n".join(out))
print("\n".join(out)[:3000])
