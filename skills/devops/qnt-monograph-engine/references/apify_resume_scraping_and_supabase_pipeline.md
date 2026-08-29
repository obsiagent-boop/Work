# Apify Agentic Scraping, Resume Matching & Supabase Job Pipeline

## Overview
This reference outlines the architecture and execution parameters for automated, agentic job scraping using Apify actors (LinkedIn Jobs Scraper), resume vector matching, and Supabase cloud database synchronization.

## Pipeline Architecture
1. **Apify Actor Execution:**
   - Actor: `curious_coder/linkedin-jobs-scraper` (or `valig/linkedin-jobs-scraper`).
   - Authentication: Bearer token passed in headers (`Authorization: Bearer <APIFY_TOKEN>`).
   - Search Query Formulation: Multi-keyword boolean queries targeting specific candidate titles (e.g. `Customer Support Team Lead OR Operations Lead OR Operations Manager OR Quality Lead`).
   - Time-Bounded Filtering: Use `publishedAt: "r86400"` for past 24-48 hours.
   - Location Targeting: Specific municipal metro parameters (e.g. `Hyderabad, Telangana, India`, `Mumbai, Maharashtra, India`, `Bengaluru, Karnataka, India`).
2. **Resume Profile Matching & Telemetry:**
   - Parse candidate `.docx` / `.pdf` resume using `read_file` or `pypdf`.
   - Score relevance against:
     - Management / Leadership tier (Lead, Manager, Supervisor).
     - Domain alignment (Operations, Support, CX, Risk, QA).
     - Methodology fit (Agile, Scrum, Salesforce, RCA).
3. **Database Sync & Reporting:**
   - Format results into clean JSON dictionaries.
   - Insert records into Supabase PostgreSQL tables (`job_postings`).
   - Render executive, luxury-cream PDF reports with direct apply links and match scores.

## Verified Apify Endpoints
- Base Run URL: `https://api.apify.com/v2/acts/<actor_id>/runs?waitForFinish=120`
- Dataset Fetch URL: `https://api.apify.com/v2/datasets/<dataset_id>/items?limit=100`
