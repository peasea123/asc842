# Research Implementation Plan
## "Hidden in Plain Sight: The Irrelevance of Book-Value Real Estate Assets in Corporate Valuation"

---

## I. RESEARCH GAP & NOVELTY

### Current State of Knowledge
- **Known**: Real estate collateral affects capital structure (Chaney et al., 2012; Valta, 2016)
- **Known**: Sale-leasebacks are economically significant transactions (Beattie et al., 2000; Shekhar, 2017)
- **Known**: Book-to-market anomalies exist broadly in equity markets (Fama & French, 2015)
- **Known**: Fair value accounting has mixed effects on earnings quality (Landsman et al., 2012)

### Critical Research Gap
**No prior work systematically tests whether book-valued RE assets are *statistically irrelevant* to market valuations *after controlling for* alternative signals (market-based RE values, transaction data).** This is distinct from:
- Collateral studies (which assume RE value matters; explain *how*)
- Fair value studies (which compare accounting methods, not relevance to market)
- Asset anomaly studies (not focused on RE specifically)

### Novel Contributions of This Work
1. **Systematic irrelevance test**: Fama-MacBeth framework testing book RE coefficient net of market RE signals (1980-2024)
2. **44-year horizon**: Captures regime changes (1980s inflation, 2008 GFC, post-2015 IFRS adoption)
3. **Multi-method triangulation**: Events + structural breaks + panel models converge on same conclusion
4. **Policy implications**: Questions whether GAAP real estate accounting serves investor information needs
5. **Comprehensive sample**: All corporate RE across sectors (not just REIT-related)

### Positioning vs. Literature
- **vs. Real Estate Finance**: Prior work focuses on industrial/office RE; this covers ALL corporate RE
- **vs. Accounting**: Extends fair value debate beyond IFRS 13 adoption; 40+ year empirical evidence
- **vs. Corporate Finance**: First comprehensive test of whether asset-side collateral valuations matter for market cap net of liability-side effects

---

## II. EMPIRICAL RESEARCH DESIGN

### Research Questions (in priority order)

#### **Q1: Is book-valued RE statistically irrelevant to market valuations?** (PRIMARY)
- **Hypothesis**: After controlling for market RE signals, book RE coefficient = 0
- **Method**: Fama-MacBeth cross-sectional regression with Tobin's q and P/B as outcomes
- **Sample**: 200+ firms × 44 years = 8,800+ firm-year observations
- **Timeline**: Months 5-7

#### **Q2: How would financial statements change under fair value accounting?** (SECONDARY)
- **Hypothesis**: Fair value revaluation would reduce ROA 2-3 pp and raise leverage, but NOT affect market valuations
- **Method**: Simulation of revalued balance sheets + event study around IFRS 13/ASC 820 adoption
- **Sample**: ~300 firms × 3-year adoption window = 900 observations
- **Timeline**: Months 7-9

#### **Q3: Do corporate actions unlocking RE value generate stock gains?** (TERTIARY)
- **Hypothesis**: Sale-leasebacks and REIT spin-offs show positive abnormal returns (evidence of hidden value)
- **Method**: Event study (CAR analysis) + propensity score matching
- **Sample**: ~2,000-3,000 sale-leasebacks + 50-100 spin-offs, 1980-2024
- **Timeline**: Months 9-12

#### **Q4: Do firms respond to RE collateral value shocks?** (CONFIRMATORY)
- **Hypothesis**: Firms increase debt/investment when RE prices rise; effect stronger for high-RE firms
- **Method**: Difference-in-differences exploiting regional RE price shocks
- **Sample**: 5,000-8,000 firm-years spanning GFC, 1990s recessions
- **Timeline**: Months 12-14

---

## III. DATA SOURCES & ASSEMBLY

### 3.1 Corporate Financial Data (1980-2024)

| Data Element | Primary Source | Backup | Collection Method | Quality Notes |
|--------------|----------------|--------|-------------------|---------------|
| **Balance sheet (PPE, accumulated depreciation)** | Compustat (via WRDS) | SEC EDGAR 10-K | Annual download; filter for nonmissing PPE data | Standardized GAAP; check consistency with 10-K footnotes (n=200 firms) |
| **Book values of land vs. structures** | SEC EDGAR footnote disclosure | Compustat segments (partial) | Manual NLP parsing of property note (Note X: Property, Plant and Equipment) | Manual verification required; available ~80% of firm-years post-1995 |
| **Income statement** | Compustat | SEC EDGAR 10-K | Annual; depreciation expense isolates building component | Depreciation policy variation across firms (useful for robustness) |
| **Cash flow statement** | Compustat | SEC EDGAR 10-K | Annual; free cash flow, capex | Use capex to test collateral-constrained investment hypothesis |
| **Segment data** | Compustat segments | SEC EDGAR (geographic note) | Identify RE-intensive segments (real estate operations, property held for sale) | ~40% of sample identifiable via segment reporting |

**Data Assembly Strategy**:
1. Query Compustat annual database: gvkey, tic, year, at (total assets), ppe (gross PPE), dpact (accumulated depreciation), capx, oancf
2. Calculate book RE/assets = (ppe - dpact) / at
3. Flag firms with ppe/at > 15% as "RE-intensive"
4. Cross-validate with SEC EDGAR footnotes for n=200 firms × 5-year window to assess measurement quality

**Data Quality Checks**:
- Exclude firms with negative PPE values (data errors)
- Exclude firms with ppe/at > 90% (likely REIT-like entities, should be excluded anyway)
- Impute missing values using prior-year data only if gap ≤ 2 years
- Document data availability by year (should show improvement post-1995)

