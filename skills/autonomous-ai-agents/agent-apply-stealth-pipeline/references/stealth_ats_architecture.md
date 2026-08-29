# Stealth ATS Scraping & Anti-Detection Architecture

## 1. Cloudflare & Bot Detection Bypass
- Modern ATS platforms (Greenhouse, Lever, Ashby) enforce Cloudflare Turnstile or Akamai bot protection on HTML submission pages.
- **Bypass Rule:** Direct REST JSON endpoints bypass frontend Cloudflare checks entirely:
  - Greenhouse: `https://boards-api.greenhouse.io/v1/boards/{board_token}/jobs/{job_id}`
  - Lever: `https://api.lever.co/v0/postings/{company}/{job_id}`
  - Remotive: `https://remotive.com/api/remote-jobs`
  - Himalayas: `https://himalayas.app/jobs/api`

## 2. Keystroke Cadence Simulation (Zero-AI Fingerprint)
- Standard ATS input monitoring flags uniform typing rates (e.g. 50ms constant) or instantaneous clipboard dumps (<500ms for 500 chars).
- **Humanized Pattern:**
  - Jitter: Random Gaussian distribution between 45ms and 120ms per character.
  - Pauses: Natural 400ms–800ms punctuation pauses after commas and periods.
  - Cursor: Bezier curve mouse movements with variable speed before clicking inputs.

## 3. Remote Work Playbook from India
- **Contract Type:** Specify B2B C2C Contractor or Global EOR (Employer of Record via Deel / Oyster / Remote.com).
- **Timezone Overlap:** Explicitly declare 4+ hours daily overlap with US Eastern (EST) / Pacific (PST) or European (CET) business hours.
- **Proof of Work:** Anchor all technical responses in verified open-source GitHub repositories.
