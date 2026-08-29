# Zero-Cost Production Web & Edge Deployment Playbook

## 1. Zero-Cost Static & Edge Hosting with Cloudflare Pages API
When deploying client web apps without manual git/dashboard steps, use Cloudflare's direct API via `wrangler`:
```bash
export CLOUDFLARE_API_TOKEN="<token>"
export CLOUDFLARE_ACCOUNT_ID="<account_id>"

# 1. Initialize project
npx wrangler pages project create <project-name> --production-branch master

# 2. Deploy directory
npx wrangler pages deploy <directory_path> --project-name <project-name> --branch master
```

## 2. Zero-Cost Backend Form Endpoints (FormSubmit.co)
Eliminate server maintenance and backend costs by using pre-configured static form targets:
```html
<form action="https://formsubmit.co/obsi.agent@gmail.com" method="POST">
  <input type="hidden" name="_subject" value="New Client Lead / Commission">
  <input type="hidden" name="_captcha" value="false">
  <input type="text" name="name" required placeholder="Name">
  <input type="email" name="email" required placeholder="Email">
  <textarea name="message" required placeholder="Project Brief"></textarea>
  <button type="submit">Submit Request</button>
</form>
```

## 3. Zero-Cost Custom Business Email Routing (Zoho + Cloudflare)
1. **Cloudflare Email Routing:** Under `dash.cloudflare.com` ──► `Email Routing`, set custom domain aliases (`contact@...`, `founder@...`) to forward directly to destination Gmail for $0.
2. **Zoho Mail Forever Free Plan:** Connect custom domain to Zoho free tier for up to 5 dedicated 5GB inboxes with webmail and mobile apps.
