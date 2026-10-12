# YouTube Transcript Analysis: Making Money with Claude (October 2026)

**Status: incomplete. Transcripts analyzed: 1 of the 150–200+ planned.** I stopped collecting on the coordinator's instruction after YouTube began blocking requests. These notes give the transcript findings from n=1, plus clearly labeled metadata and description signals for 265 candidate videos. Nothing below about methods, frequencies or case studies is drawn from a transcript sample of any size. Do not cite these notes as a transcript survey.

**Collection log (for the report writer):**
- TubeAlfred transcript tool: refused, 0 credits (402 insufficient_credits).
- vidIQ transcript tool: refused, "Not enough credits".
- Subscribr: monthly limit of 25 transcripts already used.
- YouTube Data API `search`: daily "Search Queries per day" quota exhausted. A parallel worker's `collect.py` hit the limit. `videos.list` still worked.
- Direct caption fetch from this machine (youtube-transcript-api, yt-dlp default clients) was refused with an IP block / "Sign in to confirm you're not a bot". One transcript (AP-fOOmm02g) downloaded before the block covered every route. Further attempts were blocked, and collection was halted per coordinator instruction.
- Third-party transcript sites tested (tactiq, kome, notegpt, youtubetranscript.com, youtubetotranscript.com, Invidious/Piped instances) were all unavailable, blocked or required login.
- Candidate discovery did work: yt-dlp search pages for 40 queries in 3 sort modes, plus the cached API searches. The pool was 2,778 unique videos. After filtering (Claude-related, money-related, ≥3 min, published 2025 or later, English), 1,359 remained. I selected 265 for transcript pulls: 140 top by views, 70 recent high-view (Jun–Oct 2026), and 55 mid-size recent. Their metadata is in `data/candidate_videos_description_signals.csv`. Published range is 2025-05-14 to 2026-10-11; median views are 87,168.

Data files:
- `data/transcripts_catalog.json`: 1 structured record (schema: methods, steps, tools, customer, price, claimed income, attribution, manual-work, proof level, funnel, caveats, failure modes, quotes).
- `data/candidate_videos_description_signals.csv`: 265 candidates with title, channel, views, date and URL. It also has regex flags on the descriptions only (Skool, Whop, course/community wording, affiliate markers, sponsors, book-a-call links, $ figures in the title).

## What are the distinct methods, and how frequently does each appear across transcripts?

### Takeaway
I cannot measure method frequency across transcripts, because only 1 transcript was analyzed. Titles of the 265 candidates suggest the main method clusters, but titles are not transcript evidence.

