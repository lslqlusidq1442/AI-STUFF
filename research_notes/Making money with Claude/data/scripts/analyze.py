#!/usr/bin/env python3
"""Filter, classify and summarise the collected YouTube metadata."""
import json, os, re, csv, statistics, collections, sys

DATA = "/home/user/AI-STUFF/research_notes/Making money with Claude/data"
hits = json.load(open(os.path.join(DATA, "search_hits.json")))
det = json.load(open(os.path.join(DATA, "video_details.json")))
chans = json.load(open(os.path.join(DATA, "channel_details.json")))

CLAUDE_RE = re.compile(r"\bclaude|anthropic|claude[\s-]?code|claudecode|\bcowork\b", re.I)
CLAUDE_TITLE_RE = re.compile(r"\bclaude|anthropic", re.I)
AI_RE = re.compile(r"\bai\b|a\.i\.|chatgpt|gpt|llm|vibe[\s-]?cod|agent|automation|claude|gemini|cursor|lovable|n8n|\bia\b", re.I)
STRONG_RE = re.compile(
    r"make\s+money|making\s+money|\bmoney\b|\bearn|income|revenue|\bmrr\b|\barr\b|profit|side[\s-]?hustle|hustle|passive|"
    r"\$\s?\d|\d\s?k\s?(?:/|per|a)\s?(?:mo|month|day|week|year)|per\s+month|/mo\b|/month|a\s+month\b|"
    r"monetiz|\bcash\b|millionaire|salary|\$\$|💰|💸|"
    r"ganar|dinero|dinheiro|ganhar|ingresos|\brenda\b|"
    r"kamaye|kamao|kamai|kamana|paise|paisa|rupees|₹|\blakh|crore|€\s?\d|£\s?\d|\d\s?€|"
    r"수익|돈|부업|稼|副業|収益|収入|geld\s+verdienen|nebenjob|nebeneinkommen|gagner\s+de\s+l|argent\b|कमा|पैसे|कमाई|guadagn|soldi|zarab|para\s+kazan|заработ|деньг|doanh\s+thu|kiếm\s+tiền|\buang\b|penghasilan",
    re.I)
WEAK_RE = re.compile(r"\bsell|selling|\bsold\b|\bclients?\b|agency|freelanc|fiverr|upwork|business|startup|entrepreneur|\bjobs?\b|\brich\b|\bpays?\b|negocio|neg[oó]cio|empreend|emprend", re.I)
SAVE_RE = re.compile(r"sav(?:e|ing|es)\s+(?:you\s+)?(?:\w+\s+)?money|save\s+\$", re.I)
NEWS_RE = re.compile(r"credits?\b|\bplan\b|subscription|pricing|\bprice|\bcosts?\b|billion|valuation|funding|raised|ipo\b|stock\s+price|for\s+free|\bfree\s+claude|claude\s+(?:max|pro)\b|rate\s+limit|tokens?\b|\bapi\s+bill", re.I)
MAKE_RE = re.compile(r"make\s+money|making\s+money|\bearn|income|side[\s-]?hustle|hustle|passive|\bsell|\bsold\b|clients?|agency|freelanc|profit|\bmrr\b|/\s?mo|per\s+month|a\s+month|/\s?day|a\s+day|business|ganar|dinheiro|dinero|kamaye|kamai|paise|\bi\s+made\b|made\s+\$|\bmy\s+\$", re.I)
def strong(t): return bool(STRONG_RE.search(SAVE_RE.sub(" ", t)))