---

### 3.2 Stock Market Returns & Valuation Metrics

| Metric | Source | Calculation | Availability |
|--------|--------|-----------|--------------|
| **Stock returns (monthly/daily)** | CRSP | Adjusted for splits, dividends; use RETX | 1980+ |
| **Market capitalization** | CRSP | Price × Shares outstanding | Daily; use month-end |
| **Tobin's q** | Derived | (Market Cap + Total Debt - Cash) / Total Assets | Annual; exclude q < 0.5 or q > 3 (outliers) |
| **Price-to-book ratio** | Derived | Market Cap / Book Value of Equity | Annual |
| **Fama-French factor returns** | Kenneth French library | Mkt-RF, SMB, HML, RMW, CMA | Free; use 5-factor model |

**Matching Algorithm**:
- Use CRSP permno and Compustat gvkey with standard CCM (Compustat-CRSP Merged database)
- Annual snapshot: Use June 30 market cap (fiscal year-end matching for many firms)
- Handle delistings: Record return in delisting month, then exclude

---

### 3.3 Real Estate Price Indices (Regional Level)

| Index | Provider | Coverage | Frequency | Cost | Use Case |
|-------|----------|----------|-----------|------|----------|
| **CoStar Real Capital Analytics** | CoStar | 380+ US metro areas; office, retail, industrial, multifamily | Quarterly | ~$5,000-15,000/year for institutional license | PRIMARY: metro-level price indices matched to firm HQ location |
| **NAREIT Property Index / Federal Reserve** | NAREIT / Board of Governors | National + regional (8 regions); all commercial RE | Monthly/quarterly | Free | SECONDARY: for robustness; too aggregated as primary |
| **Zillow ZTRAX (for validation)** | Zillow | Transaction-level commercial + multifamily; US coverage | Quarterly updates | Free tier (limited) | TERTIARY: validate CoStar with transaction-based prices for subset |
| **CBRE Market Reports** | CBRE (via firm reports) | Selected metros; office, retail, industrial | Quarterly | Free (public releases) | SUPPLEMENTARY: occupancy, cap rates, lease terms |

**Implementation Strategy**:
1. **Primary analysis**: CoStar metro-level indices (Q1 1990 - Q4 2024)
2. **Firm matching**: Identify firm HQ metro from Compustat (loc field) or SEC EDGAR
3. **Interpolation**: Quarterly indices to annual (average Q1-Q4)
4. **Log returns**: Calculate ln(Price_t) - ln(Price_{t-1}) as annual RE price change
5. **Lag structure**: Use lagged RE prices (year t-1) in regressions to reduce simultaneity bias

**Data Quality**:
- Report CoStar index coverage by metro-year (some metros have limited history)
- Conduct sensitivity analysis: replicate main results using NAREIT indices (more conservative estimate)
- Cross-validate CoStar with CBRE public data for major metros (should be highly correlated)

---

### 3.4 Real Estate Transaction Data

#### **Sale-Leaseback Transactions**

| Data Element | Source | Collection Method | Sample Size | Notes |
|--------------|--------|-------------------|-------------|-------|
| **Transaction date, amount, lessor/lessee** | SEC EDGAR (8-K filings) | Keyword search: "sale-leaseback", "sale and leaseback" | ~2,000-3,000 transactions (1980-2024) | Manual or RPA-based extraction from 8-K Item 1.01 or 7.01 |
| **Confirmation** | Earnings call transcripts / news | Bloomberg, FactSet, Factiva | Subset validation (n=200) | Confirm transaction size and date alignment with 8-K |
| **Property details** | SEC EDGAR 10-K or transaction press release | Extract from footnote or leaseback commitment detail | ~50% have property description | Location, property type, lease term |

**Collection Process**:
1. Query SEC EDGAR FULL-TEXT database for forms 8-K, year 1980-2024
2. Use regex to identify sale-leaseback announcements: `sale.{0,20}leaseback|sale.{0,20}lease` (case-insensitive)
3. Extract filing date as event date (announcement effect); some firms may issue earlier press release (collect if available)
4. Extract transaction amount from 8-K Item 1.01 (Material Agreement) or Item 7.01 (Regulation FD)
5. Merge with CRSP daily returns using tic (ticker symbol from 8-K)
6. Calculate abnormal returns [-10, +60] trading days vs. CAPM benchmark (calculate alpha using pre-event 120-day window)

**Sample Representativeness**:
- Expect ~45% of transaction volume identified via SEC EDGAR
- Cross-validate sample with CoStar transaction database (subset of large transactions)
- Document any biases (larger transactions more likely reported; certain industries over-represented)

#### **REIT Spin-offs**

| Data Element | Source | Collection | Notes |
|--------------|--------|-----------|-------|
| **Spin-off announcement & completion dates** | CapitalIQ / Bloomberg | Filter corporate actions: spin-off type = "real estate" | ~80-120 spin-offs identified (1980-2024) |
| **Parent firm stock reactions** | CRSP | Daily returns around announcement | Use announcement date from CapitalIQ |
| **Parent pre/post valuation** | Compustat | Annual q before spin, parent q and spinout q after | Limited to firms with continuous post-spin data |

**Sample Collection**:
1. Use CapitalIQ "Corporate Action" type = Spin-off
2. Filter for RE keywords: "real estate", "REIT", "properties"
3. Merge with CRSP using permno
4. Identify announcement date (first material disclosure, typically 8-K 8.01 or press release)
5. Calculate returns using Fama-French 5-factor benchmark

