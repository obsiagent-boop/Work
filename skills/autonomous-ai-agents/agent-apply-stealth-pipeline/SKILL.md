---
name: agent-apply-stealth-pipeline
description: "Use when automating job applications on ATS platforms."
platforms: [linux, macos, windows]
---

# Agent Apply: Autonomous Stealth Job Application Skill

## Trigger
Use this skill whenever the user requests automating job applications, applying for global/US/EU remote roles from India (including AI Operations, AI Customer Support / CX, Prompt Testing, RLHF Annotation, and real-time payout gigs), scraping high-paying remote jobs, or interacting with ATS platforms (Greenhouse, Lever, Ashby, Workday, LinkedIn, Outlier, Alignerr, ModSquad) with zero AI touch, strict anti-detection, and local data isolation.

## Target Job Universes & Roles
1. **AI Operations & Human-in-the-Loop:** Airtable/Notion data pipelines, spreadsheet verification, Zapier/Make workflow operators.
2. **AI Customer Support & Experience (CX):** Omnichannel ticket triage (Zendesk, Intercom, Freshdesk, Helpscout), AI chatbot escalation handling, CSAT optimization.
3. **RLHF Prompt Testing & Output Evaluation:** Chatbot red-teaming, model factuality rating, response comparison, hallucination detection.
4. **Real-Time Payout Gigs ($15–$60 USD/hr):** High-frequency payout platforms (Outlier AI, Alignerr, DataAnnotation.tech, Invisible Technologies, ModSquad, OneForma) with instant PayPal, Deel, Wise, or USDC rails.
5. **Engineering & Systems Roles:** Autonomous systems, Python backend, quantitative infrastructure.

## Core Principles & Security Architecture

### 1. Absolute Data Isolation & Privacy
- **Local Vault Storage Only:** Personal credentials, resumes, portfolios, and pre-vetted answer templates are stored exclusively in `/data/project_agent_apply/config/profile_vault.json` and local SQLite ledger (`applications.db`).
- **Zero Third-Party Telemetry:** Never send user credentials or PII to external third-party logging endpoints.

### 2. Zero-AI-Touch & Anti-Detection Standards
- **Keystroke Cadence Simulation:** Real ATS screening engines detect instant clipboard pastes and uniform typing intervals. Always simulate human typing delays (45ms–120ms with randomized cursor movement and natural jitter).
- **Zero Hallucinated AI Clichés:** Never generate generic AI-sounding responses ("I am thrilled to apply..."). Use structured, pre-vetted technical narratives anchored in verified GitHub repositories (e.g. `github.com/Hemang-krishna/personal-agent-os`) and production deliverables.
- **Headless Browser Stealth:** Employ Playwright stealth plugins with randomized User-Agents and real browser fingerprints.

### 3. The 4-Phase Operational Pipeline
1. **Global Reconnaissance:** Scrape real-time high-paying ($80k–$160k+ USD) remote jobs via direct ATS endpoints (Greenhouse, Lever, Ashby) and global APIs (Remotive, Himalayas, WeWorkRemotely).
2. **Profile Vault Mapping:** Map candidate attributes (Work authorization, B2B contractor status, 4-hour US timezone overlap, GitHub proof of work) to specific form fields.
3. **Pre-Flight User Approval Gate:** Provide an interactive dry-run mode showing exact mapped fields before executing final form submission.
4. **Audit Ledger & Verification:** Record all submissions in SQLite (`applications.db`) with timestamps, role IDs, and verification receipts.

## Execution Commands
- **Scan Live Remote Jobs:** `python3 /data/project_agent_apply/scrapers/remote_job_scanner.py`
- **Run Dry-Run Application Batch:** `python3 /data/project_agent_apply/scripts/orchestrator.py`
- **Audit Application History:** `python3 /data/project_agent_apply/scripts/orchestrator.py list`

## References & Playbooks
- `references/stealth_ats_architecture.md` — In-depth ATS field mapping and humanized typing heuristics.
- `references/realtime_ai_gigs_playbook.md` — Evaluation guide for Outlier, Alignerr, DataAnnotation, Invisible, ModSquad, and OneForma.
- `references/ghost_delivery_and_payouts_playbook.md` — Complete guide for autonomous client delivery (landing pages, research, bots) and the 5 direct global-to-India payout pipelines (Wise, Payoneer, Contra, Stripe, USDC) under Section 44ADA.
- `references/alternative_monetization_blueprints.md` — Complete execution guide for 7 alternative monetization streams (Cold Audit Redesigns, LemonSqueezy/Gumroad digital packs, uTest/Testlio bug hunting, white-label bots, niche lead databases).
- `references/design_md_and_ui_registries_guide.md` — Google DESIGN.md token specifications, 9 extraction engines, 7 UI component registries, and the mandatory 'state plan before building' workflow habit.
- `references/master_sales_advertising_and_sovereign_hooks.md` — Master sales and direct-response advertising mental models (Hormozi, Ogilvy, Schwartz, Cialdini, Hopkins, Halbert), the Sovereign Authority Hook framework (zero competitor mentions, zero personal roadmaps, pure objective research), and the 8 scalable web monetization engines.
- `references/ats_resume_formatting_rules.md` — Authoritative ATS-safe formatting rules: standard fonts (Calibri/Arial 10-12pt), name (14-16pt), headings (12-14pt bold), zero tables/columns/boxes/headers/footers, standard section titles, and .docx delivery.
- `references/linkedin_job_scraping_and_cron_pipeline.md` — Multi-tiered LinkedIn scraping architecture (Apify + guest search fallback), daily 4:00 PM cron supervisor automation, candidate data anonymization standard, and Supabase database syncing.

## Pitfalls & Best Practices
- **Absolute Identity & Deployment Policy:** Strictly deploy all GitHub Pages, repositories, code commits, and project artifacts under the active GitHub identity **`obsiagent-boop`** (`obsi.agent@gmail.com`). Never reintroduce legacy personal names or deprecated credentials into configs, vaults, or transcripts.
- **Explicit Habit: State Plan Before Execution:** Always communicate the architectural plan, design tokens, reference sources, and intended sequence to the user before generating production code or building complex deliverables.
- **No Direct Raw Submits Without Dry-Run:** Never submit live job applications without passing through the Pre-Flight User Approval Gate to prevent unauthorized submissions or stale field values.
- **Section 44ADA 50% Tax Advantage:** When receiving foreign freelance revenue under ₹75L/year in India, declare under Section 44ADA (50% presumptive profit) and ensure export of services is filed under 0% GST (LUT) with automated e-FIRA/FIRC certificates via Wise or Payoneer.
- **Immediate Ghost-Delivery Capability:** When client asks for landing pages or web apps, generate static responsive HTML/Tailwind templates directly under `/data/project_agent_apply/services/templates/` with 100/100 Lighthouse performance.


