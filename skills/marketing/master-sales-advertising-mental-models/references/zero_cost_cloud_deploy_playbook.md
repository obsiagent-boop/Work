# Zero-Cost Production Deployment & Free Backend Playbook

## Overview
A zero-friction, $0.00 forever architecture for deploying static SaaS applications, custom landing pages, and institutional tools with free domains, automated lead routing, and serverless databases without Git complexity or cloud hosting bills.

---

## 1. 10-Second Drag-and-Drop Global Hosting (100% Free)

### A. Cloudflare Pages (Recommended - Global Edge CDN)
- **Direct Upload:** Go to Cloudflare Dashboard ──► **Workers & Pages** ──► **Create Application** ──► **Pages** ──► **Upload assets**.
- **Worker/Project Name:** Enter custom brand name (e.g. `qnt-terminal` ──► generates `https://qnt-terminal.pages.dev` or `https://qnt-terminal.obsi-agent...workers.dev`).
- **Assets Directory:** `/` (Root directory containing `index.html` and assets).
- **HTML Handling:** `auto-trailing-slash`.
- **Not Found Handling:** `none` or `single-page-application`.
- **Free Quotas:** Unlimited bandwidth, 300+ global edge locations, sub-50ms TTFB, automated SSL.

### B. Netlify Drop (Zero Signup Instant Preview)
- Open `https://app.netlify.com/drop`
- Drag folder/zip directly into the browser box.
- Generates live instant public preview in <5 seconds.

---

## 2. Zero-Cost Serverless Backend & Lead Capture

### A. FormSubmit.co (Zero-Code Form Routing)
- Embed directly into HTML `<form>` tags without backend server code or API keys:
```html
<form action="https://formsubmit.co/obsi.agent@gmail.com" method="POST">
  <input type="hidden" name="_subject" value="New Enterprise Commission / Sponsorship">
  <input type="hidden" name="_captcha" value="false">
  <input type="text" name="name" required placeholder="Your Name">
  <input type="email" name="email" required placeholder="Your Email">
  <textarea name="message" required placeholder="Project Details"></textarea>
  <button type="submit">Submit Request</button>
</form>
```
- First submission sends a 1-click confirmation email to activate the route. Subsequent leads land directly in the inbox.

### B. Supabase Free Tier (PostgreSQL Database & Auth)
- 500MB PostgreSQL Database, 50,000 monthly active users, REST and GraphQL APIs free forever.
- Connect via official browser CDN bundle (`@supabase/supabase-js`) for direct client-side insertions.

---

## 3. Free Professional Business Email Setup

### A. Cloudflare Email Routing (Instant Direct Forwarding)
- In Cloudflare Dashboard ──► select domain/Pages project ──► **Email Routing**.
- Create custom aliases (e.g. `founder@yourbrand.pages.dev`, `contact@...`).
- Route directly to personal Gmail with zero mail server maintenance.

### B. Zoho Mail "Forever Free" Plan (Full Webmail & Mobile App)
- Go to `zoho.com/mail` ──► select **Forever Free Plan**.
- Connect up to 5 user inboxes with 5GB free storage per account.
- Ad-free webmail interface and native iOS/Android mobile apps.

---

## 4. User Workflow Pitfalls & Best Practices
1. **Never Force Complex CLI Git Workflows When User Wants Visual Guidance:** If a user encounters GitHub token scope rejections (e.g. `workflow` scope missing) or expresses difficulty navigating Git branches, pivot immediately to Direct Drag-and-Drop deployment (Cloudflare Pages zip / Netlify Drop) to achieve instant production results.
2. **Pre-Package Deployment Zips:** Always build self-contained `.zip` archives containing the complete HTML, assets, and compiled PDF monographs for single-click drag-and-drop.
3. **Inspect Dashboard Screenshots Visually:** When the user shares mobile/desktop dashboard screenshots, inspect project names, asset directory paths, and form handlers with precision before directing them to hit "Deploy".
