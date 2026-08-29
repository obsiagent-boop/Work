# Dynamic Page Number Annotation & Clickable Index Architecture

## Purpose
Establishes the exact CSS Paged Media rules and table structures required to render dynamic, 100% accurate page number annotations in the Executive Index / Table of Contents of `qnt.` monographs using WeasyPrint.

## The Dynamic Page Annotation Mechanism
WeasyPrint supports CSS Generated Content for Paged Media (GCPM) `target-counter(attr(href), page)`. This allows the Table of Contents table to automatically resolve the exact compiled page number of target headings without manual hardcoding or guessing.

### CSS Implementation
```css
/* Master Index Table */
table.index-table {
  width: 100%;
  border-collapse: collapse;
  margin: 3.5px 0 4.5px 0;
  font-size: 6.5pt;
  background-color: #FFFFFF;
  border: 1px solid #000000;
}

table.index-table th {
  background-color: #000000;
  color: #FFFFFF;
  padding: 4px 6px;
  text-align: left;
  font-weight: 800;
  text-transform: uppercase;
  font-size: 6pt;
}

table.index-table td {
  padding: 3.2px 6px;
  border-bottom: 0.5px solid #CBD5E1;
  color: #0F172A;
}

/* Dynamically resolves target element page number */
td.page-num a::after {
  content: "Page " target-counter(attr(href), page);
  font-weight: 900;
  color: #000000;
  text-decoration: none;
}
```

### HTML Implementation
```html
<table class="index-table">
  <thead>
    <tr>
      <th>Section / Volume Description</th>
      <th>Instrument Scope &amp; Methodology</th>
      <th>Module Range</th>
      <th style="text-align: right;">Target Page</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="#sec-disclaimer"><strong>STATUTORY LEGAL DISCLAIMER</strong></a></td>
      <td>Impersonal Research Exemption (Lowe v. SEC / SEBI IA Regs 2013)</td>
      <td>Compliance Notice</td>
      <td class="page-num"><a href="#sec-disclaimer"></a></td>
    </tr>
    <tr>
      <td><a href="#sec-index"><strong>EXECUTIVE DIRECTORY &amp; FINCEPT MATRIX</strong></a></td>
      <td>Fincept Terminal 6-Desk Institutional Wealth Architecture</td>
      <td>Master Directory</td>
      <td class="page-num"><a href="#sec-index"></a></td>
    </tr>
    <tr>
      <td><a href="#vol-1"><strong>VOLUME I: SOVEREIGN POSTAL BEDROCK</strong></a></td>
      <td>PPF, SSY (8.2%), SCSS, POMIS, NSC, KVP, MSSC Schemes</td>
      <td>Modules 001–020</td>
      <td class="page-num"><a href="#vol-1"></a></td>
    </tr>
  </tbody>
</table>
```

## Key Rules
1. **Always pair IDs with target anchors:** Ensure volume titles contain `<div id="vol-1" class="volume-header">...</div>`.
2. **Right-align the page numbers:** Place page number targets in a dedicated column for clean executive presentation.
3. **Preserve Clickable Navigation:** Both the title and the page number remain clickable PDF hyperlinks for the user.
