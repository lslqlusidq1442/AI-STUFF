# Product Businesses Built with Claude: Real-World Economics (as of October 2026)

Scope: micro-SaaS/web apps built with Claude Code or vibe coding, mobile apps, Chrome/Shopify/WordPress add-ons, Claude skills/MCP servers/prompts/templates, digital products (ebooks/KDP, Gumroad/Etsy, courses), and API wrappers/data products. Research date: 2026-10-12.

Evidence labels used below:
- **[VERIFIED DATA]**: payment-provider-verified or first-party platform data, or the platform's official policy text.
- **[SECONDARY]**: a third-party analysis of real data, with the methodology at least partly disclosed.
- **[ANECDOTE]**: self-reported or vendor marketing, not independently verified.

---

## Q1. What do revenue distribution datasets show? What share of launches reach >$0, >$1k/month, >$10k/month?

### Takeaway
Every dataset found shows a steep power law. In the largest payment-verified indie dataset (TrustMRR, about 10,150 products, Sept 2026), about 26% of listed products have never recorded a payment, only about 49% earned anything in the prior 30 days, the median earning product made about $169 in 30 days, and only about 2.4% reach about $8.3k MRR (about $100k ARR). Mobile shows the same pattern: per RevenueCat, 17.3% of new subscription apps reach $1k/month and 4.6% reach $10k/month within two years. Those numbers already exclude the many projects that never connect a payment provider, so the true distribution for all launches is worse.

### Cited Findings