# Method categories: (key, label, regex). Matched on title first; description head as fallback.
METHODS = [
    ("automation_agency", "AI automation agency / selling automations & workflows to businesses",
     r"automation\s+agency|\bai\s+agency|\baaa\b|sell(?:ing)?\s+(?:ai\s+)?automations?|automat(?:e|ion|ions|ing)\b|automatiz|n8n|make\.com|zapier|workflows?\b|\bagency\b|agencia|ag[eê]ncia"),
    ("saas_apps", "Build & sell SaaS / micro-SaaS / apps / software (incl. vibe coding)",
     r"saas|micro[\s-]?saas|\bapps?\b|\bmrr\b|\barr\b|software|startup|\bios\b|mobile\s+app|chrome\s+extension|vibe[\s-]?cod|product\s+hunt|web\s?app|aplicaci|aplicativo|\btools?\b\s+(?:that|to)\s+sell|build\s*(?:&|and)\s*sell|built\s+(?:a|an|my)\s+\$|indie\s+hack|app\s+store|\bgames?\b"),
    ("websites_local", "Building/selling websites (often to local businesses)",
     r"websites?|web\s?design|landing\s+pages?|local\s+business|p[aá]ginas?\s+web|sitio\s+web|sites?\s+(?:para|for)"),
    ("skills_prompts_templates", "Selling Claude skills / prompts / templates / GPTs / MCP servers / plugins",
     r"sell\w*\s+(?:\w+\s+){0,3}(?:skills?|prompts?|templates?|gpts?|plugins?|mcps?)\b|(?:skills?|prompts?|templates?|gpts|plugins?|mcp\s+servers?|mcps?)\s+(?:\w+\s+){0,2}(?:to\s+sell|for\s+sale|marketplace|business|for\s+money|that\s+(?:make|sell|earn))|prompt\s+packs?|notion\s+templates?|template\s+business|gpt\s+store|skills?\s+(?:marketplace|store)|plantillas|monetiz\w*\s+(?:\w+\s+){0,2}(?:skills?|mcp|plugins?|prompts?)|(?:skills?|mcp\s+servers?|plugins?|prompts?)\s+(?:\w+\s+){0,3}(?:\$\d|\d+k|income|revenue|money)"),
    ("digital_products", "Digital products / ebooks / KDP / Etsy / print-on-demand",
     r"e-?books?|\bkdp\b|kindle|amazon\s+books?|children'?s\s+books?|coloring\s+books?|low[\s-]content|digital\s+products?|pdfs?\b|stories\b|gumroad|etsy|print[\s-]on[\s-]demand|\bpod\b|planners?|workbooks?|\bbooks?\b|libros?|livros?|productos?\s+digitales|produtos?\s+digitais"),
    ("faceless_content", "Faceless YouTube / TikTok / Instagram / short-form content",
     r"faceless|youtube\s+automation|youtube\s+channel|\bchannel\b|shorts\b|tiktok|instagram|reels?\b|cash\s?cow|viral|\bugc\b|theme\s+pages?|content\s+creat|youtube|canal|ai\s+influencer|ai\s+videos?|podcast"),
    ("blogging_seo_affiliate", "Blogging / SEO / affiliate / niche sites / Pinterest",
     r"\bblog|\bseo\b|affiliate|afiliad|niche\s+sites?|pinterest|amazon\s+associates|programmatic\s+seo"),
    ("newsletter", "Newsletters",
     r"newsletter|substack|beehiiv"),
    ("trading_crypto", "Trading / investing / crypto / prediction-market bots",
     r"trading|\btrade|traders?|stocks?\b|stock\s+market|crypto|bitcoin|forex|polymarket|kalshi|prediction\s+market|options\b|tradingview|zerodha|invest|hedge\s+fund|portfolio|bolsa|mercado\s+de\s+valores|betting|sports\s+bet"),
    ("chatbots_voice_agents", "AI chatbots / voice agents / receptionists for businesses",
     r"chat\s?bots?|voice\s+agents?|voice\s+ai|ai\s+receptionist|receptionist|vapi|retell|customer\s+(?:service|support)\s+(?:bot|agent)|phone\s+agent|call\s+agent"),
    ("leadgen_cold_email", "Lead generation / cold email / outreach / sales",
     r"lead\s?gen|leads?\b|cold\s+(?:email|emails|outreach|call|calling|dm)|outreach|prospect|apollo|\bclay\b|appointment\s+setting|sales\s+(?:agent|team|calls?)|get\s+clients|find\s+clients|land\s+clients"),
    ("course_coaching", "Selling courses / coaching / info products / community about AI",
     r"sell(?:ing)?\s+(?:a\s+|an\s+|your\s+)?(?:online\s+)?courses?|online\s+courses?|course\s+creat|coaching|info\s?products?|\bskool\b|consult(?:ing|ant)|teach(?:ing)?\s+ai|workshops?|cursos?"),
    ("freelancing", "Freelancing / gigs (Upwork, Fiverr, services)",
     r"freelanc|upwork|fiverr|\bgigs?\b|contra\b|services?\s+(?:to|for)\s+(?:clients|businesses)|copywrit|ghostwrit|virtual\s+assistant|data\s+entry|translation|writing\s+jobs|remote\s+jobs?"),
    ("ecommerce", "E-commerce / dropshipping / Shopify / Amazon FBA",
     r"dropship|shopify|e-?commerce|amazon\s+fba|\bfba\b|online\s+store|tienda|loja"),
    ("jobs_career", "AI skills for jobs / career / salary",
     r"\bjobs?\b|salary|career|hired|high[\s-]paying\s+skill|resume|interview|empleo|trabajo"),
    ("one_person_business_agents", "AI agents / 'AI employees' / one-person business (generic)",
     r"ai\s+agents?|agentic|ai\s+employees?|one[\s-]person\s+(?:business|company)|solopreneur|1[\s-]person|solo\s+(?:business|founder)|ai\s+workforce|digital\s+employees?|agent\s+sdk|business\s+in\s+a\s+box|build\s+a\s+business|business\s+from\s+scratch"),
]
METHODS = [(k, l, re.compile(r, re.I)) for k, l, r in METHODS]
LISTICLE_RE = re.compile(r"\b\d+\s+(?:\w+\s+){0,3}(?:ways|ideas|side\s+hustles|business(?:es)?|methods|hustles|formas|maneiras|ideias|ideas)\b|ways\s+to\s+make\s+money|business\s+ideas|side\s+hustles\b|formas\s+de\s+ganar", re.I)

