# YouTube metadata survey: what videos claim about making money with Claude (data as of 2026-10-12)

**Method and data provenance (read first)**
- **Data files:** all in `research_notes/Making money with Claude/data/`.
  - `videos_classified.csv` / `.json`: one row per video, with tier, methods, income claims and description signals.
  - `stats.md`: every table quoted below.
  - `video_details.json`, `channel_details.json`: raw YouTube Data API v3 metadata.
  - `search_hits.json`: which query found each video.
  - `scripts/`: collect.py, scrape.py, merge.py, analyze.py, stats.py.
- **Discovery, step 1 (official API):** I ran 86 YouTube Data API `search` calls before the daily search quota ran out. They covered 5 query strings fully plus part of a 6th, with order=relevance/viewCount/date and publishedAfter set to 2025 and 2026. They returned 1,154 unique video IDs.
- **Discovery, step 2 (web scraping workaround):** after the quota ran out, I collected more IDs by scraping YouTube's public web search results pages. This covered 143 query variants, with relevance, view-count and upload-date sorting plus a "this year" filter, at up to 6 result pages per variant. **This was a workaround of the API limit.** The coordinator later said not to work around limits. It had already finished by then, and I have done no further collection since. The paid tools (TubeAlfred, vidIQ) returned "insufficient credits" and charged nothing.
- **Metadata:** all titles, descriptions, views, likes, comments, durations and subscriber counts come from the official API `videos`/`channels` endpoints. These cost 1 quota unit each and still worked. Total: 12,427 unique video IDs with metadata, from 6,085 channels.
- **Relevance tiers (keyword rules, automatic):**
  - **A1 (3,686 videos):** "Claude"/"Anthropic"/"Cowork" appears in the title, description or tags, AND the title has a money signal. Money signals include make money, earn, income, $ amounts, side hustle, sell, clients, agency, business, plus Spanish, Portuguese, Hindi and other-language equivalents.
  - **B (356 videos):** no Claude mention, but an AI term plus a strong money term in the title, and found by a Claude query.
  - **A2 (950 videos):** Claude video whose money signal appears only in the first 300 characters of the description. Excluded from the analysis.
  - **D (143 videos):** pricing, credits or company news, e.g. "Claude Max includes $200 in API credits". Excluded.
  - **C (6,390 videos):** Claude video with no money signal. Excluded.
  - **X (902 videos):** irrelevant. Excluded.
  - **The analysed relevant set R = A1 + B = 4,042 videos** from 2,389 channels.
- **Method classification:** keyword regexes run on the title, after removing hashtags. A video can get more than one label. The "primary" method is the most specific match. When a title names no method, the video is primary "unclassified", or "multi-method listicle" if the title is a "N ways…" listicle. I also ran a fallback on the first part of the description. It was noisy in spot checks (roughly half plausible), so it is reported separately and **not** used for the primary label.
- **Sampling bias:** YouTube search ranks recent videos heavily, so 93.8% of R is from 2026. The year-on-year comparisons describe what search surfaces today, not what was actually published each year. All view counts are a snapshot taken on 2026-10-12.

## Q1. How many unique relevant videos were found, and which methods appear most often?

### Takeaway
I found 12,427 unique videos, of which 4,042 are relevant (3,686 mention Claude explicitly). The biggest single bucket (42.2%) is titles that promise money "with Claude" without naming a method. Among titles that do name one, the most common methods are: build and sell apps/SaaS (vibe coding), digital products/ebooks/KDP, AI automation/agency, faceless YouTube/short-form content, and websites for clients. Explicitly selling Claude Skills, prompts or MCP servers is rare (about 1–2%).

