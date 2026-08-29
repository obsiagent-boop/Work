# Fincept Terminal 5-Lab Deep Quantitative Analytical Architecture

This reference document outlines the exact mathematical frameworks and plain-English intuitive analogies extracted from Fincept Terminal (`/data/FinceptTerminal/`) and infused into `qnt. Quantitative Wealth Systems` for Indian and global market investors.

---

### 🔬 Quant Lab 1: Multi-Factor Alpha Engine & Fama-French 5-Factor Modeling

* **Core Equation:**
  $$R_i - R_f = \alpha_i + \beta_1(R_m - R_f) + \beta_2(\text{SMB}) + \beta_3(\text{HML}) + \beta_4(\text{RMW}) + \beta_5(\text{CMA}) + \epsilon_i$$
* **The 5 Factors:**
  1. **Market Beta ($R_m - R_f$):** General equity market excess return.
  2. **Size Factor (SMB - Small Minus Big):** Small-cap historical risk premium.
  3. **Value Factor (HML - High Minus Low Book-to-Market):** Undervalued asset margin of safety.
  4. **Robust Profitability (RMW):** Operating profitability alpha.
  5. **Conservative Investment (CMA):** Capital expenditure discipline.
* **5-Year-Old Intuition:** Picking cricket team players based on 5 exact superpowers: Speed (Momentum), Experience (Quality), Affordability (Value), Reliability (Low Volatility), and Potential (Size). Combining all 5 guarantees winning across all seasons.
* **Indian Equity Application:** The Nifty 200 Momentum 30 Index systematically captures +4.5% annualized alpha over the Nifty 50 by overweighting top-decile earnings acceleration leaders and cutting losing stocks.

---

### 🔬 Quant Lab 2: Options Greeks, Volatility Surfaces & Theta Decay Physics

* **Black-Scholes Differential Matrix:**
  * **Delta ($\Delta$):** $\frac{\partial V}{\partial S}$ — Rate of change of option price per ₹1 move in the underlying stock.
  * **Gamma ($\Gamma$):** $\frac{\partial^2 V}{\partial S^2}$ — Curvature of risk / acceleration of Delta.
  * **Theta ($\Theta$):** $\frac{\partial V}{\partial t}$ — The daily time decay clock bleeding option value into the seller's account.
  * **Vega ($\nu$):** $\frac{\partial V}{\partial \sigma}$ — Sensitivity to Implied Volatility spikes during market panic.
* **5-Year-Old Intuition:** Collecting monthly rent on stocks you own just like renting out an empty apartment.
* **The Systematic Harvesting Strategy:** Selling 1-month 5%–7% Out-of-the-Money (OTM) Covered Calls against underlying Demat blue chips (Reliance, TCS, HDFC Bank) to harvest positive Theta ($\Theta > 0$), capturing an automated 8.0% to 14.0% annualized cashflow yield.

---

### 🔬 Quant Lab 3: Discounted Cash Flow (DCF), Reverse DCF & ROIC Moats

* **Intrinsic Valuation Equation:**
  $$\text{Intrinsic Value} = \sum_{t=1}^n \frac{\text{FCFF}_t}{(1 + \text{WACC})^t} + \frac{\text{Terminal Value}}{(1 + \text{WACC})^n}$$
* **Reverse DCF (Expectations Investing):** Calculates the exact revenue growth rate priced in by the current market stock price. If the market prices in 20% growth but the monopoly can easily deliver 30% growth, a high Margin of Safety exists.
* **Economic Moat Spread:** Real shareholder value is created only when Return on Invested Capital (ROIC) exceeds Weighted Average Cost of Capital (WACC): $\text{Spread} = \text{ROIC} - \text{WACC} > 0$.

---

### 🔬 Quant Lab 4: Macroeconomic Regimes & Sovereign Yield Curves

* **The 4 Economic Quadrants (Growth vs. Inflation):**
  1. *Quadrant 1 (Goldilocks: Growth Up, Inflation Down):* Overweight Growth Equities & Small Caps.
  2. *Quadrant 2 (Reflation: Growth Up, Inflation Up):* Overweight Commodities, Commercial REITs & Energy.
  3. *Quadrant 3 (Stagflation: Growth Down, Inflation Up):* Overweight Sovereign Gold Bonds (SGB) & Cash.
  4. *Quadrant 4 (Deflationary Recession: Growth Down, Inflation Down):* Overweight Long-Duration Sovereign G-Secs (10Y/30Y Gilts).
* **Yield Curve Inversion Warning:** Short-term yields exceeding long-term benchmark yields signals institutional credit tightness and impending economic contraction.

---

### 🔬 Quant Lab 5: Modern Portfolio Theory (MPT) & Efficient Frontier

* **Portfolio Variance Equation:**
  $$\sigma_p = \sqrt{w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2w_1 w_2 \text{Cov}(R_1, R_2)}$$
* **Nobel Discovery:** Combining assets with low or negative correlation ($\rho < 0.20$) mathematically eliminates idiosyncratic risk without lowering expected returns.
* **The qnt. Optimal Tangent Portfolio:** Indian Equities ($\rho = +1.0$), US Tech ($\rho = +0.38$), Sovereign Debt ($\rho = -0.12$), and Gold ($\rho = -0.08$) constructs an impenetrable portfolio along the maximum Sharpe tangent line.
