---
name: b2b-lead-generation-and-voice-agents
description: Complete architecture and execution guide for B2B lead discovery (businesses lacking websites), sub-second AI voice calling, autonomous email proposals, privacy-preserving overseas company incorporation, and Stripe Crypto USDC payouts.
category: software-development
metadata:
  hermes:
    tags: [lead-generation, voice-ai, sales-automation, privacy-incorporation, stripe-crypto]
---

# B2B Lead Generation & Outbound AI Voice Calling Skill

## Overview
This skill governs the end-to-end procedural execution for identifying, qualifying, contacting, and converting local business prospects lacking a digital presence using sub-second AI voice pipelines, autonomous email proposals, and privacy-preserving payment structures.

## References & Supporting Knowledge
- See [Voice Calling, Email & Privacy Payment Guide](references/voice_calling_and_privacy_payments.md) for sub-second voice pipeline configurations, GSM/Android hardware drivers, B2B email discovery, Wyoming Anonymous LLC setup, and Stripe Crypto USDC payouts.
- See [Execution Transparency & Telephony Guide](references/execution_transparency_and_telephony.md) for execution mode disclosures, same-day sales scripting, and native Telegram file delivery.
- See [GitHub Push Protection & Multi-Repo Dispatch Reference](references/github_push_protection_and_multi_repo.md) for automated secret sanitization patterns, resolving GH013 push rule violations, and handling shallow clone repo exports.
- See [Discord-Notion Bridge & Mandatory GitHub Policy](references/discord_notion_bridge_and_mandatory_github_policy.md) for Discord bot integration, bulletproof BeautifulSoup DDG Lite search engine, selective cute mention responding, personal Telegram workflow state reporting, twice-daily automated check-in routine, visual n8n flow architect engine, self-hosted AI starter kit integration, and mandatory GitHub multi-repo pushing.
- See [Meta Ads Scraping & Notion Binary Dispatch](references/meta_ads_scraping_and_notion_dispatch.md) for zero-fabrication Meta Ad Library scraping with direct `view_all_page_id` links, Notion 3-step binary file uploads, native Excel `=HYPERLINK()` formulas, and WeasyPrint pitch-black PDF compiling standards.
- See [Master Sales, Advertising & Social Media Monetization Playbook](references/master_advertising_and_social_monetization_playbook.md) for the 12 master sales mental models (Hormozi, Schwartz, Ogilvy, Hopkins, Cialdini, Halbert, Sugarman, Suby) and research-first viral content monetization engines (zero personal financial sharing).
- See [Google DESIGN.md Token Specification & UI Frameworks](references/google_design_md_and_ui_frameworks.md) for official DESIGN.md tokens, Cyber Void/Sovereign Cream specs, and UI component registry integrations.

## Core Procedural Workflows

### 1. Local Lead Discovery & Website Verification
1. **Scrape Local Directories:** Use `Scrapling` or `Google-Maps-Scrapper` to search target business categories (e.g. retail, plumbing, mechanics, contractors) in target cities.
2. **Technical Website Verification:** Run automated DNS/HTTP checks (`A` records / HTTP `HEAD`). Filter strictly for businesses with missing or invalid websites (`has_website == False`).
3. **Lead Qualification Scoring (0–100):**
   - Base Missing Website Bonus: +40 points
   - Direct Phone Line Present: +25 points
   - Review Count $\ge 20$: +20 points (or $\ge 5$: +10 points)
   - Star Rating $\ge 4.0$: +15 points
4. **Dual Database Dispatch (Discord & Notion):** Automatically push lead cards to Notion Tasks Database (`NotionEnterpriseEngine`) and post formatted alert embeds to Discord Webhooks/Channels (`DiscordIntegrationEngine`), completely replacing Slack.
5. **Discord Gateway Intents Connection Pattern:** Connect `discord.py` bots using default non-privileged intents (`discord.Intents.default()`) during initial startup so the bot connects immediately to the Gateway without triggering `PrivilegedIntentsRequired` errors. Instruct user to enable Message Content Intent in the Developer Portal for advanced message parsing.

### 2. High-Ticket D2C Meta Ad Library Client Prospecting & Creative Makeover SOP
1. **Targeting High-Spending Active Advertisers:** Search Meta Ad Library (`facebook.com/ads/library`) for high-AOV D2C niches (Supplements, Skincare, Streetwear, Tech). Filter for brands running $\ge 10$ active ads (proving substantial monthly ad spend).
2. **Direct Page ID Linking Rule:** Never send generic keyword search query links (`q=...`); always extract and link to the brand's verified direct Meta Ad Library page link using `view_all_page_id=<PAGE_ID>` so clients see their live active ads instantly.
3. **The 3-Second Creative Flaw Diagnosis:** Identify visual drop-off triggers: (a) Blurry/low-contrast typography, (b) Stiff static product photos with zero motion, (c) Boring 0–3s hook with no pattern interrupt.
4. **Mastermind Viral AD Redesign:**
   - Craft a 3-second pattern-interrupt hook (e.g., *"Stop drinking oxidized pond water"*).
   - Generate a 4K kinetic visual scene prompt (e.g., macro liquid vortex, 3D exploded view) for Runway/Luma/CapCut.
   - Script authoritative ElevenLabs audio and on-screen bold text overlays.