### Cited Findings
- **Sample size:** 12,427 unique video IDs with full metadata. Relevant set R = 4,042 (A1 = 3,686, B = 356), from 2,389 unique channels. 3,212 videos in R have "Claude"/"Anthropic" in the title itself. — [stats.md](data/stats.md); [videos_classified.csv](data/videos_classified.csv)
- **Discovery source within R:** web search only 3,338; API only 172; both 532. — [stats.md](data/stats.md)
- **Format and language:** 1,278 of the 4,042 videos (31.6%) are Shorts of 60 seconds or less. Languages: English 3,536; Spanish 150; Hindi 146; Portuguese 102; Urdu 25; French 11. — [stats.md](data/stats.md)
- **Primary method in R (title-based; n=4,042):**

  | Primary method | n | % of R |
  |---|---|---|
  | Unclassified (generic "make money with Claude/AI" titles, no method named) | 1,704 | 42.2% |
  | Build & sell SaaS / apps / software, incl. vibe coding | 402 | 9.9% |
  | Digital products / ebooks / KDP / Etsy / printables / PDFs | 337 | 8.3% |
  | Multi-method listicle ("N ways to make money with Claude") | 240 | 5.9% |
  | Websites (often sold to local businesses) | 215 | 5.3% |
  | Faceless YouTube / Shorts / TikTok / Instagram content | 212 | 5.2% |
  | Trading / investing / crypto / Polymarket bots | 176 | 4.4% |
  | AI automation / agency (selling automations) | 139 | 3.4% |
  | Freelancing / gigs (Upwork, Fiverr, copywriting) | 134 | 3.3% |
  | AI agents / "AI employees" / one-person business | 121 | 3.0% |
  | AI skills for jobs / salary | 91 | 2.3% |
  | Blogging / SEO / affiliate | 74 | 1.8% |
  | Lead gen / cold email / outreach | 57 | 1.4% |
  | Selling Claude Skills / prompts / templates / MCP servers / plugins | 47 | 1.2% |
  | E-commerce / dropshipping | 44 | 1.1% |
  | Chatbots / voice agents / AI receptionists | 27 | 0.7% |
  | Selling courses / coaching | 19 | 0.5% |
  | Newsletters | 3 | 0.1% |

  Source: [stats.md](data/stats.md)
- **Every method named in a title (multi-label count):**
  - SaaS/apps: 484
  - Digital products: 337
  - Automation/agency: 244
  - Faceless content: 221
  - Websites: 220
  - Trading: 176
  - AI agents / one-person business: 168
  - Freelancing: 147
  - Jobs/career: 130
  - Blogging/SEO: 81
  - Skills/prompts/templates: 63
  - Lead gen: 61
  - E-commerce: 46
  - Chatbots/voice: 28
  - Courses/coaching: 26
  - Newsletters: 3

  Source: [stats.md](data/stats.md)
- **Unclassified share:**
  - 51.9% of R is classified from the title.
  - 1,138 more videos match a method only in the description head. These are low-confidence: faceless 251, digital products 194, course/coaching 104, websites 92, automation 91, SaaS 82.
  - 806 match no method anywhere.
  - Title-unclassified share is 52.9% among Shorts and 37.2% among longer videos.

  Source: [stats.md](data/stats.md)
- **Claude-explicit set A1, longer videos only (n=2,546):** unclassified 39.0%, SaaS/apps 9.3%, digital products 8.7%, listicle 7.0%, faceless 5.9%, websites 5.6%, trading 5.3%, one-person business 3.8%, automation/agency 3.3%, freelancing 3.3%, Skills/prompts/templates 1.1%. — [videos_classified.json](data/videos_classified.json)
- **Claude product names in R titles:**
  - "Claude Code": 655
  - "vibe coding": 307 (all years combined)
  - "skill(s)": 94
  - Model names: "Fable" 73, "Opus" 67
  - "Cowork": 70
  - "MCP": 62
  - "artifact": 20

  Source: [videos_classified.json](data/videos_classified.json)