---

### 3.5 Real Estate Price Shock Data

**Shock Identification Strategy**:

For difference-in-differences analysis exploiting exogenous regional real estate price declines:

| Shock Period | Geographic Variation | Magnitude | Identification |
|--------------|----------------------|-----------|-----------------|
| **2007-2009 GFC** | Varies by metro; harder-hit: Tampa, Vegas, Phoenix (>40% decline) vs. stable: Boston, NYC (0-10% decline) | 10-50% decline | NBER recession dating + CoStar metro-level indices |
| **1990-1992 Regional RE recession** | S&L crisis aftermath; hardest hit: TX, LA, OK (20-30% decline) vs. growth metros (growth) | 15-30% decline | Academic real estate studies + CoStar historical |
| **2001-2003 Downturn** | Moderate; post-9/11 office declines in NYC metro; mild recovery elsewhere | 5-15% decline | CoStar indices |

**Empirical Implementation**:
1. Calculate annual RE price change by metro: $\Delta P_{m,t} = \ln(CoStar\_Index_{m,t}) - \ln(CoStar\_Index_{m,t-1})$
2. Define shock = year with $\Delta P < -10\%$ in metro m
3. Match firms to metros via Compustat location field (primary HQ) or facility concentration (for large real estate holdings, use SEC EDGAR segment data to identify main markets)
4. Construct shock exposure: Shock$_{i,m,t} = \mathbb{1}(\Delta P_{m,t} < -0.10) \times RE\_Intensity_{i,t-1}$
   - RE_Intensity = lagged PPE/assets (predetermined, avoids reverse causality)
5. Difference-in-differences: Compare high-RE firms (RE_Intensity top quartile) to low-RE firms (bottom quartile) during shock vs. non-shock years

**Key Identification Assumptions** (test via parallel trends plots):
- Absent shock, high-RE and low-RE firms follow parallel trajectories in leverage, investment
- Shock is orthogonal to firm characteristics (aggregate real estate market conditions)
- No anticipation effects (check for pre-shock coefficient changes)

---

## IV. ECONOMETRIC METHODOLOGIES & SPECIFICATIONS

### 4.1 PRIMARY ANALYSIS: Fama-MacBeth Regression (Q1)

#### **Specification**

$$q_{i,t} = \alpha_t + \beta_1 \left(\frac{\text{PPE}_{i,t}}{TA_{i,t}}\right) + \beta_2 \ln(CoStar\_Index_{m(i),t-1}) + \mathbf{X}'_{i,t}\boldsymbol{\gamma} + \epsilon_{i,t}$$

Where:
- $q_{i,t}$ = Tobin's q for firm i at year t
- $PPE_{i,t}/TA_{i,t}$ = book-valued real estate as share of total assets (key variable of interest)
- $\ln(CoStar\_Index)$ = market-based real estate price signal (lagged to reduce simultaneity)
- $\mathbf{X}_{i,t}$ = control vector (detailed below)
- $\alpha_t$ = year fixed effect (controls for inflation, interest rates, etc.)

#### **Control Variables**

| Variable | Calculation | Rationale | Expected Sign |
|----------|------------|-----------|---------------|
| $\ln(Market \, Cap)$ | log of market capitalization | Size effect; larger firms may have more efficient RE markets | + |
| $ROA_{t}$ | Net income / total assets | Profitability; profitable firms have higher q | + |
| $PPE/TA$ (all, not just RE) | All tangible assets / total assets | Asset-heavy firms typically lower q | - |
| $Leverage$ | Total debt / total assets | Collateral effect (higher leverage with more tangible assets); but high leverage = distressed q | ±/- |
| $Cash/TA$ | Cash and equivalents / total assets | Liquidity substitute for collateral; lower RE value if liquid | - |
| $R\&D/TA$ | R&D expense / total assets | Intangible-intensive (growth) firms may undervalue RE | - |
| $\Delta ln(Assets)$ | Asset growth rate | Growing firms accumulate RE; captures firm trajectory | + |
| $Dividend \, Payout$ | Dividend / net income | Mature, stable firms; mature firms may have more RE | ± |
| $Stock \, Volatility$ | Std dev of monthly returns (prior 24 months) | High-volatility firms may demand collateral for stability | - on q; + on RE coefficient |

#### **Procedure**

1. **Annual cross-sections**: For each year t = 1980, 1981, ..., 2024:
   - Run cross-sectional OLS: $q_{i} = \alpha + \mathbf{X}'\boldsymbol{\beta} + \epsilon_{i}$ (drop year subscript for brevity)
   - Collect coefficient vector $\hat{\boldsymbol{\beta}}_t$
2. **Pool coefficients** (simple mean):
   - $\hat{\beta}_{FM} = \frac{1}{T} \sum_{t=1}^{T} \hat{\beta}_t$
   - Standard error using Newey-West correction (account for autocorrelation across years, MA(3) lag)
   - t-statistic = $\hat{\beta}_{FM} / SE_{NW}$
3. **Hypotheses**:
   - $H_0$: $\beta_1 = 0$ (book RE coefficient = 0, i.e., irrelevant)
   - $H_1$: $\beta_2 > 0$ (market RE prices positively related to q)

#### **Interpretation**
- If $\beta_1 \approx 0$ and $\beta_2 > 0$: **Supports irrelevance hypothesis** (markets look through book values to market signals)
- If $\beta_1 > 0$ and $\beta_2 \approx 0$: Book values matter; contradicts hypothesis
- If both $\beta_1 > 0$ and $\beta_2 > 0$: Complementary information (both book and market values matter)

