# ASC842: Research Paper on Corporate Real Estate Valuation

## 📑 Document Index & Navigation

This repository contains a complete research framework for an academic paper investigating whether book-valued corporate real estate assets are economically irrelevant to market valuations. Below is a guide to all documentation.

---

## 🚀 Quick Start (5 minutes)

**If you're new to this project, read these in order:**

1. **[GETTING_STARTED.md](GETTING_STARTED.md)** ← You are here
   - Quick reference guide for what you have
   - Next steps checklist
   - Key decisions & timeline overview

2. **[EXECUTIVE_SUMMARY.md](EXECUTIVE_SUMMARY.md)** (15 min)
   - Research contribution & novelty
   - Empirical design overview
   - Journal strategy
   - Expected findings

3. **[RESEARCH_PLAN.md](RESEARCH_PLAN.md)** (45 min) ← Main reference document
   - Comprehensive methodology
   - Data sources & assembly procedure
   - All econometric specifications
   - Threats to causal inference
   - Sample size & power calculations

---

## 📚 Core Documentation

### Research Strategy & Planning
| Document | Purpose | Read Time | Audience |
|----------|---------|-----------|----------|
| **GETTING_STARTED.md** | Orientation & checklist | 5 min | Everyone (start here) |
| **EXECUTIVE_SUMMARY.md** | High-level overview | 15 min | PIs, collaborators, reviewers |
| **RESEARCH_PLAN.md** | Comprehensive roadmap | 45 min | Research team, journal editors |
| **JOURNAL_STRATEGY.md** | Coming soon | — | — |

### Paper-Related Files
| Document | Purpose | Notes |
|----------|---------|-------|
| **paperidea.tex** | Main LaTeX paper | Contains refined abstract; update with results |
| **methodology.tex** | Methodology section | Detailed specs; import into main paper |
| **references.bib** | Bibliography database | Add papers as you write |
| **README.md** | Project overview | Quick build & contribution guide |

### Code & Implementation
| File | Purpose | Language |
|------|---------|----------|
| **analysis_pipeline.py** | Data & analysis skeleton | Python 3.10+ |
| (Pending) **analysis_full.py** | Complete analysis code | Python |
| (Pending) **visualization.py** | Publication-ready figures | Python/ggplot2 |
| (Pending) **tables_output.py** | LaTeX table generation | Python |

### Output Directories
```
figures/     → Publication-ready figures (saved as .png/.pdf)
tables/      → LaTeX tables (.tex files for inclusion in paper)
chapters/    → Main paper sections (organized by chapter)
data/        → Raw and processed datasets (local; not in git)
output/      → Analysis results by phase
```

---

## 📋 Documentation by Use Case

### "I'm a researcher on the team. Where do I start?"
1. Read **GETTING_STARTED.md** (5 min)
2. Review **RESEARCH_PLAN.md** sections I-III (data, methods) (20 min)
3. Review your assigned Phase (see timeline in EXECUTIVE_SUMMARY.md)
4. Begin data collection/analysis
5. Check weekly against methodology.tex to ensure reproducibility

### "I'm a co-author providing feedback. What should I know?"
1. Read **EXECUTIVE_SUMMARY.md** (15 min) - Get the story
2. Skim **RESEARCH_PLAN.md** section VII (threats to inference) (10 min) - Assess rigor
3. Read **RESEARCH_PLAN.md** section II (empirical design) (10 min) - Understand tests
4. Provide feedback on:
   - Hypothesis plausibility
   - Research design appropriateness
   - Sample size/power adequacy
   - Alternative explanations addressed

### "I want to understand the methodology deeply"
1. **RESEARCH_PLAN.md** section IV (econometrics) - Detailed specs
2. **methodology.tex** - LaTeX-formatted specifications
3. Key papers: Chaney et al. (2012), Valta (2016), Fama-MacBeth seminal works
4. Code implementations: analysis_pipeline.py (Python skeletons to populate)

### "I need to write the paper. How do I structure it?"
1. Use **methodology.tex** as Section 3 template (copy directly)
2. Follow structure in **paperidea.tex** (abstract already refined)
3. Generate results from **analysis_pipeline.py** phases 1-6
4. Use **RESEARCH_PLAN.md** appendix structure for robustness tables
5. Expected paper length: ~35 pages main text + 30-40 pages appendix

### "We're submitting to Journal of Finance. What's the checklist?"
1. Review journal standards in **EXECUTIVE_SUMMARY.md** section V
2. Verify:
   - [ ] Sample size ≥ 5,000 firm-years (✓ we have 8,000+)
   - [ ] Effect sizes economically meaningful (β ≥ 0.05 elasticity)
   - [ ] Causal inference methodology appropriate (IV, DiD, events)
   - [ ] Threat-to-inference analysis comprehensive
   - [ ] Robustness tests extensive (FE, IV, alternative specs)
3. Include pre-analysis plan as appendix
4. Have 2-3 external reviewers comment before submission

---

## 🎯 Research Timeline & Milestones