# Income claims
INCOME_RE = re.compile(
    r"(?:\$|usd\s?|€|£|₹|rs\.?\s?)\s?\d[\d,\.]*\s?(?:k|m|million|mil|lakh|crore|cr|l)?\+?(?:\s?(?:/|per|a|an|every|in|each)\s?(?:mo\b|month|day|week|wk|year|yr|hour|hr|minutes?|days|months|weeks))?"
    r"|\d[\d,\.]*\s?(?:k|lakh|crore)\s?(?:/|per|a)\s?(?:mo\b|month|day|week|year)"
    r"|\d[\d,\.]*\s?(?:k|m)?\s?(?:mrr|arr)\b"
    r"|\d[\d,\.]*\s?(?:lakh|crore|lakhs|crores)\b|₹\s?\d[\d,]*", re.I)
PERIOD_RE = [("per day", re.compile(r"/\s?day|per\s+day|a\s+day|daily|every\s+day|/\s?d\b", re.I)),
             ("per week", re.compile(r"/\s?w(?:ee)?k|per\s+week|a\s+week", re.I)),
             ("per month", re.compile(r"/\s?mo|per\s+month|a\s+month|monthly|mrr|month\b", re.I)),
             ("per year", re.compile(r"/\s?y(?:ea)?r|per\s+year|a\s+year|annual|\barr\b|year\b", re.I))]

# Monetisation signals in description
SELL_RE = {
    "skool": re.compile(r"skool\.com", re.I),
    "whop": re.compile(r"whop\.com", re.I),
    "course_or_academy": re.compile(r"\bcourse\b|\bcourses\b|academy|masterclass|bootcamp|program\b|cohort|curso", re.I),
    "community": re.compile(r"community|comunidad|comunidade|discord\.gg|join\s+my|members", re.I),
    "coaching_consult": re.compile(r"coaching|mentorship|1:1|1-on-1|book\s+a\s+call|calendly|consult|work\s+with\s+me|hire\s+(?:me|us)|agency", re.I),
    "affiliate_links": re.compile(r"affiliate|commission|\?via=|\?ref=|\?fpr=|\?aff=|ref=\w|partner\s+link|referral|\bcoupon\b|discount\s+code|promo\s+code|use\s+code", re.I),
    "sponsor": re.compile(r"sponsor|sponsored|thanks\s+to\s+\w+\s+for\s+sponsoring|paid\s+promotion", re.I),
    "digital_store": re.compile(r"gumroad|stan\.store|beacons\.ai|payhip|lemonsqueezy|kajabi|teachable|podia|thinkific|linktr\.ee|newsletter", re.I),
}

def dur_secs(iso):
    m = re.match(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso or "")
    if not m: return None
    d, h, mi, s = (int(x or 0) for x in m.groups())
    return d * 86400 + h * 3600 + mi * 60 + s

PRIORITY = ["trading_crypto", "newsletter", "digital_products", "chatbots_voice_agents", "leadgen_cold_email",
            "websites_local", "skills_prompts_templates", "ecommerce", "blogging_seo_affiliate", "faceless_content",
            "freelancing", "course_coaching", "saas_apps", "automation_agency", "one_person_business_agents", "jobs_career"]
SPONSOR_SHORT_RE = re.compile(r"#\w*partner\b|\banzeige\b|#ad\b|#sponsored|paid\s+partnership", re.I)

HASHTAG_RE = re.compile(r"#[\w\-]+", re.U)
def classify(title, desc_head):
    title = HASHTAG_RE.sub(" ", title)
    desc_head = HASHTAG_RE.sub(" ", desc_head)
    t = title
    labels = [k for k, _, r in METHODS if r.search(t)]
    src = "title"
    if not labels:
        labels = [k for k, _, r in METHODS if r.search(desc_head[:300])]
        src = "desc" if labels else "none"
    return labels, src