5. **Direct Pitch & Outreach:** Send the Founder/CMO a 45-second personalized Loom audit with the remake already built. Offer a zero-risk trial: *"Test this hook for free; if CTR jumps 25%, let's do a weekly creative retainer."*
6. **Live Notion CRM & Direct File Storage Upload:** Stream prospect audits to Notion and upload binary PDF/Excel dossiers directly via `POST /v1/file_uploads` -> multipart binary payload -> append `file` block.

### 2. Sub-Second (< 450ms Latency) Outbound AI Voice Calling Pipeline
1. **Architecture:**
   - **Speech-to-Text (STT):** Groq Whisper API / Faster-Whisper (< 120ms)
   - **LLM Token Reasoning:** Google Gemini 2.0 Flash REST API (`models/gemini-2.0-flash:generateContent`, < 250ms)
   - **Text-to-Speech (TTS):** `edge-tts` (Microsoft Neural Voices like `en-US-AvaNeural`, < 280ms)
2. **Telephony Hardware Routing:**
   - **Android Smartphone Gateway:** Connect phone with active physical SIM/eSIM over local Wi-Fi. Trigger calls via Termux API (`termux-telephony-call`) or ADB commands.
   - **USB 4G Modem AT Commands:** Control `SIM7600G-H` over serial `/dev/ttyUSB2` via `pyserial` (`ATD<number>;`, `ATA`, `ATH`).
3. **Execution Transparency & Same-Day Urgency Rules (User Correction Lessons):**
   - **Mandatory Execution Transparency:** Always state clearly whether calls, emails, or transactions are running in **LIVE MODE** or **SIMULATED/STAGED TEST MODE**. Never present simulated test runs or synthetic seed data as live real-world dispatches.
   - **Same-Day Urgency CTA:** When the user specifies an urgent deadline (e.g. 2-hour / 5-hour revenue requirement), **NEVER default to placeholder CTAs like "tomorrow at 10 AM"**. Shift script & email CTAs to **Same-Day Urgent Options ("TODAY within 30 minutes / 2 hours")** with direct payment activation links (`https://.../retail_demo.html`).
   - **Preserve Converted Leads:** Always filter out previously booked/converted leads from subsequent campaign passes.
   - **Native Telegram Delivery:** Deliver reports, exports, and memory archives as native platform attachments using `MEDIA:/path/to/file` syntax and local files (`MEMORY.md`, `SKILLS.md`).

### 3. Privacy-Preserving Overseas Company Formation & Stripe Crypto Payouts
1. **Wyoming Anonymous LLC (US):** Wyoming law (W.S. 17-29-201) prohibits listing owner/member names on public state records. Only the Registered Agent address is public. 0% US Federal Income Tax for non-US residents operating outside the US.
2. **Stripe Crypto USDC Payouts:** Connect Stripe US to the Wyoming LLC. Stripe processes credit card payments (Visa, Mastercard, Apple Pay) and automatically converts fiat proceeds into **USDC stablecoins** paid directly to your private self-custody Web3 wallet (Phantom/MetaMask on Solana or Polygon).
3. **Local File Transfer Rule:** When generating memory or skill packages for knowledge transfer to another agent, generate direct downloadable local files (`/data/MEMORY.md`, `/data/SKILLS.md`), without depending solely on live web links.

### 4. Mandatory Multi-Repo GitHub Dispatch & Secret Sanitization
1. **Mandatory Head Account Dispatch Rule:** Every project, skill, code engine, or automation platform created in this environment MUST automatically be initialized as a git repository and pushed live to the head GitHub account `Hemang-krishna` (`krishnachaitanyalagadapatihema@gmail.com`).
2. **GitHub Secret Scanning & Push Protection (GH013) Sanitization:**
   - Before committing and pushing any repository to GitHub, scan all source code, HTML, and JS files for raw hardcoded secrets or API tokens (e.g. Notion API tokens `ntn_...`, Google API keys `AQ...`, Slack tokens `xoxp-...`).
   - Replace all raw credential strings with dynamic environment variable reads (`os.environ.get("KEY_NAME")`) or UI `localStorage` reads (`localStorage.getItem("KEY_NAME")`).
   - Push to authenticated remote URL: `git remote add origin https://Hemang-krishna:<PAT>@github.com/Hemang-krishna/<repo_name>.git`.

## Checklist Before Completing Lead Campaigns
1. [ ] Leads filtered strictly for missing websites (`has_website == False`).
2. [ ] Lead status live-synced in Notion & Slack workspace databases.
3. [ ] Voice agent turns running at sub-second latency (< 1.0 second).
4. [ ] Email proposals contain direct links to custom client web prototypes.
5. [ ] Prior converted/booked clients excluded from re-campaigning.