**SaaS / web apps (TrustMRR, Stripe-verified)**
- [VERIFIED DATA, secondary analysis] TrustMRR snapshot pulled Sept 4, 2026: 10,150 listed products. 58.4% had zero MRR. 26.1% (2,654) had never recorded revenue. 2,417 had earned before but had nothing in the last 30 days. 49.1% (4,987) earned in the prior 30 days. The median 30-day revenue among earning products was $169. The top 1% (102 products) took 76.1% of all 30-day revenue. 245 products (2.41%) were at $8,333+ MRR after stale records were removed, and 353 were at $5k+ MRR. The median subscription price was $13/month. Caveats: self-selected listings, survivorship bias (launched Oct/Nov 2025), and stale connections concentrated at the top. The article also has small arithmetic inconsistencies (92 products unaccounted for; it says 72.9% ever earned, but 100% − 26.1% = 73.9%). — [TechStartups, Sept 28 2026](https://techstartups.com/2026/09/28/what-percentage-of-indie-hacker-products-make-100k-in-arr/)
- [SECONDARY] An analysis of 3,787 revenue-generating TrustMRR businesses (non-earners excluded) found median MRR of $145, a 75th percentile of $894, a 90th percentile of $5,107, a 95th percentile of $13,205, and 6.1% at or above $10k MRR. The same search summary cites a live TrustMRR distribution of 68.3% below $1k, 16.7% at $1k–10k, 10% at $10k–100k, 4% at $100k–1M and 1% above $1M. That sample is listed businesses and skews upward. — [stealwhatworks.com](https://stealwhatworks.com/blogs/news/indie-hackers-over-10k-per-month); [saasranger.com](https://saasranger.com/blog/micro-saas-revenue-reality-what-1000-founders-actually-earn/)
- [SECONDARY] An aggregator reports about 6,040 TrustMRR startups with average MRR of about $4,682, and a median of about $177 for AI startups under $5k. The averages are distorted by outliers. — [bigideasdb.com](https://bigideasdb.com/trustmrr)
- [VERIFIED DATA] The TrustMRR leaderboard tops out at about $3.57M MRR, with #2 at about $864k and #3 at about $424k. Verification runs through read-only Stripe, RevenueCat, Superwall or Creem connections. — [trustmrr.com](https://trustmrr.com/); [exitbid.io review](https://exitbid.io/blog/trustmrr-review-2026)
- [ANECDOTE / weakly sourced] Blog estimates conflict. One says about 70% of micro-SaaS products never pass $500/month and 1–2% exceed $50k MRR (attributed to a "RockingWeb 2025 analysis" of 1,000 products). Another claims 40% never reach $1k MRR. — [boringriches.com](https://boringriches.com/guides/saas-business-revenue-benchmarks/); [softwareseni.com](https://www.softwareseni.com/solo-founder-saas-metrics-from-0-to-10k-mrr-in-6-months-with-realistic-timelines/)
- No current Stripe-published distribution was found. The only Stripe-linked figure is an older Indie Hackers set of 937 Stripe-verified products, with about 5% above about $8.3k/month. — [stealwhatworks.com](https://stealwhatworks.com/blogs/news/indie-hackers-over-10k-per-month)

**Mobile apps (RevenueCat State of Subscription Apps 2026: 115k+ apps, $16B+ revenue, mostly 2025 data)**
- [VERIFIED DATA, first-party aggregate] "Only 4.6% of newly launched apps reach $10K in monthly revenue within two years." 17.3% reach $1k/month within two years (Photo & Video 21.4%, Business 14.7%). About 75% of apps that reach $1k never reach $10k. Among apps that do get there, the median time is 58 days to $1k and 109 days to $10k. — [RevenueCat](https://www.revenuecat.com/state-of-subscription-apps)
- [VERIFIED DATA] Median revenue is about $72/month one year after launch. The top quartile starts at about $429/month and the top 10% at about $2,574/month. — [RevenueCat](https://www.revenuecat.com/state-of-subscription-apps)
- [VERIFIED DATA] Saturation: about 15,000 new subscription apps launch per month (14,700+ in Jan 2026), up from about 2,000/month three years earlier, and about 77% of them are on iOS. Apps launched before 2020 earn 69% of all subscription revenue, while apps launched in 2025 or later earn about 3%. — [RevenueCat](https://www.revenuecat.com/state-of-subscription-apps)
- [VERIFIED DATA] "AI-powered apps generate 41% more revenue per payer, but they churn 30% faster." The top 25% of apps grew 80% year over year while the bottom 25% shrank 33%. — [RevenueCat](https://www.revenuecat.com/state-of-subscription-apps)

**Chrome extensions**
- [SECONDARY] Paid extensions are 8.9% of Chrome Web Store extensions (Extension Monitor) but less than 2.6% of installs. A DeBugBear analysis restricted to extensions with 10 or more ratings found 4.7% support any payment, mostly one-off purchases. About 35% of paid extensions (5,885 of 16,718) have zero users. — [konabayev.com](https://konabayev.com/blog/extension-monetization-statistics-2026/); [DebugBear](https://debugbear.com/blog/counting-chrome-extensions)
- [SECONDARY] 70.4% of Chrome extensions have 100 or fewer users, and the median extension has 18 users (Exstats, cited in a 2026 report). — [konabayev.com](https://konabayev.com/blog/extension-monetization-statistics-2026/)
- [ANECDOTE] One developer's six-month freemium extension reached a 0.8% free-to-paid conversion rate and suggests 0.5–2% is realistic. — [dev.to](https://dev.to/_350df62777eb55e1/real-numbers-freemium-chrome-extension-monetization-after-6-months-5hga)

**Shopify apps**
- [VERIFIED DATA] Shopify says merchants choose from more than 16,000 apps and that it paid developers more than $1B "last year" (changelog, 2025). Developers keep 100% of their first $1M lifetime gross app revenue (counted from Jan 1, 2025) and 85% above that. Registration is a one-time $19 Partner fee. No per-app distribution is published. — [Shopify changelog](https://shopify.dev/changelog/update-to-shopifys-app-developer-revenue-share); [Shopify revenue share docs](https://shopify.dev/docs/apps/launch/distribution/revenue-share)

**Gumroad / digital products**
- [VERIFIED DATA, but old] Gumroad's own 2020 recap: about 45,917 creators made at least one sale, and about 7,945 (about 17%) earned at least $1,000 for the year. The top 1% took about 60% of earnings. — [Gumroad "Last Year in the Creator Economy"](https://gumroad.gumroad.com/p/last-year-in-the-creator-economy)
- [SECONDARY, low reliability] InsightRaider's crawl of 146,271 Gumroad products modeled revenue as listed price times a sales proxy, but only 12,952 products (8.9%) had a sales count. Within that subset, the top 130 products made 77.3% of modeled revenue. The page itself says this "is modeled gross product revenue, not audited earnings" and that there is no validated error margin. Headlines that claim "99.5% to top 1%" or "<5% earn >$1k/month" go beyond what the data supports. — [InsightRaider State of Gumroad 2026](https://insightraider.com/en/state-of-gumroad-2026); [InsightRaider stats](https://insightraider.com/en/data/gumroad-statistics-2026)

**MCP servers / skills**
- [ANECDOTE / unsourced estimate] Fewer than 5% of the 20,000+ published MCP servers generate any revenue. Most money comes from custom builds and hosted servers, not open-source listings. — [a8gent.com](https://a8gent.com/blog/sell-mcp-servers-monetize-guide) / [mcp-marketplace.io](https://mcp-marketplace.io/blog/state-of-mcp-monetization-2026) (vendor sources)

### Inferences
- Across SaaS (TrustMRR) and mobile (RevenueCat), the figures line up roughly. Of products that are serious enough to connect a payment provider, about 50–75% make more than $0. About 15–30% reach $1k/month at some point. About 2.5–6% reach $8–10k/month. As a share of all launches, including abandoned projects that never connect payments, these rates are probably much lower. That last point is inference: no dataset covers zero-effort launches.
- Revenue is extremely concentrated. The top 1% take 60–76% of revenue on both Gumroad (2020) and TrustMRR (2026).
- Monthly subscription-app launches have grown about 7x in three years, consistent with AI coding tools lowering build costs. New cohorts get a shrinking share of revenue, so saturation is real and measurable on mobile.
- For Chrome extensions, the median outcome is effectively zero users. Monetization is rare and usually a one-off purchase.

### Gaps
- No dataset isolates Claude-Code-built or vibe-coded products from other products. Every distribution above is for all indie or subscription products.
- No WordPress plugin revenue distribution was found.
- No Etsy or KDP earnings-distribution survey was found in this session. Only policy pages were retrieved.
- The "17.3% to $1k" figure is conditional on apps using RevenueCat, which skews toward more serious developers.
- Gumroad's first-party distribution data is from 2020. Nothing first-party for 2025–2026 was found.

---

## Q2. Documented case studies of Claude-Code-built products with verified MRR, and counter-examples

### Takeaway
No independently verified, payment-linked case was found of a product attributed to Claude Code earning significant MRR. Every widely circulated success story ($2.4k MRR in 3 days, a $20k MRR Mac app, $50k MRR "agent-leveraged" solo founders) is self-reported or comes from secondary blogs. The one TrustMRR-verified listing found with "Claude Code" in its name earned $235 all-time and had no active subscriptions. Counter-evidence is better documented: security failures in vibe-coded apps and App Store enforcement against undifferentiated apps.

### Cited Findings
- [VERIFIED, weak] The TrustMRR listing "Claude Code Distribution Framework" shows $235 all-time revenue and no active subscriptions as of its last update. — [TrustMRR](https://trustmrr.com/startup/claude-code-distribution-framework)
- [ANECDOTE] A solo founder with no Swift experience reportedly built a macOS app with Claude Code that reached $20k MRR six months after launch. The figures come from an Indie Hackers/X disclosure relayed by a secondary blog and are not verified. — [waytoclawearn.com](https://waytoclawearn.com/en/cases/claude-code-mac-app-20k-mrr-solo-founder-2026)
- [ANECDOTE] A Medium post: "I Built a SaaS in 3 Days Using Claude Code. It Makes $2,400/Month." Personal account, no verification. — [Stackademic/Medium](https://blog.stackademic.com/i-built-a-saas-in-3-days-using-claude-code-it-makes-2-400-month-heres-the-entire-process-0af017932f9c?gi=d2f6ef514125)
- [ANECDOTE] A GitHub testimonial on the anthropics/claude-code repo reports "5 SaaS products shipped in 8 weeks" by a Belgian solo founder. It gives no MRR, and the enterprise and government deals are described as still in negotiation. Shipping speed is documented here, revenue is not. — [GitHub issue #28527](https://github.com/anthropics/claude-code/issues/28527)
- [ANECDOTE] An industry blog claims solo founders using Claude Code and Cursor reach $10k–$50k MRR without hiring, with no verifiable data. — [agentmarketcap.ai](https://agentmarketcap.ai/blog/2026/04/11/agent-leveraged-solo-founder-micro-saas-2026)
- [VERIFIED, counter-example] A May 2025 scan found 170 of 1,645 Lovable-built apps (about 10%) exposed sensitive user data, including names, emails, financial data and API keys, through misconfigured Supabase databases (CVE-2025-48757). — [Slashdot](https://tech.slashdot.org/story/25/05/30/1810246/); [The Next Web](https://thenextweb.com/news/lovable-vibe-coding-security-crisis-exposed)
- [VERIFIED, counter-example] Feb 2026: a Lovable-hosted app "littered with basic flaws" exposed 18k users. — [The Register](https://www.theregister.com/2026/02/27/lovable_app_vulnerabilities)
- [SECONDARY, counter-example] RedAccess, reported via WIRED, found more than 5,000 vibe-coded app instances on Lovable, Replit, Base44 and Netlify lacking basic security or authentication, about 40% of them leaking private information. Escape.tech separately found more than 2,000 vulnerabilities across 5,600 vibe-coded apps. — [freevacy/WIRED summary](https://www.freevacy.com/news/wired/study-finds-security-gaps-in-thousands-of-vibe-coded-apps/7362)
- [VERIFIED DATA, context] Platform revenue concentration (Q1) applies: 26% of TrustMRR products never record a sale. — [TechStartups](https://techstartups.com/2026/09/28/what-percentage-of-indie-hacker-products-make-100k-in-arr/)

### Inferences
- The evidence supports the claim that "Claude Code drastically lowers build time and cost." It does not support the claim that "Claude Code products make money at higher rates." A cheaper build means more launches, which on the RevenueCat data means more competition per niche.
- Security and liability are a concrete risk for vibe-coded products that handle user data. One breach can end a micro-SaaS and create legal exposure.
- The way to verify a case study is a TrustMRR or Stripe-linked profile. Screenshots on X or YouTube are not equivalent.

### Gaps
- Anthropic has published no data on revenue earned by Claude Code users' products.
- A systematic tally of TrustMRR listings whose founders credit Claude Code was not possible in this session. The TrustMRR API could enable one.
- None of the anecdotal claims above could be verified.

---

## Q3. Platform policy risks (KDP, Etsy, App Store, Anthropic terms, others)

### Takeaway
Policy risk is real but specific to each platform. KDP requires disclosure of AI-generated (not AI-assisted) content and has capped new titles at 3 per day since 2023. Etsy requires AI disclosure and bans selling prompt bundles. Apple's guideline 4.3 (spam) is being applied to undifferentiated and template apps, reportedly tightened in June 2026. Anthropic's Commercial Terms give customers ownership of outputs but bar reselling the Services or using them to build a competing product without approval.

### Cited Findings

**Amazon KDP**
- [VERIFIED, official policy] "We require you to inform us of AI-generated content" (text, images or translations created by an AI tool) when publishing or republishing. "You are not required to disclose AI-assisted content" (your own content edited or refined with AI). Publishers remain responsible for guideline compliance. The guidelines bar content "meant to mislead customers" or "typically disappointing to customers," and undifferentiated public-domain versions. — [KDP Content Guidelines](https://kdp.amazon.com/en_US/help/topic/G200672390)
- [VERIFIED via press] In Sept 2023 KDP introduced a cap of 3 new titles per day per account; Amazon said it may adjust the figure and exceptions can be requested. The KDP guidelines page does not state the cap, and no confirmation of a change since 2023 was found. — [Authors Guild](https://authorsguild.org/news/amazon-adds-to-kdp-generative-ai-policy-caps-daily-self-publishing-uploads/); [ebookfriendly](https://ebookfriendly.com/amazon-kdp-publishers-publish-more-than-3-books-a-day/)
- [SECONDARY] A third-party compliance guide says AI disclosure is not shown on product pages and does not affect ranking or royalties. This is not Amazon's own statement. — [scribecount.com](https://scribecount.com/author-resource/protecting-books/kdp-ai-content-policy-the-compliance-guide)

**Etsy**
- [SECONDARY] Etsy's Creativity Standards (from July 2024) require sellers to disclose AI involvement. Items generated by AI with seller prompts can be listed under "Designed by a seller," but selling AI prompt bundles alone is banned. A June 2025 update reportedly tightened the "Made by a seller" category. The primary Etsy policy text was not retrieved. — [aitrace.org](https://www.aitrace.org/company/etsy/practice/9868222b-5b23-41e2-9ab5-40b7cf6db2f6); [Listadum](https://www.listadum.com/blog/etsy-creativity-standards); [rankhero](https://www.rankhero.com/blog/etsy-policy-changes-2025-what-you-need-to-know)

**Apple App Store**
- [SECONDARY] Apple reportedly updated its guidelines on June 9, 2026 to tighten 4.3(b). Apps "indistinguishable" from existing ones can be rejected or even removed after going live, and saturated categories such as dating, wallpaper and fortune-telling are named. Treat this as needing confirmation against Apple's changelog. — [appcompliance.io](https://appcompliance.io/blog/apple-2026-app-review-guideline-changes/)
- [VERIFIED via press] In March 2026 Apple blocked updates to vibe-coding builder apps Replit and Vibecode (reported by The Information and The Decoder), citing rules on apps that execute code which changes their functionality. Apple said the rule does not target vibe coding as such. — [li.solutions summary](https://li.solutions/blog/apple-blocks-vibe-coded-apps/); [greensighter](https://www.greensighter.com/blog/vibe-coded-app-app-store-rejection)
- [VERIFIED, official] Apple's 2025 transparency report lists 418 apps removed under 4.3.0 Spam and 279 under 4.1.0 Copycats. — cited in [appetiteui.com](https://www.appetiteui.com/blog/app-store-vibe-coding-statistics) (secondary relay)
- [ANECDOTE] Developers report a rise in 4.3(a) "design spam" rejections for AI-built submissions. Apple publishes no rate. — [ptkd.com](https://ptkd.com/journal/app-store-rejection-4-3-a-ai-slop-design-spam)

**Anthropic terms (for building on or reselling Claude)**
- [VERIFIED, official] Commercial Terms: "Customer (a) retains all rights to its Inputs, and (b) owns its Outputs"; Anthropic assigns its rights (if any) in Outputs to the customer, subject to compliance. Anthropic "may not train models on Customer Content from Services." — [Anthropic Commercial Terms](https://www.anthropic.com/legal/commercial-terms)
- [VERIFIED, official] Restriction: customers may not "access the Services to build a competing product or service, including to train competing AI models or resell the Services except as expressly approved by Anthropic." Use must comply with the Usage Policy and Supported Regions Policy, and the customer must evaluate whether outputs are appropriate. — [Anthropic Commercial Terms](https://www.anthropic.com/legal/commercial-terms)

**MCP / skills marketplaces**
- [SECONDARY] Third-party MCP marketplaces take 15–20% (MCP Marketplace 85/15 via Stripe Connect, Apify 80/20 pay-per-event, MCPize 20%). One payout model is monthly with a $100 minimum. Anthropic's own connector directory reportedly has no paid listings. — [mcp-marketplace.io](https://mcp-marketplace.io/blog/how-to-monetize-mcp-server); [Apify](https://apify.com/mcp/developers); [mcpize.com](https://mcpize.com/developers/monetize-mcp-servers); [getchatads](https://www.getchatads.com/blog/tools-for-monetizing-mcp-servers/)

### Inferences
- Selling outputs (an ebook, code, templates) is allowed under Anthropic's commercial terms. A thin "wrapper" that simply resells raw Claude access, or a product that competes with Claude itself, needs Anthropic's approval. A product that adds a workflow on top of Claude is the normal API use case. That last point is an inference from the terms.
- KDP's 3-per-day cap and disclosure rule, Etsy's prompt-bundle ban, and Apple's 4.3 enforcement all target the same strategy: high-volume, low-differentiation AI output. That strategy is the main one promoted in "make money with AI" content.

### Gaps
- The current Anthropic Consumer Terms (Pro/Max) and Usage Policy text was not fetched in this session. It is unconfirmed whether a Pro/Max subscription may power a commercial product's backend, as opposed to being used to build it. Verify at anthropic.com/legal.
- The primary Etsy Creativity Standards text and Apple's June 2026 guideline changelog were not retrieved directly.
- The Chrome Web Store, WordPress.org and Google Play AI-content policies were not researched.

---

## Q4. Marketing and distribution as the bottleneck

### Takeaway
The data indirectly but strongly shows that distribution, not building, is the binding constraint. Launch volume is rising (about 15k subscription apps a month, 20k+ MCP servers), median extension users are 18, and the top 1% take most revenue. No rigorous dataset was found on which acquisition channels work for Claude-built products. Successful cases mostly cite an existing audience, marketplace discovery or SEO, but the evidence is anecdotal.

### Cited Findings
- [VERIFIED DATA] Monthly subscription-app launches rose about 7x in three years, and 2025+ cohorts earn about 3% of subscription revenue. — [RevenueCat](https://www.revenuecat.com/state-of-subscription-apps)
- [SECONDARY] The median Chrome extension has 18 users, and 70.4% have 100 or fewer. — [konabayev.com](https://konabayev.com/blog/extension-monetization-statistics-2026/)
- [ANECDOTE] Most MCP server revenue comes from custom builds and hosted servers (sales or service-led), not open-source listings. — [a8gent.com](https://a8gent.com/blog/sell-mcp-servers-monetize-guide)
- [VERIFIED DATA] The top 1% of TrustMRR products take 76.1% of 30-day revenue. — [TechStartups](https://techstartups.com/2026/09/28/what-percentage-of-indie-hacker-products-make-100k-in-arr/)
- [VERIFIED, old] On Gumroad, the top 1% of creators took about 60% of 2020 earnings, which is consistent with audience-driven sales. — [Gumroad](https://gumroad.gumroad.com/p/last-year-in-the-creator-economy)
- [ANECDOTE] TrustMRR is itself used as a marketing channel (public verified revenue builds trust), and its API is pitched as a source of product ideas. — [superframeworks.com](https://superframeworks.com/articles/trustmrr-api-ideas-indie-hackers)

### Inferences
- Built-in marketplace discovery (Shopify App Store, Chrome Web Store, App Store search, Etsy/KDP search) is the main alternative to building an audience. Each of these is now flooded with AI-assisted entrants, and policy enforcement (Q3) targets undifferentiated listings.
- The founders behind most viral "I made $X with Claude" stories sell courses or tools to aspiring builders, so their income may come from audience monetization rather than the product itself. This is inference. No source quantified it.

### Gaps
- No survey quantifies acquisition channels (SEO, Product Hunt, X/build-in-public, paid ads, marketplace search) for indie or AI-built products in 2025–2026.
- No customer acquisition cost data for micro-SaaS was found.

---

## Q5. API cost structure: Claude API pricing, Pro/Max plans, and margin implications

### Takeaway
As of October 2026, official Claude pricing is Opus 5.5 at $4/$20 per million input/output tokens, Sonnet 5.5 at $2/$10, Haiku 5.5 at $0.10/$0.50 (prompts up to 100k tokens), and Fable 5.1 at $10/$50. Batch is 50% off and cache reads are about 5% of input price. Consumer plans are Pro at $20/month ($17/month annual) and Max from $100/month. For most light-usage micro-SaaS, inference cost per user is small relative to a $10–30 subscription. AI-heavy products still run structurally lower gross margins (about 50–60%) than classic SaaS (80–90%), and power users can wipe out margin.

### Cited Findings
- [VERIFIED, official] API per million tokens (input / output / cache write / cache read):
  - Fable 5.1: $10 / $50 / $12.50 / $0.25
  - Opus 5.5: $4 / $20 / $5 / $0.20
  - Sonnet 5.5: $2 / $10 / $2.50 / $0.10
  - Haiku 5.5, prompts up to 100k tokens: $0.10 / $0.50 / $0.125 / $0.01
  - Haiku 5.5, prompts over 100k tokens: $0.50 / $2.50
  - Batch processing saves 50%. US-only inference is 1.1x. Opus 5.5 fast mode is 2x.
  - Source: [claude.com/pricing](https://claude.com/pricing)
- [VERIFIED, official] Plans:
  - Free: $0
  - Pro: $20/month monthly, or $17/month billed annually ($200/year)
  - Max: from $100/month (5x and 20x tiers; the page does not list each separately)
  - Team Standard seat: $25 monthly or $20 annual
  - Team Premium seat: $125 monthly or $100 annual
  - Enterprise: $20/seat plus usage at API rates
  - Source: [claude.com/pricing](https://claude.com/pricing)
- [SECONDARY] Max tiers are commonly reported as $100 (5x) and $200 (20x). — [morphllm.com](https://www.morphllm.com/claude-code-pricing)
- Conflict note: several early-2026 third-party pages list older prices (Opus 4.8 at $5/$25, Sonnet 4.6 at $3/$15, Haiku 4.5 at $1/$5), and one lists "Sonnet 5" at $2/$10. The official page is authoritative. — [metacto](https://www.metacto.com/blogs/anthropic-api-pricing-a-full-breakdown-of-costs-and-integration); [tminusai](https://www.tminusai.com/blog/claude-api-pricing-monthly-cost-2026)
- [SECONDARY] ICONIQ's Jan 2026 State of AI report (via secondary blogs): inference averages about 23% of revenue at scaling-stage AI B2B companies, and 84% saw gross margin erosion of 6 points or more from AI infrastructure. Average AI product gross margin is about 52%, up from 41% in 2024 and 45% in 2025. Bessemer (Feb 2026) puts AI product margins at 50–60%, versus 80–90% for traditional SaaS. — [beancount.io](https://beancount.io/blog/2026/07/13/llm-api-cost-cogs-ai-wrapper-gross-margin-guide); [softwareseni](https://www.softwareseni.com/why-ai-gross-margins-are-so-much-lower-than-saas-and-what-that-means-for-your-business/)
- [SECONDARY] Wrapper risk: a Google Cloud executive reportedly said in Feb 2026 that LLM wrappers and aggregators are "heading toward extinction." Cursor reportedly ran at negative gross margins on rented models before shipping its own model. — [beancount.io](https://beancount.io/blog/2026/07/13/llm-api-cost-cogs-ai-wrapper-gross-margin-guide); [aieatingtheworld](https://www.aieatingtheworld.com/articles/ai-wrapper-business-why-most-fail-2026)
- [VERIFIED DATA] The median subscription price among TrustMRR subscription products is $13/month. — [TechStartups](https://techstartups.com/2026/09/28/what-percentage-of-indie-hacker-products-make-100k-in-arr/)

### Inferences (my calculations from official prices; illustrative only)
- Assume a user makes 200 requests a month, each with 3k input and 1k output tokens.
  - On Sonnet 5.5: 0.6M × $2 + 0.2M × $10 = **$3.20/user/month**. That is about 25% of a $13/month subscription before payment fees.
  - On Haiku 5.5: 0.6M × $0.10 + 0.2M × $0.50 = **$0.16/user/month**.
  - On Opus 5.5: **$6.40/user/month**.
  - Model choice and caching therefore decide whether a cheap micro-SaaS has SaaS-like margins or wrapper-like margins.
- A one-off build with Claude Code costs about $20–$200/month in subscription fees (Pro/Max). That is small next to the time cost and is not the main economic constraint. Hosting, domains and developer-program fees are additional.
- Wrapper products face two-sided compression. Anthropic and others keep cutting prices (good for COGS), but that also lowers the value of a thin wrapper and invites first-party features that replace it.

### Gaps
- No primary access to the ICONIQ or Bessemer reports. Figures are relayed by blogs.
- Claude Code usage limits per Max tier (hours or tokens) were not verified in this session.

---

## Per-model economics summary: startup cost, time to first dollar, automation, saturation, key risks

### Takeaway
All models have low cash startup costs, typically under $300 excluding time. Outcomes are dominated by distribution and differentiation, not build cost. The best-documented odds come from mobile (RevenueCat) and SaaS (TrustMRR). Data is thin or vendor-sourced for MCP servers, skills, prompts and templates, and absent for WordPress plugins and KDP earnings.

### Cited Findings
- **Micro-SaaS / web apps:** 26% of listed products never earn and about 2.4% reach about $100k ARR. The median earning product makes about $169 in 30 days and the median subscription is $13/month. — [TechStartups/TrustMRR](https://techstartups.com/2026/09/28/what-percentage-of-indie-hacker-products-make-100k-in-arr/). Key risk: security failures in AI-generated apps (about 10% of a Lovable sample leaked data). — [Slashdot](https://tech.slashdot.org/story/25/05/30/1810246/)
- **Mobile apps:** 17.3% reach $1k/month and 4.6% reach $10k/month within two years. The median is $72/month at year one. Apps that reach $1k take a median 58 days. About 15k new subscription apps launch per month. — [RevenueCat](https://www.revenuecat.com/state-of-subscription-apps). Key risk: Apple 4.3 spam enforcement. — [appcompliance.io](https://appcompliance.io/blog/apple-2026-app-review-guideline-changes/)
- **Chrome extensions:** median 18 users, 4.7–8.9% monetized, about 0.5–2% freemium conversion (anecdotal). — [konabayev.com](https://konabayev.com/blog/extension-monetization-statistics-2026/); [dev.to](https://dev.to/_350df62777eb55e1/real-numbers-freemium-chrome-extension-monetization-after-6-months-5hga)
- **Shopify apps:** $19 one-time Partner fee and 0% revenue share up to $1M lifetime. More than 16,000 apps compete, and Shopify paid out more than $1B in total. — [Shopify](https://shopify.dev/changelog/update-to-shopifys-app-developer-revenue-share)
- **MCP servers / skills:** 15–20% marketplace fees, roughly $5–25 one-time or $10–50+/month pricing (vendor claims), and under 5% of 20k+ servers earning (unsourced). Anthropic's directory reportedly has no paid listings. — [mcp-marketplace.io](https://mcp-marketplace.io/blog/how-to-monetize-mcp-server); [a8gent.com](https://a8gent.com/blog/sell-mcp-servers-monetize-guide)
- **Prompts / templates on Etsy:** prompt bundles are banned on Etsy, and AI disclosure is required. — [aitrace.org](https://www.aitrace.org/company/etsy/practice/9868222b-5b23-41e2-9ab5-40b7cf6db2f6)
- **Gumroad digital products:** about 17% of creators with at least one sale made $1k or more for the year, and the top 1% took about 60% (2020, first-party). — [Gumroad](https://gumroad.gumroad.com/p/last-year-in-the-creator-economy)
- **KDP ebooks:** disclosure of AI-generated content is required, 3 titles per day maximum (2023 cap), and "disappointing" content is prohibited. — [KDP](https://kdp.amazon.com/en_US/help/topic/G200672390); [Authors Guild](https://authorsguild.org/news/amazon-adds-to-kdp-generative-ai-policy-caps-daily-self-publishing-uploads/)
- **API wrappers / data products:** inference costs about 23% of revenue at scaling AI firms, and AI product gross margins are about 50–60%. Reselling Claude access or building competing products requires Anthropic approval. — [beancount.io](https://beancount.io/blog/2026/07/13/llm-api-cost-cogs-ai-wrapper-gross-margin-guide); [Anthropic Commercial Terms](https://www.anthropic.com/legal/commercial-terms)

### Inferences
- **Automation potential:** building is highly automatable with Claude Code. Distribution, customer support, app review compliance and security review are not. The models most pitched as "fully automated" (KDP volume publishing, Etsy printables and prompts, template apps) are the ones platforms have written specific rules against.
- **Time to first dollar:** the only hard figure is RevenueCat's median of 58 days to $1k, and it applies only to apps that ever reach $1k (17%). For most launches, time to first dollar is undefined because they never earn.
- **Saturation ranking** (inference from the evidence above), most to least saturated: KDP/Etsy AI content and prompt packs, then generic mobile utility apps and Chrome extensions, then generic AI-wrapper SaaS, then MCP servers (many free, few paid), then vertical B2B micro-SaaS and Shopify apps for specific niches. The niche B2B end is least saturated, but evidence there is thin.

### Gaps
- Apple Developer Program fee ($99/year), Google Play ($25 one-time) and Chrome Web Store ($5 one-time) are widely known but were not verified from official pages in this session.
- No 2025–2026 earnings surveys were found for KDP, Etsy digital printables, Notion template sellers, or course creators.
- No data on GPT-store-style assistant earnings, or on whether any Claude-native assistant marketplace pays creators.
- No WordPress plugin revenue data.
