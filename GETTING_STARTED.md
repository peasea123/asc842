# GETTING STARTED: Quick Reference Guide

## What You've Got

Your `asc842` repository now contains a complete **research framework** for a top-tier academic paper on corporate real estate valuation. This includes:

### 📋 Documentation (Reading Order)
1. **[EXECUTIVE_SUMMARY.md](EXECUTIVE_SUMMARY.md)** ← Start here (5 min read)
   - High-level overview of research contribution, design, and timeline
   - Key findings expected
   - Success metrics and go/no-go decisions

2. **[RESEARCH_PLAN.md](RESEARCH_PLAN.md)** ← Main reference (45 min read)
   - Comprehensive research roadmap covering:
     - Research gap analysis & novelty evaluation
     - Data sources (Compustat, CRSP, CoStar, SEC EDGAR)
     - Econometric specifications (Fama-MacBeth, DiD, event studies, IV)
     - Control variables and threats to causal inference
     - Sample size & power calculations
     - Journal strategy & publication timeline

3. **[methodology.tex](methodology.tex)** ← For paper writing
   - Detailed methodology section (ready to include in main manuscript)
   - All specifications, definitions, procedures in academic format
   - Can be imported directly into paperidea.tex

4. **[paperidea.tex](paperidea.tex)** ← Main paper
   - Paper idea with refined abstract (start here for writing)
   - Contains title, author information, structure outline

### 💻 Code
- **[analysis_pipeline.py](analysis_pipeline.py)**
  - Data collection and analysis code skeleton
  - Phase-by-phase organization (1-5)
  - Placeholder functions with full docstrings
  - Ready to populate with actual analysis

### 📊 Additional Files
- **[README.md](README.md)** - Project overview & build instructions
- **[references.bib](references.bib)** - Bibliography template
- **[.gitignore](.gitignore)** - Excludes LaTeX build artifacts
- **[chapters/](chapters/)**, **[figures/](figures/)** - Directories for organization

---

## Key Insights from Research Plan

### The Research Question
**Are book-valued real estate assets statistically irrelevant to corporate market valuations, after controlling for market-based real estate prices?**

- **Why novel**: No prior work systematically tests this irrelevance hypothesis
- **Why important**: Questions whether GAAP historical-cost accounting serves investor information needs
- **Expected answer**: Yes, book RE values are largely ignored by markets

### The Evidence (Four Complementary Tests)

| Test | Method | Expected Result |
|------|--------|-----------------|
| **Q1: Relevance** | Fama-MacBeth cross-sections (8,000+ obs) | Book RE β≈0; Market RE β>0 |
| **Q2: Fair Value** | Balance sheet simulation + event study | ROA↓3pp, Leverage↑, q unchanged |
| **Q3: Corporate Actions** | Event studies (2,000+ sales-leasebacks, 100 spin-offs) | CAR = +0.5 to +1.0% |
| **Q4: Collateral** | DiD using regional RE shocks | Elasticity = 0.08-0.12 |

### Why This Matters for Top-Tier Journals

1. **Novel contribution**: First systematic evidence on whether book RE is information-relevant
2. **Rigorous methodology**: Multi-method triangulation + explicit threat-to-inference analysis
3. **Long time horizon**: 44 years captures multiple regimes (inflation, 2008 crisis, IFRS adoption)
4. **Bridges disciplines**: Connects corporate finance, accounting, and real estate economics
5. **Policy implications**: Informs debate over fair-value accounting standards

---

## Implementation Timeline (18 Months)

```
Months 1-3:    Data Assembly → 8,000+ firm-years in clean panel
              |
Months 3-5:    Descriptive Analysis → Summary tables & trends
              |
Months 5-7:    Main Tests (Q1) → Fama-MacBeth regressions ← CRITICAL
              |
Months 7-9:    Fair Value (Q2) → Balance sheet simulation
              |
Months 9-12:   Events (Q3) → Sale-leaseback & spin-off CARs
              |
Months 12-14:  Collateral (Q4) → Regional shocks diff-in-diff
              |
Months 14-18:  Writing & Submission → Journal manuscript ready
```

**Go/No-Go Decision (Month 7)**: If book RE coefficient is NOT significant in main test, hypothesis confirmed (paper is stronger). If highly significant, pivot to explaining why instead of why they're irrelevant.

---

## Next Steps (First 4 Weeks)

### Week 1: Confirm Data Access
- [ ] Verify WRDS institutional access (Compustat, CRSP)
- [ ] Contact CoStar for real estate price indices license
- [ ] Confirm SEC EDGAR public data availability
- [ ] Estimate cost/timeline for data subscriptions

### Week 2: Begin Data Collection
- [ ] Write Python script to pull Compustat annual (1980-2024)
- [ ] Pull CRSP daily/monthly returns
- [ ] Begin SEC EDGAR 8-K scraping for sale-leaseback events
- [ ] Estimate sample size & missing data patterns

