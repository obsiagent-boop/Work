# Zero-Cost Serverless Backends & Form Routing for Static Sites

When deploying static websites (GitHub Pages, Netlify Drop, Cloudflare Pages, Vercel) without a dedicated VPS or server subscription ($0.00 infrastructure), use these pre-wired backend integrations:

## 1. FormSubmit.co (Instant Zero-Code Email Routing)
- **Use Case:** Lead capture, sponsorship inquiries, client consultation bookings.
- **Integration:** Set the HTML form action directly:
  ```html
  <form action="https://formsubmit.co/your-email@domain.com" method="POST">
    <input type="hidden" name="_subject" value="New Lead Submission">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" required>
    <input type="email" name="email" required>
    <button type="submit">Submit</button>
  </form>
  ```
- **Key Features:** Zero account creation required, automated spam filtering, instant notification delivery.

## 2. Supabase (Free PostgreSQL & Authentication)
- **Use Case:** Relational data storage, user accounts, structured tables.
- **Free Tier:** 500 MB PostgreSQL database, 50,000 monthly active users, REST & GraphQL APIs.
- **Client-Side CDN:**
  ```html
  <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
  <script>
    const supabase = supabase.createClient('https://xyz.supabase.co', 'public-anon-key');
    async function insertLead(data) {
      const { error } = await supabase.from('leads').insert([data]);
    }
  </script>
  ```

## 3. Cloudflare D1 + Workers (Global Serverless SQL)
- **Use Case:** High-throughput transactional data, rate-limiting, and webhook processing.
- **Free Tier:** 100,000 requests/day, 5 GB storage, global edge execution.

## 4. Notion API & Airtable (No-Code Lead CRM)
- **Use Case:** Direct sync of form entries into visual client tracking databases without custom dashboards.