### Phase 1: Data Assembly (Months 1-3)
**Deliverable**: Clean panel of 8,000+ firm-year observations
- Compustat financial data (1980-2024)
- CRSP stock returns & valuations
- CoStar real estate price indices (1990-2024)
- SEC EDGAR event data (sale-leasebacks, spin-offs)

**Reference**: RESEARCH_PLAN.md §III (Data Sources)

### Phase 2: Descriptive Analysis (Months 3-5)
**Deliverable**: Tables 1-4, Figures 1-2 (summary statistics, trends)
- Summary statistics by year, industry
- Time trends in RE holdings
- Book-market RE correlations
- Sample composition documentation

**Reference**: Analysis code Phase 2 in analysis_pipeline.py

### Phase 3: Main Relevance Tests (Months 5-7) ⭐ CRITICAL
**Deliverable**: Tables 2-5 (Fama-MacBeth main results + robustness)
- **Go/No-Go Decision Here**: Does book RE coefficient = 0?
- Fama-MacBeth cross-sectional regressions
- Panel FE robustness checks
- IV specifications with predetermined instruments
- Time-varying coefficients by decade

**Reference**: RESEARCH_PLAN.md §IV.1 (Fama-MacBeth Specification)

### Phase 4: Fair Value Analysis (Months 7-9)
**Deliverable**: Tables 6-7 (fair value simulation & DiD)
- Market value estimation using CoStar indices
- Pro forma revalued balance sheets
- Event study around IFRS 13/ASC 820 adoption
- Comparison of book vs. market RE information content

**Reference**: RESEARCH_PLAN.md §IV.2 (Fair Value Simulation)

### Phase 5: Event Studies (Months 9-12)
**Deliverable**: Tables 8-10, Figures 3-4 (CARs for transactions)
- Sale-leaseback transaction analysis (n ≈ 2,000-3,000)
- Propensity score matching controls
- REIT spin-off analysis (synthetic control method)
- Heterogeneous effects by firm characteristics

**Reference**: RESEARCH_PLAN.md §IV.3-4 (Event Studies)

### Phase 6: Regional Shocks & Collateral (Months 12-14)
**Deliverable**: Tables 11-12, Figures 5-6 (DiD shocks)
- Identification of regional RE price shocks (GFC, 1990s recessions)
- Difference-in-differences estimation
- Parallel trends validation
- Instrumental variable specifications
- Robustness to alternative shock definitions

**Reference**: RESEARCH_PLAN.md §IV.4 (DiD Specification)

### Phase 7: Writing & Submission (Months 14-18)
**Deliverable**: Complete manuscript ready for journal submission
- Integrate results into main narrative
- Write introduction, related work, discussion
- Develop appendix with robustness tests
- Internal review (2-3 colleagues)
- Target: Submit to Journal of Finance (Month 15-16)

**Reference**: GETTING_STARTED.md section on paper writing

---

## 📊 Key Statistics & Targets

| Metric | Target | Source |
|--------|--------|--------|
| **Sample size** | 8,000-12,000 firm-years | RESEARCH_PLAN.md §VIII |
| **Time period** | 1980-2024 (44 years) | paperidea.tex abstract |
| **Main effect size** | β₁ ≈ 0 (irrelevant); β₂ > 0 (market RE relevant) | EXECUTIVE_SUMMARY.md §VII |
| **Event samples** | 2,000-3,000 sales-leasebacks; 100 spin-offs | RESEARCH_PLAN.md §III.4 |
| **Regional shocks** | 5,000-8,000 firm-years during price declines | RESEARCH_PLAN.md §III.5 |
| **Statistical power** | >80% for δ = 0.05 (α = 0.05, two-tailed) | RESEARCH_PLAN.md §VIII |

---

## 🔗 Cross-References

### Where to Find Information About...

**Data requirements?**
- RESEARCH_PLAN.md §III (complete data sources & assembly)
- GETTING_STARTED.md (data needs checklist)

**Econometric specifications?**
- RESEARCH_PLAN.md §IV (all models)
- methodology.tex (LaTeX-formatted specs)
- analysis_pipeline.py (Python code skeleton)

**Threats to causal inference?**
- RESEARCH_PLAN.md §VI (comprehensive threat analysis)
- EXECUTIVE_SUMMARY.md §IV (risk mitigation)

**Journal submission?**
- EXECUTIVE_SUMMARY.md §V (journal strategy)
- EXECUTIVE_SUMMARY.md §XI (success metrics)

**Literature to cite?**
- RESEARCH_PLAN.md (embedded throughout)
- references.bib (ready to expand)

**Timeline & milestones?**
- EXECUTIVE_SUMMARY.md §VI (18-month timeline)
- RESEARCH_PLAN.md §VIII (phase deliverables)

---

## 🔄 How to Use This Framework

### For Regular Progress Meetings
1. Open **RESEARCH_PLAN.md** section corresponding to current phase
2. Check off completed milestones
3. Identify blockers/challenges
4. Update timeline if needed
5. Assign next week's tasks