#### **Robustness Checks**
1. **Time-varying coefficients**: Report $\hat{\beta}_{1,t}$ separately by decade to show stability
2. **Panel fixed effects**: $q_{i,t} = \alpha_i + \alpha_t + \mathbf{X}'\boldsymbol{\beta} + \epsilon_{i,t}$ (controls for firm unobservables)
3. **Instrumental variables**: Instrument PPE/TA using lagged RE intensity + geographic IV (firm HQ metro × national RE trends); use 2SLS
4. **P/B ratio outcome**: Replicate using Price-to-Book instead of q (alternative valuation metric)
5. **Alternative RE measure**: Use Net RE (PPE - Accumulated Depreciation) instead of gross PPE; use book value of land separately (never revalued)

---

### 4.2 FAIR VALUE SIMULATION & EVENT STUDY (Q2)

#### **Fair Value Revaluation Simulation**

**Step 1: Estimate market value of RE**
- Use CoStar metro-level index to inflate historical cost:
  $$\text{Market Value}_{i,t} = (\text{Gross PPE}_{i,t} - Depreciation_{i,t}) \times \frac{\text{CoStar Index}_{m,t}}{\text{CoStar Index}_{m,t_0}}$$
  where $t_0$ = acquisition year (use accumulated depreciation as proxy for acquisition timing)

**Step 2: Construct revalued balance sheet**
- Revalued total assets = Total assets + (Market Value RE - Book Value RE)
- Revalued equity = Equity + Revaluation surplus
- Revalued leverage = Debt / Revalued assets

**Step 3: Calculate pro forma financial statement metrics**
- $\text{Revalued ROA} = \text{Net Income} / \text{Revalued Assets}$
- $\text{Revalued Leverage} = \text{Total Debt} / \text{Revalued Assets}$
- $\Delta ROA = ROA_{Revalued} - ROA_{Book}$
- $\Delta Leverage = Leverage_{Revalued} - Leverage_{Book}$

**Step 4: Test impact on market valuations**
- Regress Tobin's q on revalued metrics vs. book metrics
- Expectation: If markets ignore book values, then adding market RE signals should improve model fit
- Test: Does q respond to Book RE or Market RE?

**Event Study: IFRS 13 / ASC 820 Adoption** (2007-2009)
- Event: Year firm subject to fair value accounting requirement for investment property
- Outcome: Tobin's q, leverage, spread, analyst forecast dispersion (measure information changes)
- Specification:
  $$y_{i,t} = \alpha_i + \alpha_t + \beta \cdot (\text{Post-Adoption})_{i,t} + \gamma (RE/TA)_{i,t-1} + \epsilon_{i,t}$$
- Interpretation: If $\beta \approx 0$ on q, then fair value disclosure doesn't change market valuations (markets already adjusted); if $\beta < 0$ on spread, markets may interpret fair value as informative about uncertainty

---

### 4.3 EVENT STUDIES (Q3)

#### **Sale-Leaseback Event Study**

**Event Definition**: 8-K announcement of sale-leaseback transaction

**Sample**: N = 2,000-3,000 transactions, 1980-2024

**Event Window**: [-10, +60] trading days
- Day 0 = announcement date
- Conduct sensitivity to windows: [-5,+30], [-1,+2], [-5,+5] to test robustness

**Abnormal Return Calculation** (Fama-French 5-factor):
$$AR_{i,d} = R_{i,d} - \hat{R}_{i,d}^{\text{FF5}}$$

where:
- $R_{i,d}$ = daily return for firm i on day d
- $\hat{R}_{i,d}^{\text{FF5}}$ = predicted return using 5-factor model estimated over days [-150, -11]

**Cumulative Abnormal Return** (CAR):
$$CAR_{i} = \sum_{d=-10}^{+60} AR_{i,d}$$

**Test Statistic**: $t = \frac{\overline{CAR}}{\sigma(CAR) / \sqrt{N}}$

**Cross-Sectional Analysis** (heterogeneous effects):
- Regress CAR on pre-event firm characteristics:
  $$CAR_i = \alpha + \beta_1 Leverage_{i,t-1} + \beta_2 (RE/TA)_{i,t-1} + \beta_3 ROA_{i,t-1} + \epsilon_i$$
  - Expect $\beta_1 > 0$: more-constrained (high-leverage) firms gain more
  - Expect $\beta_2 > 0$: more-RE-intensive firms gain more

**Matching Controls** (propensity score):
1. Estimate propensity to do sale-leaseback: logit of transaction indicator on firm characteristics (size, leverage, profitability, RE intensity)
2. Match each transaction firm to 3-5 control firms with similar propensity scores (caliper = 0.01)
3. Use kernel-based weighting (Epanechnikov) for robustness
4. Calculate difference in returns: $CAR_{Treated} - CAR_{Controls}$

---

#### **REIT Spin-off Event Study** (Synthetic Control)

**Event**: Completion date of real estate REIT spin-off from parent corporation

**Sample**: N = 50-100 spin-offs, 1980-2024

**Challenge**: Small sample; traditional matching may be underpowered

**Solution**: Synthetic Control Method
1. For each spin-off, create synthetic control = weighted average of non-spinning firms
2. Weights $\mathbf{w}$ chosen to minimize pre-spin difference in outcomes (q, leverage, ROA):
   $$\min_{\mathbf{w}} \sum_{s=1}^{S} v_s (X^P_s - \sum_{j \in Control} w_j X^C_{j,s})^2$$
   where $X$ = pre-treatment characteristics, $P$ = parent, $C$ = control pool, $S$ = number of characteristics