### Week 3: Proof-of-Concept Analysis
- [ ] Merge Compustat-CRSP (CCM linkage)
- [ ] Calculate Tobin's q, RE/TA, control variables
- [ ] Run small sample Fama-MacBeth on first 100 firm-years
- [ ] Check effect sizes against literature expectations

### Week 4: Share with Collaborators
- [ ] Present research plan to co-authors
- [ ] Get feedback on methodology choices
- [ ] Agree on data sources and timeline
- [ ] Divide responsibilities

---

## Key Decisions You've Already Made

✅ **Sample**: 200+ firms, 44 years (1980-2024) - comprehensive coverage  
✅ **Main method**: Fama-MacBeth + robustness checks (FE, IV)  
✅ **RE price signal**: CoStar metro-level indices (primary) + NAREIT (robustness)  
✅ **Events**: ~2,000-3,000 sale-leasebacks + 100 spin-offs (well-powered)  
✅ **Causal inference**: DiD using regional shocks + explicit threat analysis  
✅ **Journal target**: Journal of Finance (Tier 1) → Journal of Real Estate Economics (fallback)  

---

## Data Needs Checklist

- [ ] **Compustat**: PPE, depreciation, total assets, debt, capex, ROA (1980-2024)
- [ ] **CRSP**: Daily returns, prices, shares outstanding (1980-2024)
- [ ] **CoStar**: Metro-level commercial RE price indices (1990-2024, 380+ metros)
- [ ] **SEC EDGAR**: 8-K announcements (sale-leasebacks), 10-K footnotes (RE disclosures)
- [ ] **Supplementary**: Fama-French factors, Treasury rates, NBER recession dates

**Estimated cost for institutional subscriptions**: $15,000-30,000/year

---

## Common Pitfalls to Avoid

🚫 **Don't**:
1. Ignore data quality issues (missing PPE, inconsistent SIC codes)
2. Use only book RE without market-based controls (weakens main test)
3. Report results without addressing endogeneity concerns (IV/lagging)
4. Overlook compositional changes in sample (document by decade)
5. Report p-values without effect sizes (markets care about economic magnitude)
6. Claim causal findings without appropriate methodology (IV, DiD, events)

✅ **Do**:
1. Document all data collection & cleaning procedures
2. Create balanced vs. unbalanced panels; report both
3. Include pre-analysis plan (improves credibility with Tier-1 journals)
4. Test for parallel trends visually before DiD
5. Report multiple significance tests with FDR correction
6. Interpret results conservatively; acknowledge limitations upfront

---

## Where to Learn More

### Econometric Methods
- **Fama-MacBeth**: Fama & MacBeth (1973, JFE) or modern reviews in Cochrane (2011)
- **Panel FE & IV**: Wooldridge (2010, "Econometric Analysis of Cross Section & Panel Data")
- **Difference-in-Differences**: Callaway & Sant'Anna (2021, *Journal of Econometrics*) for recent advances
- **Causal Forests**: Athey & Wager (2019) for machine learning heterogeneous effects

### Real Estate Finance Literature
- **Collateral channel**: Chaney et al. (2012) and Valta (2016) in references
- **Fair value accounting**: Landsman et al. (2012) in Real Estate Economics
- **Sale-leasebacks**: Beattie et al. (2000) and Shekhar (2017)

### LaTeX Writing
- Use [overleaf.com](https://www.overleaf.com) for collaborative writing
- Templates for top journals available in Overleaf gallery
- methodology.tex can be directly imported with `\input{methodology}`

---

## Questions to Revisit Periodically

1. **Are we answering the right question?** 
   - Does market irrelevance hypothesis hold after Month 7 test?
   - If not, how does finding change interpretation?

2. **Is sample size adequate?**
   - Check power calculation assumptions against observed data
   - Do results hold in balanced panel only?

3. **Are causal claims justified?**
   - Do threat-to-inference mitigation strategies hold up?
   - Would Tier-1 journal reviewers be convinced?

4. **Is the story compelling?**
   - Does multi-method evidence triangulate to same conclusion?
   - Are heterogeneous effects (by firm type, shock magnitude) interesting?

5. **What's the policy implication?**
   - Should GAAP change? How?
   - Should managers restructure real estate? When?
   - What should investors do differently?

---

## Final Reminder

This research plan is **ambitious but feasible**. The combination of:
- **Long time horizon** (44 years)
- **Comprehensive sample** (200+ firms)
- **Multiple methods** (Fama-MacBeth + events + shocks)
- **Rigorous causal inference** (IV, DiD, matching)

…positions your paper for publication in a **top-tier academic journal**. 

The key is **disciplined execution**: Follow the timeline, validate data quality early, check assumptions continuously, and be prepared to pivot if Month 7 results contradict the hypothesis.

**You've got this.** 📊

---

**Next: Open [EXECUTIVE_SUMMARY.md](EXECUTIVE_SUMMARY.md) for a 5-minute orientation, then dive into [RESEARCH_PLAN.md](RESEARCH_PLAN.md) for detailed implementation guidance.**

