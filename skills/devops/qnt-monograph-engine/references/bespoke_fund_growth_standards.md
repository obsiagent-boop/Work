# Bespoke Fund Data & Real Money Compounding Standards

## 1. Absolute Prohibition of Templated Boilerplate
- **Never reuse generic intro sentences:** Sentences like *"This analytical module establishes the mathematical, regulatory, and practical execution frameworks governing..."* destroy executive credibility.
- **Never reuse generic step-by-step lists:** Bullet points like *"1. Verification -> 2. Capital Allocation -> 3. Systematic Mandate -> 4. Dynamic Monitoring"* must NOT appear across all funds. Every instrument must specify its real-world portal route, specific NetBanking tab, eNPS registration path, or Demat order type.

## 2. Mandatory Real-Time Compounding Tables (5Y, 10Y, 15Y)
Every fund or scheme profile must include a dedicated table modeling exact rupee outcomes for three distinct saver profiles:

```html
<table class="growth-table">
  <thead>
    <tr>
      <th>Initial Principal Amount</th>
      <th>5-Year Corpus Value</th>
      <th>10-Year Corpus Value</th>
      <th>15-Year Corpus Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>₹1,000 (Small-Ticket Saver)</strong></td>
      <td><strong>₹[Val_5Y_1k]</strong></td>
      <td><strong>₹[Val_10Y_1k]</strong></td>
      <td><strong>₹[Val_15Y_1k]</strong></td>
    </tr>
    <tr>
      <td><strong>₹10,000 (Disciplined Accumulator)</strong></td>
      <td><strong>₹[Val_5Y_10k]</strong></td>
      <td><strong>₹[Val_10Y_10k]</strong></td>
      <td><strong>₹[Val_15Y_10k]</strong></td>
    </tr>
    <tr>
      <td><strong>₹1,00,000 (High-Conviction Lump-Sum)</strong></td>
      <td><strong>₹[Val_5Y_1L]</strong></td>
      <td><strong>₹[Val_10Y_1L]</strong></td>
      <td><strong>₹[Val_15Y_1L]</strong></td>
    </tr>
  </tbody>
</table>
```

## 3. Structural Risk & Lock-In Warning Boxes
Every asset must carry an explicit risk warning:
```html
<div class="risk-box">
  <strong>⚠️ CRITICAL RISKS, LOCK-IN &amp; FAILURE MODES:</strong> [Exact penalty clauses, lock-in duration, market volatility thresholds, and tax liabilities]
</div>
```

## 4. Subject-Specific Onboarding & Portal Linking
```html
<div class="access-box">
  <strong>🌐 OFFICIAL ACCESS PORTAL:</strong> <a href="[URL]">[URL]</a><br/>
  <strong>🚀 EXACT ONBOARDING PROCEDURE:</strong> [Exact menu clicks, KYC forms, and ticker symbols]
</div>
```