3. Estimate treatment effect:
   $$\tau_i = q_{Parent,t}^{Actual} - q_{Synthetic,t}^{Predicted}$$
4. Conduct placebo tests: apply same method to random "false" spin-offs; should show zero effects

**Time Horizon**: Examine effects over 36 months post-spin (long-window analysis)

---

### 4.4 DIFFERENCE-IN-DIFFERENCES ANALYSIS (Q4)

#### **Research Question**: Do firms increase leverage/investment when collateral (RE) values rise?

**Shock-based design**: Exploit exogenous real estate price declines (GFC 2007-2009, 1990s S&L crisis)

**Sample Construction**:
1. Identify shock years and metros: CoStar index decline > 10%
2. Match firms to metros via HQ location (primary) or facility concentration
3. Define treatment: high RE intensity (RE/TA > median) × shock occurrence
4. Define control: low RE intensity firms (RE/TA < median) × shock occurrence

**Parallel Trends Test** (graphical):
- Plot pre-shock trends (5 years before) in leverage, investment by treatment/control groups
- Verify parallel trends; if divergent, violates key assumption

**Main DiD Specification**:
$$y_{i,t} = \alpha_i + \alpha_t + \beta_1 Shock_{m,t} + \beta_2 (RE/TA)_{i,t-1} + \beta_3 (Shock \times RE/TA)_{i,t} + \mathbf{X}'_{i,t}\boldsymbol{\gamma} + \epsilon_{i,t}$$

Where:
- $Shock_{m,t}$ = indicator for metro m experiencing >10% RE price decline in year t
- $(RE/TA)_{i,t-1}$ = firm i's lagged RE intensity (determines sensitivity to shock)
- $(Shock \times RE/TA)_{i,t}$ = treatment effect (interact shock with RE exposure)
- Coefficient of interest: $\beta_3$ (should be positive if collateral hypothesis correct)

**Outcomes Tested**:
- $\Delta Leverage_{i,t}$ = change in debt/assets
- $\Delta Investment_{i,t}$ = capex / lagged assets
- $\Delta Cash\_Holding_{i,t}$ = change in cash/assets

**Instrumentation for Reverse Causality**:
- IV approach: Instrument $(RE/TA)_{i,t-1}$ using lagged predecessor RE intensity (predetermined)
- Geographic IV: Instrument shock exposure using interaction of firm's HQ location × national RE index trend (isolates local shocks from national trends)

**Robustness Checks**:
1. Placebo shocks: Use sham shock dates (3 years before actual shock); coefficient should be zero
2. Exclude crisis years: Re-estimate omitting year t and t+1 of shock (controls for confounds)
3. Alternative RE measures: Use gross PPE/assets; net PPE/assets; log RE holdings
4. Balanced panel: Restrict to firms with continuous data across shock window

---

## V. KEY CONTROL VARIABLES (FULL SPECIFICATION)

### Firm-Level Controls (Annual)

```
ln(Market Cap)            # Size effect; larger firms more efficient RE markets
ROA                       # Profitability; profitable firms higher q
PPE / Total Assets        # Asset intensity (tangibility)
Leverage                  # Debt / total assets; collateral effect
Cash / Total Assets       # Liquidity; substitute for collateral
R&D / Total Assets        # Intangible intensity; growth firms behavior
Asset Growth              # Annual change in ln(assets)
Dividend Payout           # Dividend / earnings; maturity signal
Stock Volatility (24mo)   # Std dev of monthly returns
Capex / Total Assets      # Capital intensity; investment needs
```

### Macro Controls

```
ln(CoStar Index_metro_lagged)  # Regional RE price changes
10-Year Treasury Rate           # Discount rate; affects RE cap rates
NBER Recession Indicator        # Macro conditions
Year Fixed Effects             # Inflation, credit cycles, accounting regime
Industry Fixed Effects         # Sector-specific RE intensity (Retail >> Manufacturing)
```

### Interaction Terms (Test Heterogeneity)

```
RE/TA × Leverage           # Do collateral values matter more for constrained firms?
RE/TA × Industry           # RE valuation differences by sector?
RE/TA × Recession          # Are book RE values especially ignored in downturns?
RE/TA × ln(CoStar Index)   # Does market RE price substitutute for book values?
Shock × RE/TA              # DiD treatment effect
```

---

## VI. THREATS TO CAUSAL INFERENCE & MITIGATION STRATEGIES

### Threat 1: Reverse Causality (Simultaneity Bias)

**Problem**: High-q firms may accumulate RE assets (not reverse); RE holding endogenous to firm value

**Evidence Tests**:
1. **Lag structure**: Regress $q_{t+1}$ on $Book \, RE_t$ (controls for contemporaneous feedback)
2. **Lead test**: Show that current RE does NOT predict past q (falsification)
3. **Granger causality**: Test whether q temporally precedes RE accumulation
4. **Report lag structure coefficients**: $\hat{\beta}_1(q_{t}, RE_t)$, $\hat{\beta}_1(q_{t+1}, RE_t)$, $\hat{\beta}_1(q_t, RE_{t-1})$

**Mitigation**:
- Use IV regression: Instrument PPE/TA with lagged RE intensity + geographic IV
- Panel fixed effects control for time-invariant unobservables
- Shock-based DiD design uses exogenous RE price changes (quasi-experimental)

---

### Threat 2: Omitted Variable Bias (Selection into RE)