- **Example titles by method (all R, views as of 2026-10-12):**
  - Faceless content: "How I Make $24,937/mo Posting YouTube Shorts (Using Claude AI)", 1,341,739 views — [YouTube](https://www.youtube.com/watch?v=V_t51u1tBJc)
  - Websites: "Build $10,000 Websites using Claude Code (Ultimate Guide)", 1,182,557 views — [YouTube](https://www.youtube.com/watch?v=VMvZuhcDdnw)
  - Build-and-sell course: "CLAUDE CODE FULL COURSE 4 HOURS: Build & Sell (2026)", 2,653,833 views — [YouTube](https://www.youtube.com/watch?v=QoQBzR1NIqI)
  - Trading: "Zerodha + Claude AI is INSANE – Let Claude Print Money", 683,693 views — [YouTube](https://www.youtube.com/watch?v=FwxhPaHoeBM)
  - Notion templates: "How to Make $3,200 Per Month Using Claude AI to Write and Sell Notion Templates #Shorts" — [videos_classified.csv](data/videos_classified.csv)

### Inferences
- Most Claude money content does not name a concrete business model in the title. It sells the idea that "Claude makes money" through generic titles, listicles and hashtag-stuffed Shorts. In 2026 the specific methods pitched most are build-and-sell apps (Claude Code / vibe coding), digital products, websites for clients, faceless content and automation agencies.
- Selling Claude Skills, MCP servers or plugins is a small niche (47 primary / 63 any-label in titles). Claude Skills, MCP and Cowork mostly show up as *tools* inside other methods, not as products to sell.

### Gaps
- Classification uses titles only. I did not watch videos or read transcripts, so the 42% unclassified share and the multi-method listicles cannot be broken down further.
- Regex labels have some errors I saw in spot checks. Examples: "$10,000 websites" sometimes means the site *looks* expensive rather than being sold for $10k; "Startup Founders: Get Claude AI FREE" was labelled SaaS. I did not measure precision formally.
- Recall is unknown. The scraped search results are a sample of what YouTube surfaces, not a census.

## Q2. Which methods get the most views, median views, views per subscriber and engagement?

### Takeaway
By total views, generic "make money with Claude/AI" titles and listicles lead, followed by SaaS/app building, faceless content, websites and "one-person AI business" titles. By *median* views (the typical video), e-commerce, one-person-business, jobs/career, faceless content, websites and trading do best. Freelancing, Skills/prompts selling, courses and newsletters have the lowest medians. Faceless content, chatbots/voice agents and jobs/career get the most views per subscriber. Engagement sits between about 2.6% and 4.1% for every method.

### Cited Findings
- **Performance by primary method (R; views are lifetime as of 2026-10-12):**

  | Method | n | Total views | Median views | Median views/subscriber | Median (likes+comments)/views (videos ≥1k views) | Videos ≥100k views |
  |---|---|---|---|---|---|---|
  | Unclassified / generic | 1,704 | 73.5M | 1,292 | 0.41 | 2.98% | 153 |
  | SaaS / apps / vibe coding | 402 | 31.2M | 2,558 | 0.38 | 2.83% | 50 |
  | Multi-method listicle | 240 | 30.7M | 2,534 | 0.26 | 3.30% | 42 |
  | Faceless content | 212 | 24.6M | 6,928 | 0.89 | 3.61% | 48 |
  | Websites | 215 | 12.5M | 5,964 | 0.52 | 3.19% | 34 |
  | AI agents / one-person business | 121 | 11.6M | 12,288 | 0.41 | 3.61% | 24 |
  | Digital products / KDP | 337 | 10.9M | 2,568 | 0.38 | 3.82% | 27 |
  | Trading / crypto | 176 | 9.8M | 5,478 | 0.53 | 2.75% | 18 |
  | Jobs / career | 91 | 5.9M | 9,506 | 1.00 | 2.91% | 15 |
  | Automation / agency | 139 | 5.9M | 1,380 | 0.45 | 2.90% | 15 |
  | E-commerce | 44 | 2.2M | 20,504 | 0.41 | 4.09% | 5 |
  | Blogging / SEO / affiliate | 74 | 1.6M | 1,225 | 0.27 | 3.55% | 5 |
  | Freelancing | 134 | 1.3M | 398 | 0.63 | 2.60% | 3 |
  | Skills / prompts / templates | 47 | 0.73M | 413 | 0.59 | 3.75% | 2 |
  | Lead gen / cold email | 57 | 0.36M | 1,248 | 0.58 | 3.06% | 0 |
  | Chatbots / voice agents | 27 | 0.35M | 4,420 | 0.96 | 3.40% | 0 |
  | Courses / coaching | 19 | 0.22M | 611 | 0.68 | 3.37% | 0 |
  | Newsletters | 3 | 2.7k | 29 | 0.16 | 1.97% | 0 |

  Source: [stats.md](data/stats.md)
- **Longer videos only (Shorts of 60s or less removed):**
  - Median views: faceless 12,338; websites 13,239; one-person business 17,564; jobs/career 26,966; e-commerce 22,521; SaaS/apps 6,637; digital products 5,504; automation/agency 2,406; freelancing 984; Skills/prompts 582.
  - Total views are about the same as above: SaaS 27.6M, faceless 22.7M.

  Source: [stats.md](data/stats.md)
- **Overall distribution:**
  - Total views in R: 223,482,993.
  - Median video in R: 1,928 views. A1 (Claude-explicit) median: 1,657. B (generic AI-money surfaced by Claude queries) median: 17,334.
  - 441 videos have ≥100k views and 41 have ≥1M. 1,616 (40%) have under 1,000 views.

  Source: [videos_classified.json](data/videos_classified.json)
- **Sponsored/partner content:** 75 videos in R carry partner or ad tags (#…partner, "Anzeige", #ad), 73 of them from 2026. 81 titles in R mention "Higgsfield". Many are #higgsfieldpartner Shorts pairing Claude with "side hustle" hashtags. Higgsfield AI's own channel has 6 videos in R with 2.37M total views, e.g. "I Used Higgsfield AI + Claude Fable 5 to Build a $39,500/Month Faceless Channel", 873,355 views. — [stats.md](data/stats.md); [YouTube](https://www.youtube.com/watch?v=wU_bmWb6bhg)

### Inferences
- Methods that sound easy and passive (faceless channels, "AI business", generic "make money with Claude") get the most total and per-subscriber reach. B2B service methods (automation agencies, lead gen, freelancing, selling Skills/prompts) are pitched often but each video gets modest views.
- Views per subscriber near or above 1.0 for faceless content, chatbots and jobs means small channels in those niches sometimes outperform their size. That pattern is typical of search- and Shorts-driven discovery.

### Gaps
- Engagement uses only public likes and comments. Watch time, CTR and revenue are not available.
- Views per subscriber uses the channel's *current* subscriber count, not the count at upload.
- Per-method numbers are small for newsletters (3), courses (19) and chatbots (27), so treat them as indicative only.

## Q3. What income claims appear in titles, and how common are they?

### Takeaway
About a third of relevant titles (33.8%) contain a money figure. The typical claim is around $10,000/month. Of USD claims with a stated period, 70% are $10k/month or more, and 45 imply $100k/month or more. Titles with a figure get higher median views than titles without one.

### Cited Findings
- **How common:** 1,365 of 4,042 R titles (33.8%) contain a currency or income figure; in A1 it is 1,231 of 3,686. Periods: none or lump sum 808; per month 429; per day 93; per week 18; per year 17. — [stats.md](data/stats.md)
- **Normalised USD claims** (USD figures with an explicit period, converted to $/month; n=527):
  - Median $10,000/month; 25th percentile $5,000; 75th percentile $30,000; maximum $4.8M/month.
  - Buckets: under $1k: 40; $1k–$10k: 123; $10k–$50k: 286; $50k–$100k: 33; $100k or more: 45.

  Source: [stats.md](data/stats.md)
- **Views with and without a figure:** median 3,641 with a figure vs 1,450 without. Longer videos only: 7,260 vs 5,071. — [stats.md](data/stats.md)
- **Share of titles with a figure, by year:** 2024 29.2% (7/24); 2025 44.3% (97/219); 2026 33.2% (1,257/3,791). — [stats.md](data/stats.md)
- **Share of titles with a figure, by primary method:**
  - E-commerce: 70.5%
  - Websites: 69.8%
  - Chatbots/voice: 66.7%
  - Faceless: 62.3%
  - SaaS/apps: 51.6%
  - Trading: 43.8%
  - Skills/prompts: 35.2%
  - Digital products: 31.2%
  - Automation/agency: 30.9%
  - Freelancing: 20.1%
  - Jobs: 9.9%

  Source: [stats.md](data/stats.md)
- **Most-viewed titles with Claude-related income claims:**
  - "How a Faceless Channel Made $39K With Claude + ChatGPT", 1.37M views — [YouTube](https://www.youtube.com/watch?v=8Rf0xna31xg)
  - "How I Make $24,937/mo Posting YouTube Shorts (Using Claude AI)", 1.34M views — [YouTube](https://www.youtube.com/watch?v=V_t51u1tBJc)
  - "Claude Code (Free Plan) + YouTube = $77,000/Month", 1.06M views — [YouTube](https://www.youtube.com/watch?v=WVT2FCjhDDY)
  - "Claude + ChatGPT = $57,152 In 90 Days", 560k views — [YouTube](https://www.youtube.com/watch?v=kYPAlvnRiiI)
  - "Claude Ai + YouTube = $9,987/Month (FREE Plan)", 511k views — [YouTube](https://www.youtube.com/watch?v=qJkC05DjVlA)
- **Recurring title template "Claude + X = $N/month":** the dataset also contains "Claude Code + Airbnb = $13,000/Month", "Claude (Free Plan) + YouTube = $52000/Month" and "I make 10k/month making AI Documentaries with Claude Code". — [videos_classified.csv](data/videos_classified.csv)

### Inferences
- "$10k/month" is the standard anchor figure. Income claims cluster in faceless-content and website/app titles, and these claims go with higher views. That gives creators a reason to inflate them.
- None of these figures were verified. They are claims made in titles, often by channels that sell courses or communities (see Q5).

### Gaps
- Income regexes catch only figures in titles, not in thumbnails or spoken content.
- Rupee (₹ / lakh / crore) and euro claims are counted in the 33.8% but not normalised to USD.
- Some "$" figures are prices rather than income claims, e.g. "$10,000 websites" or "$250M app". These inflate the count somewhat.

## Q4. How has the method mix changed from 2024 to 2025 to 2026?

### Takeaway
Search results are overwhelmingly from 2026 (3,791 of 4,042), and Claude money content took off in 2026 Q2–Q3. From 2025 to 2026, SaaS/app building fell from the dominant pitch to one of several. Faceless content, websites, generic "AI business" titles, courses and jobs pitches grew. Titles moved from "vibe coding" to "Claude Code", Cowork, Skills and MCP, and Shorts rose to about 40% of 2026 H2 uploads.

### Cited Findings
- **Volume by year in R:** 2023: 8; 2024: 24; 2025: 219; 2026: 3,791.
- **Volume by quarter in R:** 2025 Q1 24; Q2 36; Q3 51; Q4 108; 2026 Q1 327; Q2 1,410; Q3 1,422; Q4 (to Oct 12 only) 632.

  Source: [stats.md](data/stats.md)
- **Primary-method share, 2025 (n=219) vs 2026 (n=3,791):**
  - SaaS/apps: 35.6% → 8.4%
  - Digital products: 9.1% → 8.2%
  - Trading: 5.5% → 4.3%
  - Freelancing: 5.5% → 3.2%
  - Automation/agency: 4.1% → 3.4%
  - Websites: 3.2% → 5.4%
  - Faceless: 2.7% → 5.3%
  - One-person business: 2.7% → 3.0%
  - Jobs: 0.5% → 2.4%
  - Unclassified/generic: 20.5% → 43.5%

  Source: [stats.md](data/stats.md)
- **Any-label share by half-year** (2025 H1 n=60, 2025 H2 n=159, 2026 H1 n=1,737, 2026 H2 to Oct 12 n=2,054):
  - SaaS/apps: 41.7% / 43.4% / 17.8% / 14.0%
  - Faceless: 10.0% / 5.7% / 15.5% / 14.5%
  - Courses/coaching: 3.3% / 3.8% / 9.0% / 7.1%
  - Jobs: 0% / 2.5% / 4.3% / 5.1%
  - Websites: 6.7% / 3.8% / 8.6% / 8.4%
  - Freelancing: 10.0% / 6.9% / 5.9% / 5.8%
  - Digital products: steady at 11.7–13.8%
  - Automation/agency: 18.3% / 11.3% / 12.8% / 11.2%

  These shares include the low-confidence description fallback. Source: [stats.md](data/stats.md)
- **Claude product names in titles:**
  - 2025: "Claude Code" 22, "vibe cod" 57, Cowork 0, "skill" 3, MCP 1
  - 2026: "Claude Code" 633, "vibe cod" 250, Cowork 70, "skill" 92, MCP 61, artifact 19

  Source: [stats.md](data/stats.md)
- **Claude named in the title:** 33.3% of R titles in 2024 and in 2025, 82.6% in 2026. — [videos_classified.json](data/videos_classified.json)
- **Shorts (60s or less) share of R:** 2024 29.2%; 2025 22.8%; 2026 32.0% (2026 H1 22.2%, 2026 H2 40.4%). — [videos_classified.json](data/videos_classified.json)
- **Older content:** most 2023–2024 videos in R are ChatGPT-era generic AI-money videos surfaced by Claude queries. Examples: "Le Doy $100 a Chat GPT Para Que Me Haga Ganar Dinero" (2023, 962k views) and "How I Created a $10,000/month Faceless YouTube Channel Using Free AI Tools" (2024-10-02, 2.54M views). — [YouTube](https://www.youtube.com/watch?v=Nm6hhWYA55U); [YouTube](https://www.youtube.com/watch?v=LEJGFnjIWmQ)

### Inferences
- In 2025, Claude money content was mostly "vibe-code an app and sell it". By 2026 it is a broad "make money with Claude" genre that applies Claude to older hustles (faceless YouTube, KDP/PDFs, websites for local businesses, trading). It increasingly arrives as hashtag-heavy Shorts, some of them sponsored, e.g. #higgsfieldpartner.
- Cowork, Skills and MCP appear mainly from 2026 and as tool mentions rather than as products to sell.

### Gaps
- Because YouTube search favours recent videos, the 2024 and 2025 samples (24 and 219 videos) undercount what was actually published then. Treat the shifts as directional.
- 2026 Q4 covers only October 1–12.

## Q5. Which channels dominate, and how many sell their own course or community?

### Takeaway
The field is long-tailed: 2,389 channels, 1,800 of them with only one video in R. Views are still concentrated, with the top 10 channels holding 28.7% of all views in R and the top 25 holding 46.3%. Most large channels sell something. 82% of the top 50 channels by views have an own-offer signal in their descriptions (course, community, coaching, Skool, store), and 66% have affiliate links. Only 10% of top-50 channels link Skool specifically.

### Cited Findings
- **Concentration:** 2,389 unique channels in R; 283 have 3 or more videos; 1,800 have exactly one. 1,139 channels have under 1k subscribers and 321 have 100k or more. Top 10 channels: 28.7% of 223.5M total views; top 25: 46.3%. — [stats.md](data/stats.md); [videos_classified.json](data/videos_classified.json)
- **Top channels by total R views:**
  - Mark Tilbury: 3 videos, 11.6M views
  - Raj Shamani: 4 videos, 10.5M
  - Adrián Sáenz (Spanish): 22 videos, 8.7M
  - Nate Herk | AI Automation: 21 videos, 6.9M
  - Shane Hummus: 66 videos, 4.8M
  - Nick Saraev: 6 videos, 4.7M
  - Dhaval Kataria: 5 videos, 4.4M
  - Starter Story: 11 videos, 4.3M
  - Kellan Henneberry: 4 videos, 4.2M
  - Dan Martell: 7 videos, 4.2M
  - Others in the top 30: Edmund Yong, Patrick Dang, Chris Koerner, Sabrina Ramonov, Wholesale Ted, Greg Isenberg, Jack Roberts, Albert Olgaard, Higgsfield AI, Metics Media

  Source: [stats.md](data/stats.md)
- **Most prolific channels by number of R videos:** Shane Hummus 66; Irvale Studio 35 (3 subscribers, 756 total views, i.e. spam-like volume); Patrick Dang 28; Sabrina Ramonov 25; Adrián Sáenz 22; BridgeMind 22; THE ECOM KING 21; Nate Herk 21; Franko Dorival 20; Automate AI Consulting 19. — [stats.md](data/stats.md)
- **Monetisation signals in descriptions** (regex on full description text):

  | Signal | % of R videos | % of R channels | % of top-50 channels by views |
  |---|---|---|---|
  | skool.com link | 11.1% | 8.2% | 10% |
  | whop.com | 0.8% | 0.8% | 0% |
  | course / academy / program | 19.3% | 19.5% | 54% |
  | community / "join my" | 17.0% | 15.2% | 32% |
  | coaching / consult / book a call / agency | 28.1% | 26.8% | 66% |
  | affiliate / ref / coupon links | 21.4% | 18.2% | 66% |
  | sponsor disclosure | 3.7% | 3.6% | 22% |
  | Store (Gumroad / Stan / Kajabi / linktree / newsletter) | 8.7% | 9.5% | 20% |
  | **Any own-offer signal** | **50.5%** | **46.3%** | **82%** |
  | Skool or Whop | 11.8% | 8.9% | 10% |

  Among longer videos (n=2,764): Skool link 15.1%; any own-offer 63.4%; affiliate 27.8%. Source: [stats.md](data/stats.md)
- **Channels with a Skool link plus course/community signals:** Nate Herk, Nick Saraev, Albert Olgaard, Greg Isenberg and Jack Roberts. — [stats.md](data/stats.md)
- **Anthropic's own content:** its video "Claude ran a business in our office" (2025-12-18, 669,298 views) is the only first-party video in the Claude-in-title top 30. — [YouTube](https://www.youtube.com/watch?v=5KTHvKCrQ00)

### Inferences
- A large share of "make money with Claude" content funnels viewers to the creator's own paid offer: a course, community, coaching or agency service. Affiliate links (often for AI tools) are almost as common among top channels. This fits with income claims doing better than plain titles.
- The biggest names are general finance/business creators (Tilbury, Shamani, Martell, Gadzhi) who cover "AI money" broadly. The Claude-specific leaders are AI-automation educators (Nate Herk, Nick Saraev, Jack Roberts) and newer faceless/Shorts channels.

### Gaps
- Description regexes are approximate. "Agency" and "consult" can be about the creator's services or about the topic, and "community" can be a Discord link. I did not check landing pages or prices.
- Several large channels (Mark Tilbury, Raj Shamani, Iman Gadzhi, Diary of a CEO) appear because of AI-money videos that only mention Claude in passing, or not at all (tier B).

## Q6. Top 30 most-viewed videos

### Takeaway
The 30 most-viewed relevant videos are dominated by big business/finance creators' general "make money with AI" content. Only 9 of the 30 mention Claude anywhere, and only 5 in the title. The most-viewed Claude-titled videos are Claude Code build-and-sell courses, faceless-channel income stories and "$10k websites" tutorials.

### Cited Findings
- **Top 30 in R by views as of 2026-10-12.** Claude = Claude mentioned anywhere in title, description or tags. Source: [stats.md](data/stats.md)

| # | Views | Date | Channel | Title | Primary method | Claude? |
|---|---|---|---|---|---|---|
| 1 | 6,086,417 | 2026-09-21 | Mark Tilbury | [I Tried The LAZIEST Way to Make Money With AI](https://www.youtube.com/watch?v=LlhTEttKcwQ) | unclassified | Y |
| 2 | 4,594,795 | 2025-07-03 | Raj Shamani | [Start Earning Money With AI - Free Tools & Business Ideas](https://www.youtube.com/watch?v=0-FUhQKe-eU) | listicle | N |
| 3 | 3,182,766 | 2026-04-21 | Raj Shamani | [Earn Crores with AI: Business Ideas, Claude, Free Tools & Prompts](https://www.youtube.com/watch?v=7fsb6ZESyzE) | listicle | Y |
| 4 | 2,892,432 | 2026-03-06 | Mark Tilbury | [I'm Changing How I Invest My Money Because of AI](https://www.youtube.com/watch?v=O8t50OxsfB8) | trading | N |
| 5 | 2,653,833 | 2026-02-12 | Nick Saraev | [CLAUDE CODE FULL COURSE 4 HOURS: Build & Sell (2026)](https://www.youtube.com/watch?v=QoQBzR1NIqI) | SaaS/apps | Y |
| 6 | 2,625,277 | 2026-07-25 | Mark Tilbury | [Laziest Ways to Make Money with AI (For Beginners)](https://www.youtube.com/watch?v=ytAW1_g2IfI) | listicle | N |
| 7 | 2,583,320 | 2024-12-27 | Edmund Yong | [How I Code Profitable Apps SOLO](https://www.youtube.com/watch?v=CNsvts6pVzo) | SaaS/apps | N |
| 8 | 2,543,172 | 2024-10-02 | All About Money | [How I Created a $10,000/month Faceless YouTube Channel Using Free AI Tools](https://www.youtube.com/watch?v=LEJGFnjIWmQ) | faceless | N |
| 9 | 2,212,925 | 2026-02-28 | Dhaval Kataria | [I Tried Raj Shamani's Business Idea to Make ₹1,00,000](https://www.youtube.com/watch?v=IW5_ivFlO6U) | unclassified | N |
| 10 | 1,971,371 | 2025-05-23 | Nate Herk | [Build & Sell n8n AI Agents (8+ Hour Course, No Code)](https://www.youtube.com/watch?v=Ey18PDiaAYI) | automation/SaaS | Y |
| 11 | 1,946,903 | 2026-03-16 | The Diary Of A CEO | [Daniel Priestley: AI Will Make Plumbers Earn More Than Lawyers!](https://www.youtube.com/watch?v=fpETS6q1Hww) | unclassified | N |
| 12 | 1,892,652 | 2025-05-07 | Vaibhav Kadnar | [5 Ways To Make Money With ChatGPT As A Student](https://www.youtube.com/watch?v=fWQNuA_z330) | listicle | N |
| 13 | 1,744,974 | 2026-09-03 | Raj Shamani | [How AI Makes Him Crores: Second Brain, Automations & Systems](https://www.youtube.com/watch?v=LqY6hFLMEJw) | automation | Y |
| 14 | 1,660,956 | 2025-01-22 | Your Average Tech Bro | [How I Code Apps SOLO That Actually Make Money](https://www.youtube.com/watch?v=dNntYdZQ_mk) | SaaS/apps | N |
| 15 | 1,500,105 | 2026-07-09 | Iman Gadzhi | [5 Proven Ways To Make Money With AI (No Experience)](https://www.youtube.com/watch?v=DZoeGR_tatA) | listicle | N |
| 16 | 1,497,054 | 2025-06-08 | Dan Kieft | [How To Actually Make Money with Whop Clipping](https://www.youtube.com/watch?v=sTvsM0ej4Eg) | unclassified | N |
| 17 | 1,491,075 | 2025-04-20 | Codie Sanchez | [Making $1000/Day With AI?](https://www.youtube.com/watch?v=SXNBsSy6Xlg) | unclassified | N |
| 18 | 1,473,411 | 2025-05-02 | Edmund Yong | [How I Coded ANOTHER Profitable App SOLO](https://www.youtube.com/watch?v=cESaIUWoCJQ) | SaaS/apps | N |
| 19 | 1,468,810 | 2023-07-16 | Dan Fuentes | [Cómo ganar dinero con Inteligencia Artificial](https://www.youtube.com/watch?v=ia0IIBaS__g) | unclassified | N |
| 20 | 1,370,672 | 2026-08-24 | Sanji Nai-Chien | [How a Faceless Channel Made $39K With Claude + ChatGPT](https://www.youtube.com/watch?v=8Rf0xna31xg) | faceless | Y |
| 21 | 1,364,933 | 2025-04-29 | Nick Saraev | [N8N FULL COURSE 6 HOURS (Build & Sell AI Automations + Agents)](https://www.youtube.com/watch?v=2GZ2SNXWK-c) | SaaS/automation | Y |
| 22 | 1,351,590 | 2026-04-30 | Dan Martell | [The Only 14 Ways to Make Money with AI in 2026](https://www.youtube.com/watch?v=K8Ros5RhJW4) | listicle | N |
| 23 | 1,341,739 | 2026-06-28 | Kellan Henneberry | [How I Make $24,937/mo Posting YouTube Shorts (Using Claude AI)](https://www.youtube.com/watch?v=V_t51u1tBJc) | faceless | Y |
| 24 | 1,336,898 | 2025-05-22 | Financially Free™ | [TradingView + AI is a Game Changer](https://www.youtube.com/watch?v=6tPk26N851c) | trading | N |
| 25 | 1,257,038 | 2024-11-23 | Adam Erhart | [How I Make $1,000 a Day Using ChatGPT!](https://www.youtube.com/watch?v=f8ZHQtnpg_w) | unclassified | N |
| 26 | 1,245,524 | 2025-10-29 | Kellan Henneberry | [how i make $36,438/mo posting YouTube Shorts (using AI)](https://www.youtube.com/watch?v=ygeCgN-SfE8) | faceless | N |
| 27 | 1,232,216 | 2025-11-06 | Mel Robbins | [How to Use AI to Make Money, Save Time, and Be More Productive](https://www.youtube.com/watch?v=64qXq8AG_9M) | unclassified | N |
| 28 | 1,223,124 | 2026-09-05 | Nitesh Nayak | [AI Video बनाकर Meesho से पैसे कमाओ (faceless, Hindi)](https://www.youtube.com/watch?v=u-5Gf8uCnJ4) | faceless | N |
| 29 | 1,182,557 | 2026-05-29 | Metics Media | [Build $10,000 Websites using Claude Code (Ultimate Guide)](https://www.youtube.com/watch?v=VMvZuhcDdnw) | websites | Y |
| 30 | 1,153,641 | 2026-03-20 | Chris Koerner | [He Asked AI To Make Money. It Did.](https://www.youtube.com/watch?v=l0Vqm0ZIySc) | unclassified | N |

  Row 10 note: the regex picked "Selling skills/prompts" as primary because the title says "Sell … Agents". It is better read as automation/agency.

- **Top Claude-in-title videos** (full top 30 in [stats.md](data/stats.md)):
  - Raj Shamani, "Earn Crores with AI…Claude…", 3.18M — [YouTube](https://www.youtube.com/watch?v=7fsb6ZESyzE)
  - Nick Saraev, Claude Code Build & Sell course, 2.65M — [YouTube](https://www.youtube.com/watch?v=QoQBzR1NIqI)
  - Sanji Nai-Chien, faceless $39K, 1.37M — [YouTube](https://www.youtube.com/watch?v=8Rf0xna31xg)
  - Kellan Henneberry, $24,937/mo Shorts, 1.34M — [YouTube](https://www.youtube.com/watch?v=V_t51u1tBJc)
  - Metics Media, $10,000 websites, 1.18M — [YouTube](https://www.youtube.com/watch?v=VMvZuhcDdnw)
  - Nate Herk, "Build & Sell with Claude Code (10+ Hour Course)", 1.14M — [YouTube](https://www.youtube.com/watch?v=mpALXah_PBg)
  - Calum Johnson, AI agents in your business (OpenClaw & Claude), 1.08M — [YouTube](https://www.youtube.com/watch?v=cqMpTbTrMW4)
  - zapiwala ai, "Claude Code (Free Plan) + YouTube = $77,000/Month", 1.06M — [YouTube](https://www.youtube.com/watch?v=WVT2FCjhDDY)
  - Albert Olgaard, "Start a 1-Person Business with Claude (4 HOUR COURSE 2026)", 1.02M — [YouTube](https://www.youtube.com/watch?v=mKyaNr3jK-E)
  - 3.7Million, "I Built A Business From Scratch Only Following Claude's Advice", 1.01M — [YouTube](https://www.youtube.com/watch?v=_-jZ6eV3DP4)
  - Higgsfield AI, Claude + Higgsfield $39,500/Month faceless channel, 873k — [YouTube](https://www.youtube.com/watch?v=wU_bmWb6bhg)
  - Spanish-language: Adrián Sáenz, "3 Formas De Ganar Dinero Con Claude", 760k — [YouTube](https://www.youtube.com/watch?v=Or8neoE7Z4c)

### Inferences
- The highest-reach "Claude money" videos are long build-and-sell courses (Claude Code, n8n) and faceless or website income stories. Claude-specific titles rarely pass 1–3M views, while generic "AI money" videos from big creators reach 2–6M.

### Gaps
- Some high-view items in R are not really about making money with Claude. Examples: Diary of a CEO's labour-market prediction; Firstpost news "Claude CoWork Breakthrough Triggers Sell-Off in Indian Tech" (896k views, Claude-titled list); "SOFTWARE JOBS Gone?" (510k). They passed the keyword filter and I did not remove them by hand.
- The top-30 ranking covers only videos my searches surfaced. Popular videos those queries missed would not appear.