rows = []
for vid, v in det.items():
    sn, st = v["snippet"], v.get("statistics", {})
    title = sn.get("title", "")
    desc = sn.get("description", "")
    tags = " ".join(sn.get("tags", []) or [])
    full = f"{title}\n{desc}\n{tags}"
    claude_any = bool(CLAUDE_RE.search(full))
    claude_title = bool(CLAUDE_TITLE_RE.search(title))
    money_title_strong = strong(title)
    money_title = money_title_strong or bool(WEAK_RE.search(title))
    money_desc_strong = strong(desc[:300])
    ai_any = bool(AI_RE.search(title + " " + desc[:800] + " " + tags))
    if claude_any and money_title:
        tier = "A1_claude_money_in_title"
    elif claude_any and money_desc_strong:
        tier = "A2_claude_money_in_desc_only"
    elif (not claude_any) and ai_any and money_title_strong:
        tier = "B_ai_money_title_no_claude_mention"
    elif claude_any:
        tier = "C_claude_no_money_signal"
    else:
        tier = "X_irrelevant"
    if tier in ("A1_claude_money_in_title", "B_ai_money_title_no_claude_mention") and NEWS_RE.search(title) and not MAKE_RE.search(title):
        tier = "D_pricing_or_company_news"
    desc_head = desc[:600]
    labels, src = classify(title, desc_head)
    listicle = bool(LISTICLE_RE.search(title))
    inc_title = [m.group(0).strip() for m in INCOME_RE.finditer(title)]
    inc_title = [x for x in inc_title if re.search(r"\d", x) and not re.fullmatch(r"\$?\d{1,2}", x.strip())]
    periods = sorted({p for p, r in PERIOD_RE for x in inc_title if r.search(x)})
    ch = chans.get(sn.get("channelId"), {})
    subs = int(ch.get("statistics", {}).get("subscriberCount", 0) or 0)
    hidden = ch.get("statistics", {}).get("hiddenSubscriberCount", False)
    views = int(st.get("viewCount", 0) or 0)
    likes = int(st.get("likeCount", 0) or 0) if "likeCount" in st else None
    comments = int(st.get("commentCount", 0) or 0) if "commentCount" in st else None
    ds = dur_secs(v.get("contentDetails", {}).get("duration"))
    sell = {k: bool(r.search(desc)) for k, r in SELL_RE.items()}
    rows.append({
        "video_id": vid, "url": f"https://www.youtube.com/watch?v={vid}", "title": title,
        "channel": sn.get("channelTitle", ""), "channel_id": sn.get("channelId"),
        "published": sn.get("publishedAt", "")[:10], "year": sn.get("publishedAt", "")[:4],
        "quarter": sn.get("publishedAt", "")[:4] + "Q" + str((int(sn.get("publishedAt", "2000-01")[5:7]) - 1) // 3 + 1),
        "views": views, "likes": likes, "comments": comments, "subs": subs, "subs_hidden": hidden,
        "duration_s": ds, "is_short_le60": ds is not None and ds <= 60, "le180": ds is not None and ds <= 180,
        "lang": sn.get("defaultAudioLanguage") or sn.get("defaultLanguage") or "",
        "tier": tier, "claude_in_title": claude_title, "claude_any": claude_any,
        "money_in_title": money_title, "money_title_strong": money_title_strong,
        "methods": labels, "method_src": src, "primary_method": (sorted(labels, key=PRIORITY.index)[0] if (labels and src == "title") else ("multi_method_listicle" if listicle else "unclassified")),
        "primary_method_desc_fallback": (sorted(labels, key=PRIORITY.index)[0] if labels else "unclassified"),
        "partner_tag": bool(SPONSOR_SHORT_RE.search(title + " " + desc[:300])),
        "listicle": listicle, "income_claims_title": inc_title, "income_periods": periods,
        "n_queries_hit": len({h[0] for h in hits.get(vid, [])}),
        **{"desc_" + k: b for k, b in sell.items()},
    })

json.dump(rows, open(os.path.join(DATA, "videos_classified.json"), "w"), indent=0)
with open(os.path.join(DATA, "videos_classified.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    for r in rows:
        r2 = dict(r); r2["methods"] = "|".join(r["methods"]); r2["income_claims_title"] = " | ".join(r["income_claims_title"]); r2["income_periods"] = "|".join(r["income_periods"])
        w.writerow(r2)
print("wrote", len(rows))