### For Writing the Paper
1. Import **methodology.tex** into **paperidea.tex**
2. Generate tables & figures from analysis phases
3. Use **RESEARCH_PLAN.md** as outline for introduction/related work
4. Include threat-to-inference tests in appendix
5. Reference **EXECUTIVE_SUMMARY.md** for policy implications in conclusion

### For Journal Submission
1. Review journal-specific requirements in **EXECUTIVE_SUMMARY.md** §V
2. Verify all robustness tests from **RESEARCH_PLAN.md** §VI included
3. Prepare response to anticipated reviewer comments (preview in RESEARCH_PLAN.md)
4. Gather supplementary materials (pre-analysis plan, replication data, code)

### For Revising After Rejection
1. Document reviewer comments
2. Map to relevant sections of **RESEARCH_PLAN.md**
3. Execute additional robustness tests as needed
4. Update **RESEARCH_PLAN.md** with findings
5. Retarget next journal based on revision magnitude

---

## 📝 File Manifest

```
asc842/
├── README.md                      # Project overview & build instructions
├── GETTING_STARTED.md             # ← Quick reference (this file)
├── EXECUTIVE_SUMMARY.md           # 15-min overview of entire plan
├── RESEARCH_PLAN.md               # 45-min comprehensive methodology reference
├── .gitignore                     # Excludes LaTeX artifacts, data files
├── 
├── Paper Files (Writing)
│   ├── paperidea.tex              # Main LaTeX paper template
│   ├── methodology.tex            # Detailed methodology section (import to main)
│   └── references.bib             # Bibliography (update as you go)
├── 
├── Analysis Code
│   └── analysis_pipeline.py       # Data & econometric analysis skeleton
├── 
├── Directory Structure
│   ├── chapters/                  # Main paper sections (to be populated)
│   ├── figures/                   # Publication-ready figures (.png, .pdf)
│   ├── tables/                    # LaTeX tables (.tex for inclusion in paper)
│   ├── data/                      # Raw & processed datasets (not in git)
│   └── output/                    # Analysis results by phase (not in git)
└── 
└── .git/                          # Git version control (all commits tracked)
```

---

## ✅ Verification Checklist

Before diving into data collection, verify:

- [ ] Git repository initialized & pushed to GitHub
- [ ] WRDS institutional access confirmed (Compustat, CRSP available)
- [ ] CoStar real estate indices available (or fallback to NAREIT planned)
- [ ] SEC EDGAR accessibility confirmed
- [ ] Python environment set up (pandas, statsmodels, scipy installed)
- [ ] LaTeX compiler working (pdflatex or Overleaf)
- [ ] Team members have repository access
- [ ] Timeline agreed upon with collaborators
- [ ] Roles/responsibilities assigned by phase

---

## 🆘 Getting Help

### Issue: Can't access WRDS data
**Solution**: Contact WRDS support or institution IT. Estimated 1-2 week turnaround.

### Issue: CoStar data too expensive
**Solution**: Use NAREIT indices (free, national level) for main analysis; CoStar for robustness

### Issue: SEC EDGAR scraping failing
**Solution**: Fall back to manual collection for subset; use FactSet/Bloomberg for validation

### Issue: Coefficient signs unexpected
**Solution**: Check data construction (have you lagged correctly?), remove outliers, verify sample composition

### Issue: Sample too small in subgroups
**Solution**: Combine event/shock analyses into joint hypothesis test; use synthetic control for small samples

---

## 🎓 Additional Resources

### Methodology References
- **Fama-MacBeth**: Cochrane (2011) or original Fama & MacBeth (1973)
- **Panel methods**: Wooldridge (2010) textbook
- **Causal inference**: Angrist & Pischke (2009, 2015)
- **Event studies**: MacKinlay (1997), Corrado (2011)

### Domain Literature
- **Real estate finance**: See references in RESEARCH_PLAN.md (Chaney et al., Valta, Dessaint & Matray)
- **Accounting standards**: Landsman et al. (2012), Müller et al. (2015)
- **Corporate finance**: Fama & French literature on anomalies

### Coding Resources
- **Python/Pandas**: [Modern Pandas](https://tomaugspurger.github.io/) by Tom Augspurger
- **Statsmodels**: Official documentation (https://www.statsmodels.org/)
- **Visualization**: Seaborn & Matplotlib guides

---

## 📞 Contact & Questions

For questions about:
- **Research design**: See RESEARCH_PLAN.md or contact PI
- **Code implementation**: See analysis_pipeline.py docstrings or post issue
- **Data access**: Contact institution's data librarian or WRDS support
- **Paper writing**: Refer to journal guidelines (linked in EXECUTIVE_SUMMARY.md)
- **General**: Open GitHub issue with clear description

---

**Last Updated**: February 8, 2026  
**Status**: Research framework complete; ready for implementation  
**Next Step**: Begin Phase 1 (Data Assembly) - See RESEARCH_PLAN.md §III

Good luck with your research! 🚀

