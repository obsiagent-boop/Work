# In-Situ Deep Cognitive Definitions & Full 10-Volume Index Architecture

## Purpose
Establishes the strict design and engineering standards for:
1. Explaining who cognitive authors are and what their mental models mean directly on-page in every single module.
2. Guaranteeing that the Master Executive Index resolves 100% of volume page numbers with zero blanks.

---

## 1. Explicit Cognitive Mental Model Structure

Every single instrument card MUST embed the `🧠 12-BOOK COGNITIVE MENTAL MODEL MATRIX` box with full context:

* **Eliyahu Goldratt's Theory of Constraints / Bottleneck Removal (*The Goal*):**
  * *Meaning:* A system's output is governed entirely by its single greatest bottleneck.
  * *Application:* In investing, the primary bottlenecks are high expense ratios (TER) and annual tax friction. Sovereign and direct-growth funds remove both constraints.
* **Nassim Nicholas Taleb's Antifragile Barbell (*Antifragile*):**
  * *Meaning:* Eliminating vulnerability by pairing 85% hyper-safe bedrock with 15% convex upside bets.
  * *Application:* Guarantees zero ruin risk while capturing compounding market alpha.
* **Charlie Munger's Inversion Principle (*Poor Charlie's Almanack*):**
  * *Meaning:* Solving problems backwards by identifying and avoiding failure modes.
  * *Application:* Eliminating capital loss, liquidity traps, and tax clawbacks.
* **Donella Meadows' Stocks & Flows (*Thinking in Systems*):**
  * *Meaning:* Wealth accumulates when reservoirs are sealed and steady inflows are maintained.
  * *Application:* Designing cashflow waterfalls and automated paycheck sweeps.
* **John C. Hull's Theta Greeks Decay (*Options, Futures & Derivatives*):**
  * *Meaning:* Time value of options decays daily, putting non-refundable cash in the seller's account.
  * *Application:* Covered call synthetic rent strategies.
* **Prof. Aswath Damodaran's DCF & ROIC Spread (*Investment Valuation*):**
  * *Meaning:* True value is driven by free cash flows and Return on Invested Capital exceeding the cost of capital.
  * *Application:* Evaluating business moats and REIT distribution yields.

---

## 2. Table of Contents Anchor Resolution Protocol

To prevent WeasyPrint from rendering blank "Page" entries in the Master Executive Index:

1. **Volume Anchor ID Contract:** Every volume container in the HTML body MUST be assigned a strict sequential ID:
   ```html
   <div id="vol-1" class="volume-header">VOLUME I: ...</div>
   <div id="vol-2" class="volume-header">VOLUME II: ...</div>
   ...
   <div id="vol-10" class="volume-header">VOLUME X: ...</div>
   ```
2. **Index Table Target Counter:** The table of contents rows MUST match these anchor links:
   ```html
   <td class="page-num"><a href="#vol-1"></a></td>
   <td class="page-num"><a href="#vol-6"></a></td>
   ```
3. **CSS Target Counter Rule:**
   ```css
   td.page-num a::after {
     content: "Page " target-counter(attr(href), page);
     font-weight: 900;
     color: #000000;
     text-decoration: none;
   }
   ```