### Cited Findings
- The one transcript analyzed describes a single method: productized LinkedIn ghostwriting for SaaS founders. Claude prompts are used to pick an offer and plan, then the creator sells through cold DMs and a free sample post. A second option, a "LinkedIn profile cleanup + five launch posts" package, is mentioned only briefly. — [Sabrina Ramonov, "I Asked Claude To Make Me As Much Money As Possible" (Apr 2026, ~487K views)](https://www.youtube.com/watch?v=AP-fOOmm02g)
- Title-only signals (not transcript-verified) from high-view candidates in the pool:
  - Faceless YouTube / Shorts channels: [$39K faceless channel](https://www.youtube.com/watch?v=8Rf0xna31xg) and other titles in the CSV.
  - $10K websites for clients: Metics Media, Jack Roberts, Nick Saraev, Zubair Trabzada titles in the CSV.
  - "Build & Sell" Claude Code courses: Nick Saraev, Nate Herk.
  - Side-hustle listicles: Patrick Dang, Shane Hummus, Ayushman Pandita, Sean Dollwet, Alek.
  - Ebooks: Molly Keyser.
  - Trading: AI Pathways "made $102k"; Investors way.
  - Dropshipping: Austin Rabin "$2.7M".
  - Vibe-coded apps: Jason Lee "$400K/mo app".
  - WhatsApp agents: Oliver Rasmussen "$12,000/month".
  - Source for all of the above: `data/candidate_videos_description_signals.csv`. Titles are copied from YouTube metadata; the claims are unverified.

### Inferences
- Judging only by titles, the content falls into roughly five groups: service businesses (websites, automations/agents, ghostwriting), content farms (faceless YouTube/Shorts), software products (SaaS/apps), info products (ebooks, courses), and trading. This is a hypothesis for the report writer to test against other researchers' notes.

### Gaps
- Method frequency counts across 150+ transcripts could not be produced. Transcript access was blocked (see collection log).

## For each method: typical steps, tools and costs, price points, claimed income, time to first sale

### Takeaway
I have step-level detail for only one method, LinkedIn ghostwriting via Claude prompts. The creator says it relies mainly on high-volume manual DMs, not on Claude itself.

### Cited Findings
- **Steps, as described:**
  1. Prompt Claude for "two ways I could make my first $1,000 in 30 days" that use existing skills, need no audience and are sellable within 48 hours. Claude asks clarifying questions until it is 95% confident.
  2. Ask Claude for the most successful person to model (Justin Welsh).
  3. Have Claude role-play that person and write a 20-day plan under $1,000.
  4. Days 1–3: build your own profile and a prospect list of SaaS founders.
  5. Days 4–10: DM founders and offer one free post in their voice.
  6. Close with a fixed price via a Stripe payment link, without discounting.
  - [Source](https://www.youtube.com/watch?v=AP-fOOmm02g)
- **Tools and costs:** Claude.ai, LinkedIn (Premium mentioned) and Stripe payment links. Total upfront cost is "less than $1,000"; no itemized prices are given. — [Source](https://www.youtube.com/watch?v=AP-fOOmm02g)
- **Price points:** these are Claude-suggested or example figures, not the creator's actual sales: "$750" per client, and "$500" in the bonus-prompt example. — [Source](https://www.youtube.com/watch?v=AP-fOOmm02g)
- **Claimed income:** "three prompts I gave Claude to make me an extra $15,000 in 10 days with less than $1,000 invested upfront" ([00:00]). This is a claim; it is not tied to the ghostwriting method shown. — [Source](https://www.youtube.com/watch?v=AP-fOOmm02g)
- **Time to first sale:** the plan targets a first customer within 20 days. — [Source](https://www.youtube.com/watch?v=AP-fOOmm02g)

### Inferences
- In this example, Claude's role is planning and strategy. The revenue-generating work (prospecting, DMs, writing the posts) is human.

### Gaps
- Per-method steps, costs, prices and time-to-first-sale for websites, automation agencies, SaaS, faceless YouTube, ebooks, skills/MCP sales and trading are not available from transcripts.

## What share of videos show verifiable proof vs. unverified claims? What share funnel viewers to a paid course, community or affiliate offer?

### Takeaway
Proof share across transcripts cannot be computed (n=1, verbal claim only). Description metadata for the 265 candidates suggests heavy commercial funnelling: about 27% link Skool, and about 42% contain affiliate or discount markers. These are regex signals on descriptions, not transcript findings.

### Cited Findings
- **Transcript-based (n=1):** the $15K claim is verbal only. No Stripe, bank or dashboard is referenced in the transcript. The description carries an affiliate/ref link (blotato.com `?ref=`) and a free-resources site; the creator founded Blotato. No course or community is pitched. — [Source](https://www.youtube.com/watch?v=AP-fOOmm02g)
- **Description regex across 265 candidates** (file: `data/candidate_videos_description_signals.csv`; descriptions from the YouTube Data API `videos.list`):

  | Signal in description | Videos | Share |
  |---|---|---|
  | Skool link | 72 | 27% |
  | Whop link | 5 | 2% |
  | Course/community/masterclass/coaching wording | 150 | 57% (noisy: includes videos titled "full course") |
  | Affiliate/ref/discount-code markers | 111 | 42% |
  | Sponsor wording | 30 | 11% |
  | Book-a-call / apply / Calendly | 29 | 11% |
  | Any paid-funnel marker (Skool, Whop, course wording, or book-a-call) | 172 | 65% |
  | Dollar, "k", "lakh" or "crore" figure in the title | 117 | 44% |

- Example from metadata: the top search result's description opens with "Claim your FREE $499 Masterclass … https://mikeyno-code.com/Skool-base44". — [Mikey No Code, "How I'm ONLY Using Claude Code to Make Money Online in 2026"](https://www.youtube.com/watch?v=qF0-bXhRrTQ)

### Inferences
- About 44% of titles carry an income figure, and about two-thirds of descriptions have a paid-funnel marker. This suggests the genre is substantially lead-generation for the creators' own offers. Confirming that needs transcript or on-screen review.

### Gaps
- The proof-level distribution (dashboard shown vs. verbal claim) needs transcripts or video frames; neither was available.

## Which methods do creators admit require sales, outreach or manual work (i.e., not fully automated)?

### Takeaway
In the one transcript analyzed, the creator says plainly that the bottleneck is manual cold outreach, not AI.

### Cited Findings
- "The skill isn't the writing. I already have that. The skill is doing the unsexy thing 300 times in a row, which is sending DMs." ([09:07]) — [Source](https://www.youtube.com/watch?v=AP-fOOmm02g)
- "Volume is a beautiful thing... volume gives you data and feedback faster." ([11:08]) — [Source](https://www.youtube.com/watch?v=AP-fOOmm02g)

### Inferences
- None generalizable beyond this one video.

### Gaps
- Cross-method comparison of "admitted manual" vs. "claimed passive" was not possible.

## What warnings, failure modes and caveats are mentioned?

### Takeaway
From the one transcript, the failure modes are behavioural: not sending DMs, quitting after being ghosted, discounting, and procrastinating.

### Cited Findings
- Failure modes the creator names:
  - Not sending the DMs (she calls this the biggest reason people fail).
  - Quitting after being ghosted.
  - Fear of rejection.
  - Discounting or over-justifying the price.
  - Over-consuming a mentor's content instead of doing outreach.
  - Plans that put customer acquisition too late.
  - Procrastination; a bonus prompt has Claude cut the plan in half.
  - [Source](https://www.youtube.com/watch?v=AP-fOOmm02g)
- Caveat: Claude's suggestions depend on how much context about you it is given; the prompts ask it to keep questioning until it is 95% confident. — [Source](https://www.youtube.com/watch?v=AP-fOOmm02g)

### Inferences
- None generalizable.

### Gaps
- Warnings across the wider corpus (API costs, platform bans, saturation, refund risk, quality problems with AI-built sites or apps) were not collected.

## 10–15 most concrete, well-evidenced case studies

### Takeaway
I cannot deliver the requested 10–15 case studies, because only one transcript was analyzed.

### Cited Findings
- **Case 1 (only analyzed case):**
  - Video: Sabrina Ramonov, "I Asked Claude To Make Me As Much Money As Possible", uploaded 2026-04-11, ~487K views, 12 min. [Link](https://www.youtube.com/watch?v=AP-fOOmm02g)
  - Method: Claude-planned LinkedIn ghostwriting service sold via about 300 cold DMs.
  - Numbers: $15K in 10 days (claimed); $500–$750 per client (examples).
  - Proof level: verbal claim only.
  - Funnel: affiliate/ref link to the creator's own SaaS; no course.
  - Concreteness: 3/5.
- **Candidates I would have prioritized**, chosen because the title makes a specific income claim (titles only; unverified):
  - [Kellan Henneberry "$24,937/mo posting YouTube Shorts"](https://www.youtube.com/watch?v=V_t51u1tBJc)
  - [Jason Lee "Vibe Coded a $400K/mo App"](https://www.youtube.com/watch?v=hDOUzlJwM1E)
  - [AI Pathways "Letting Claude Trade… Made $102k"](https://www.youtube.com/watch?v=RetsRS5u-8Q)
  - [Molly Keyser "selling Ebooks with Claude"](https://www.youtube.com/watch?v=nmRWmF2Umes)
  - [Oliver Rasmussen "Claude + WhatsApp = $12,000/month"](https://www.youtube.com/watch?v=-VXrYRBCdCU)

### Inferences
- None.

### Gaps
- To finish this research, someone would need either restored transcript credits (TubeAlfred, vidIQ or Subscribr) or a sanctioned transcript source. The prepared pipeline is in the scratchpad at `tx/extract.py` with `tx/schema.json`. It runs structured extraction through a headless Claude call at about $0.13 per video, and could process the 265-video list in `tx/ids_all.txt`.