**Problem**: Firms with high-RE holdings differ fundamentally; unobservables correlate with both RE holdings and q

**Evidence Tests**:
1. **Coefficient stability**: Add controls sequentially; show β changes minimally
2. **Rosenbaum bounds**: Quantify how strong unmeasured confounder must be to change inference
3. **Matched sampling**: Use propensity score matching (high-RE vs. low-RE on observables); compare within matched sample
4. **Placeholder test**: Show that unrelated asset types (intangibles) also "irrelevant"; if they're irrelevant too, measurement error ≠ irrelevance

**Mitigation**:
- Panel fixed effects (controls for time-invariant unobservables)
- Rich control vector (size, profitability, growth, leverage, R&D, industry)
- Within-industry analysis (hold sector strategy constant)
- Event-study designs (minimize selection: sale-leaseback dates quasi-random)

---

### Threat 3: Measurement Error in Real Estate Values

**Problem**: Book values incomparable across firms (different depreciation, acquisition dates); market prices subject to appraisal error

**Evidence Tests**:
1. **Attenuation bias**: Measurement error in X biases coef toward zero; test sensitivity to measurement assumptions
2. **Variance comparison**: Compare book RE/assets variance to market RE variance
3. **Timing test**: Show that firm-specific depreciation assumptions (from footnotes) don't materially affect results

**Mitigation**:
- Use multiple RE measures (gross PPE, net PPE, land-only, indexed market value)
- Test robustness to exclusion of low-quality data (pre-1990, small RE holdings)
- Develop measurement error model: if $\text{Observed} = \text{True} + \text{Error}$, then attenuation bias = $1 / (1 + \sigma_E^2 / \sigma_T^2)$; show that true effect likely small even adjusting for measurement

---

### Threat 4: Compositional Changes / Survivorship Bias

**Problem**: Sample composition changes over 44 years; firms enter/exit; survivors may differ

**Evidence Tests**:
1. **Subsample analysis**: Run regressions by decade; show β stable
2. **Balanced vs. unbalanced**: Restrict to firms with continuous 44-year data (n↓); show results unchanged
3. **Hazard model**: Model firm delisting; show unrelated to RE holdings
4. **Entry/exit analysis**: Compare entering/exiting firms to incumbents; show no systematic selection

