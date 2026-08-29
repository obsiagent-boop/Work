# Robust LinkedIn Job Scraping & Daily Cron Pipeline Architecture

## Overview
Automated daily job scouting pipeline targeting LinkedIn Jobs, matching against candidates' ATS-compliant profile parameters, generating structured JSON and executive PDF digests, and synchronizing to Supabase PostgreSQL instances.

## 1. Multi-Tiered Scraping Resilience (Zero-Failure Architecture)
Scraping LinkedIn via public APIs or actors requires multi-tier fallback architecture:
1. **Tier 1: Apify Actor Pipeline (`curious_coder/linkedin-jobs-scraper`):** High-volume structured JSON parser utilizing Apify Actor API with `publishedAt: "r86400"` (past 24-48 hours).
2. **Tier 2: Direct Guest Search API Fallback:** When Apify limits/credits expire (HTTP 403 `platform-feature-disabled`), the pipeline seamlessly falls back to the public LinkedIn Guest Jobs API endpoint:
   ```python
   # Endpoint for unauthenticated guest search (f_TPR=r86400 represents past 24h/past 2 days)
   url = f"https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={encoded_title}&location={encoded_loc}&f_TPR=r86400&start=0"
   ```
   Parses titles, company subtitles, locations, direct apply URLs, and timestamps with BeautifulSoup.

## 2. Daily 4:00 PM Cron Scheduling Standards
- **Schedule Expression:** `0 16 * * *` (Daily at 16:00 / 4:00 PM).
- **Execution Script:** Stored in `/data/job_search_supervisor.py`.
- **Telegram Delivery:** Script produces structured summary, latest PDF media path (`MEDIA:/data/project_job_scrapping/latest_scraped_jobs.pdf`), and latest JSON file.

## 3. Strict Candidate Data Anonymization Policy
- When directed to anonymize or remove names, scrub all PII from transcripts, memory entries, filenames, and resume headers.
- Standardize header to: `TARGET ROLE TITLE | SECONDARY ROLE TITLE` followed by `Location | Core Competency | Contact on Request`.
- Scrub all git commits and history of old name references.

## 4. Supabase Schema & Seed Script Automation
- The scraper automatically maintains an idempotent PostgreSQL seed script (`supabase_job_postings_seed.sql`) containing:
  ```sql
  CREATE TABLE IF NOT EXISTS public.job_postings (
      id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
      job_title TEXT NOT NULL,
      company_name TEXT,
      location TEXT,
      apply_url TEXT NOT NULL,
      match_score TEXT,
      relevance TEXT,
      posted_at TEXT,
      created_at TIMESTAMPTZ DEFAULT now()
  );
  ALTER TABLE public.job_postings ENABLE ROW LEVEL SECURITY;
  CREATE POLICY "Allow public read and insert on job_postings" 
  ON public.job_postings FOR ALL USING (true) WITH CHECK (true);
  ```