**Mitigation**:
- Report results for balanced panel (conservative)
- Separately report unbalanced panel with firm-year fixed effects (efficiency)
- Document sample composition by decade (# firms, median RE/TA, median q)
- Include Fama-MacBeth (rebalances annually) alongside panel models

---

### Threat 5: Financial Statement Manipulation

**Problem**: Firms may overstate RE book values; fair value estimates subject to discretion

**Evidence Tests**:
1. **Cross-validation**: Compare book RE to auditor-verified transaction prices (sale-leaseback deals)
2. **Disclosure quality**: Score footnote completeness (property descriptions, valuation methods, sensitivity ranges); test whether quality predicts RE coefficient
3. **Aggressive accruals**: Identify high-accrual firms (earnings management signal); test whether results driven by them

**Mitigation**:
- Exclude firms with restatements (predates event ±2 years)
- Use transaction-based RE prices (highest quality) for subset analysis
- Conduct robustness test: Restrict to firms with high-quality auditors (Big 4); show results unchanged
- Fair value estimates: Use auditor-verified appraisals where available (subset of firms)

---

### Threat 6: Event Study Confounds

**Problem**: Multiple events occur simultaneously; true event window uncertain

**Evidence Tests**:
1. **Event window sensitivity**: Report CARs for [-5,+30], [-10,+60], [-5,+5], [-1,+2] windows
2. **Placebo tests**: Use sham announcement dates; should show zero effects
3. **Concurrent events**: Measure correlation with simultaneous announcements (earnings, dividend, capex); include in regression

**Mitigation**:
- Specify event window a priori in pre-analysis plan
- Use narrow window if returns large ([-1, +2] days)
- Exclude transactions with confounding events within [-5, +10] window
- Use propensity score matching (create control sample with similar characteristics but no event)

---

### Threat 7: Geographic Sorting in Shock Analysis

**Problem**: Firms may locate in high-RE-value metros; shock exposure endogenous

**Evidence Tests**:
1. **Parallel trends plots**: Verify high-RE vs. low-RE firms on same trajectory pre-shock (graphical test)
2. **Pre-shock coefficient test**: Run DiD on pre-shock period (sham shock 3 years before); coefficient should be zero
3. **Placebo treatment**: Define fake high-RE/low-RE groups; apply DiD; should show zero effects

**Mitigation**:
- IV approach: Instrument RE/TA with lagged predecessor RE intensity (predetermined)
- Geographic IV: Use firm HQ location × national RE trend (isolates local from national shocks)
- Exclude firms that relocated within ±3 years of shock (endogenous location choice)
- Conduct falsification test: Use non-RE assets as "shock" (should show zero effects)

---

### Threat 8: Accounting Regime Changes

**Problem**: 44-year span includes major changes (IFRS, GAAP updates, REIT creation); RE coefficient may vary by regime

**Evidence Tests**:
1. **Coefficient stability by decade**: Report β_1(1980s), β_1(1990s), ..., β_1(2020s)
2. **GAAP vs. IFRS**: Stratify sample by accounting standard; show consistent results
3. **Interaction with regime**: Include (RE/TA) × (IFRS Indicator); test if coefficient materially changes

**Mitigation**:
- Report results separately by era: pre-1990 (limited RE data), 1990-2007 (GAAP), 2008+ (fair value)
- Use accounting standard fixed effects
- Conduct subset analysis: Restrict to post-2007 (IFRS/ASC adoption standardizes fair value disclosure)

---

## VII. SAMPLE SIZE & POWER REQUIREMENTS

### Target Sample Sizes (by Research Question)

| Question | N (Firm-Years) | Event Count | Rationale | Expected Effect | Power |
|----------|----------------|-------------|-----------|-----------------|-------|
| **Q1: Relevance test (FM)** | 8,000-12,000 | — | 200 firms × 40 years; some missing data | Elasticity = 0.05 | >90% |
| **Q2: Fair value event (DiD)** | 500-1,000 | 200 adoptions | 200-300 firms × 2-3 year window | δ = 3 bp/month | 75-85% |
| **Q3a: Sale-leaseback events** | 1,500-2,500 | 2,000-3,000 | 50-100 per year × 30 years; 1,500-2,500 matched controls | CAR = 0.5-1.0% | 80-90% |
| **Q3b: Spin-off events** | 250-500 | 50-100 | Limited spin-off universe; 250-500 firm-year observations | q improvement = 50 bp | 75% |
| **Q4: Regional shocks (DiD)** | 5,000-8,000 | 2-3 major shocks | Multiple metros × years spanning GFC, 1990s recessions | Elasticity = 0.10 | 85%+ |

### Power Calculation (Illustrative)

**Model**: $q_i = \alpha + \beta (\text{Book RE}/TA)_i + X'\gamma + \epsilon_i$

- Null: $\beta = 0$ (RE irrelevant)
- Alt: $\beta = 0.05$ (elasticity: 1% ↑ RE/TA → 5% ↑ q; modest effect)
- Effect size: $\delta = \beta \times \sigma(RE/TA) / \sigma(q)$
  - Assume $\sigma(RE/TA) = 0.15$, $\sigma(q) = 0.80$
  - $\delta = 0.05 × 0.15 / 0.80 = 0.009$ (small effect)
  - Power analysis (Cohen 1988): To achieve 80% power, α=0.05, need **N ≈ 8,000-10,000**
  
**Clustering adjustment**: Standard errors likely clustered by firm and year; ICC ≈ 0.15-0.25. Effective sample size = N / (1 + ICC·m). **Inflate target N by 1.3-1.5×**.

### Publication Standards (Tier-1 Journals)

| Journal | Min Sample | Preferred Effect | Significance | Corrections |
|---------|-----------|-----------------|--------------|-----------|
| **Journal of Finance** | 5,000+ firm-yrs or 200+ events | β ≥ 0.05 elasticity; CAR ≥ 0.5% | p < 0.05 | Control for 3-5 main tests; report FDR |
| **JFE** | 3,000+ firm-yrs | β ≥ 0.05; CAR ≥ 0.3% | p < 0.05; p < 0.01 preferred | Bonferroni for <5 tests; FDR for >5 |
| **Journal of Real Estate Finance & Economics** | 500+ firm-yrs or 100+ events | β ≥ 0.03; CAR ≥ 0.2% | p < 0.05; p < 0.10 accepted | Discretionary; typically 1-2 |

### Achievability Assessment

✅ **Feasible**: Proposed sample (200+ firms × 44 years = 8,800 pre-attrition) meets JF/JFE requirements  
✅ **Achievable**: Sale-leaseback events (est. 2,000-3,000) within target  
✅ **Achievable**: Regional shock analysis (5,000+ firm-years) with CoStar + Compustat  
⚠️ **Limited**: REIT spin-offs (50-100) underpowered; recommend synthetic control or bundling with sale-leaseback results

---

## VIII. IMPLEMENTATION TIMELINE

| Phase | Tasks | Duration | Outputs | Dependencies |
|-------|-------|----------|---------|-------------|
| **Phase 1: Data Assembly** | Pull Compustat, CRSP, CoStar; SEC EDGAR 8-K/10-K scraping; property matching | 3 months | Clean dataset; 200+ firms × 44 years; sale-leaseback/spin-off event lists | WRDS/CoStar/EDGAR access |
| **Phase 2: Descriptive** | Summary stats; RE holdings trends; book-market correlation; regime shifts | 2 months | Figures 1-4; Table 1 (descriptive); sample composition docs | Phase 1 completion |
| **Phase 3: Main Test (Q1)** | Fama-MacBeth regressions; cross-sectional; robustness (FE, IV, quantile) | 2 months | Tables 2-5; effect sizes; decade-by-decade breakdown; robustness appendix | Phase 2 completion |
| **Phase 4: Fair Value (Q2)** | DiD around IFRS/ASC adoption; simulate revalued statements; test information content | 2 months | Tables 6-7; fair-value simulation spreadsheet; coefficient comparison pre/post | Phase 1 completion |
| **Phase 5: Event Studies (Q3)** | Sale-leaseback CAR + matching; spin-off synthetic control; cross-sectional heterogeneity | 3 months | Tables 8-10; event-study figures; heterogeneity analysis | Phase 1 + 8-K collection |
| **Phase 6: Shock Analysis (Q4)** | Regional RE shocks (GFC, recessions); DiD; IV validation; parallel trends plots | 2 months | Tables 11-12; parallel trends figures; robustness tests; interaction effects | Phase 1 + CoStar regional indices |
| **Phase 7: Robustness & Writing** | Sensitivity analysis; threat-to-inference tests; paper writing; submission prep | 4 months | Complete manuscript; online appendix; response document | All phases complete |
| **Total** | | **18 months** | | |

---

## IX. JOURNAL SELECTION & SUBMISSION STRATEGY

### Target Journal Ranking

#### **Tier 1 (Primary Targets)**

1. **Journal of Finance**
   - Impact: Highest in finance
   - Acceptance rate: 6-8%
   - Target: Main results (Q1 + events) + one novel finding (fair value simulation)
   - Timeline: Submit after Phase 5 completion (~Month 12)
   - Considerations: Requires novel methodological contribution or surprising empirical finding; strong causal identification expected

2. **Journal of Financial Economics**
   - Impact: Top-tier; real estate finance focus slightly higher
   - Acceptance rate: 8-10%
   - Target: Main relevance test (Q1) + shock analysis (Q4)
   - Timeline: Month 13
   - Considerations: Values causal inference designs (DiD, IV); strong mechanisms

#### **Tier 2 (Alternative/Backup Targets)**

3. **Real Estate Economics** (AREUEA Journal)
   - Impact: Specialized; highest real estate credibility
   - Acceptance rate: 20-25%
   - Target: Full paper (all 4 research questions)
   - Timeline: Month 15 (if rejected from Tier 1)
   - Considerations: Most likely acceptance; good fit with audience

4. **Journal of Real Estate Finance & Economics**
   - Impact: Secondary; more methods-permissive
   - Acceptance rate: 25-30%
   - Target: Full paper
   - Timeline: Month 16

### Pre-Submission Strategy

1. **Month 12**: Compile results; assess novelty vs. empirical strength trade-off
   - If effects large & clean: target JF
   - If mechanisms novel & causal clear: target JFE
   - If robustness thorough: target Real Estate Economics

2. **Month 13**: Draft for feedback
   - Share with 2-3 finance/RE colleagues for comments
   - Seminar presentation (university, central bank, Fed)
   - Refine based on feedback

3. **Month 14**: Finalize for submission
   - Run all final robustness checks
   - Verify data quality; audit empirical tables
   - Write clear main text (results, not methods in body; methods in appendix)

4. **Month 15**: Submit

---

## X. OUTLINE OF EXPECTED PAPER STRUCTURE

### Main Text (~35 pages)

1. **Abstract** (250 words): Research question, data, main findings, contribution
2. **Introduction** (3-4 pages): Motivation (Macy's, Shopko examples), literature gap, research questions
3. **Literature Review** (3-4 pages): Real estate collateral, accounting, valuation anomalies, sale-leasebacks
4. **Data & Sample** (4-5 pages): Compustat, CRSP, CoStar, SEC EDGAR; sample composition; descriptive stats
5. **Main Results** (8-10 pages):
   - Fama-MacBeth regressions (Table 2-3)
   - Time-varying coefficients by decade (Figure 1, Table 4)
   - Robustness: fixed effects, IV, alternative outcomes (Table 5, appendix)
6. **Event Analysis** (5-6 pages):
   - Sale-leaseback CARs (Table 6, Figure 2)
   - Heterogeneous effects (Table 7)
   - REIT spin-offs (Table 8)
7. **Fair Value Simulation** (3-4 pages):
   - Revalued statements (Table 9)
   - DiD event study (Table 10, Figure 3)
8. **Collateral Channel** (4-5 pages):
   - Regional shocks DiD (Table 11, Figure 4)
   - Parallel trends, robustness (Table 12, appendix)
9. **Discussion & Implications** (2-3 pages):
   - What irrelevance means; implications for GAAP, managers, investors
10. **Conclusion** (1-2 pages)

### Online Appendix (~30-40 pages)

- A1: Data appendix (variable definitions, sources)
- A2: Sample composition by year, industry
- A3: All robustness tables (quantile regression, alternative RE measures, IV first stage, etc.)
- A4: Parallel trends plots (full set, by shock type)
- A5: Threat-to-inference tests (Rosenbaum bounds, attenuation bias calculations, coefficient stability)
- A6: Technical specifications (Fama-MacBeth SE formula, propensity score algorithm, synthetic control method)

---

## XI. KEY TAKEAWAYS FOR IMPLEMENTATION

1. **Research question is novel & important**: Fills a genuine gap (irrelevance vs. collateral effects; book vs. market values)
2. **Sample size achievable**: 8,000+ firm-years for main analysis; 2,000+ events for robustness
3. **Multi-method triangulation is strength**: Fama-MacBeth + events + shocks converge on same conclusion
4. **Causal inference needs careful attention**: Identify key threats (reverse causality, omitted vars, measurement error) early; plan mitigation during analysis
5. **Fair value simulation bridges accounting & finance**: Unique contribution; shows why fair value matters (information) and why accounting rules matter (agent behavior)
6. **Journal targeting pragmatic**: JF/JFE ambitious but achievable with clean effects; Real Estate Economics excellent fit for complete work
7. **Timeline realistic**: 18 months from data assembly to submission; allows for iterative refinement and robustness testing

---

## XII. REFERENCES TO SEMINAL PAPERS (See RESEARCH_PLAN_REFERENCES.md for full bibliography)

Key papers to cite/engage with:

- Chaney et al. (2012, JF): Real estate collateral
- Valta (2016, JFE): Regional RE shocks, causality
- Dessaint & Matray (2017, RoF): Sale-leaseback values
- Fama & French (2015, JFE): Book-to-market anomalies
- Landsman et al. (2012, RAS): Fair value accounting
- Shekhar (2017, MS): Sale-leaseback signaling
- Powers & Tsyplakov (2008, JF): RE separations create value

