"""
Data Collection and Analysis Pipeline for:
"Hidden in Plain Sight: The Irrelevance of Book-Value Real Estate Assets in Corporate Valuation"

This script provides the skeleton/template for:
1. Pulling data from Compustat, CRSP, CoStar
2. Merging financial data with stock returns
3. Computing valuation metrics and real estate measures
4. Conducting main econometric analyses
5. Generating tables and figures for publication

Author: [Research Team]
Date: February 2026

USAGE:
    python main_analysis.py --phase 1  # Data assembly
    python main_analysis.py --phase 2  # Descriptive statistics
    python main_analysis.py --phase 3  # Main Fama-MacBeth regressions
    python main_analysis.py --phase 4  # Fair value simulation
    python main_analysis.py --phase 5  # Event studies
"""

import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# For econometric analysis
import statsmodels.api as sm
from statsmodels.formula.api import ols, gls
from statsmodels.regression.linear_model import RegressionResults
import scipy.stats as stats

# Plotting style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 11

# ==============================================================================
# PHASE 1: DATA ASSEMBLY
# ==============================================================================

class DataAssembly:
    """Pull and merge Compustat, CRSP, CoStar, SEC EDGAR data"""
    
    def __init__(self, output_dir='./data'):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
    def pull_compustat(self, start_year=1980, end_year=2024):
        """
        Query Compustat annual data via WRDS
        
        Variables needed:
        - gvkey, tic, conm (company name)
        - fyear, indfmt, datafmt, consol
        - at (total assets), ppe (gross PPE), dpact (accumulated depreciation)
        - debt (total debt), cash, capx (capital expenditures)
        - ni (net income), revt (revenues)
        - Segment data for RE identification
        
        NOTE: Requires WRDS account access
        """
        
        print(f"[Phase 1] Pulling Compustat data ({start_year}-{end_year})...")
        
        # TODO: Implement WRDS connection
        # from wrds import sql
        # conn = sql.create_engine('postgres://...')
        
        query = f"""
        SELECT gvkey, tic, conm, fyear, 
               at, ppe, dpact, debt, cash, capx, ni, revt,
               loc
        FROM comp.funda
        WHERE fyear BETWEEN {start_year} AND {end_year}
          AND datafmt = 'STD'
          AND consol = 'C'
          AND indfmt IN ('FS', 'FS')
        ORDER BY gvkey, fyear
        """
        
        # comp_data = conn.raw_sql(query)  # Uncomment with WRDS
        # comp_data.to_csv(f'{self.output_dir}/compustat_raw.csv', index=False)
        
        print("  ✓ Compustat data pulled")
        return None  # Replace with actual dataframe
    
    def pull_crsp(self, start_year=1980, end_year=2024):
        """
        Query CRSP daily/monthly stock prices and returns
        
        Variables:
        - permno, cusip, namedt
        - date, prc (price), ret (return), shrout (shares outstanding)
        
        NOTE: Requires WRDS or local CRSP access
        """
        
        print(f"[Phase 1] Pulling CRSP data ({start_year}-{end_year})...")
        
        # TODO: Implement CRSP connection
        # Typically access via WRDS or OptionMetrics
        
        print("  ✓ CRSP data pulled")
        return None
    
    def pull_costar_indices(self):
        """
        Load CoStar Real Capital Analytics regional price indices
        
        Data structure: metro_code, property_type (office, retail, etc), date, price_index
        
        NOTE: CoStar data requires institutional license
        Fallback: NAREIT indices (national level, less detailed)
        """
        
        print("[Phase 1] Loading CoStar real estate price indices...")
        
        # TODO: Load from CSV or database
        # costar_data = pd.read_csv('./raw_data/costar_indices.csv')
        
        print("  ✓ CoStar indices loaded")
        return None
    
    def merge_ccm(self, comp_data, crsp_data):
        """
        Merge Compustat-CRSP using CCM (Compustat-CRSP Merged) linkage
        
        Standard approach: Use gvkey-permno linkages
        Timing: Use June 30 market cap for fiscal year-end matching
        """
        
        print("[Phase 1] Merging Compustat-CRSP (CCM)...")
        
        # TODO: Implement CCM merge
        # ccm_link = pd.read_csv('./raw_data/ccm_linkage.csv')
        # merged = comp_data.merge(ccm_link, on='gvkey')
        # merged = merged.merge(crsp_data, on=['permno', 'date'])
        
        print("  ✓ CCM merge completed")
        return None
    
    def create_sample(self, merged_data, exclude_re_firms=True):
        """
        Construct analysis sample with data quality filters
        
        Exclusions:
        - Missing PPE data
        - Negative PPE values
        - PPE/TA > 90% (likely REITs or data errors)
        - Non-positive total assets
        """
        
        print("[Phase 1] Constructing analysis sample...")
        
        # TODO: Apply filters
        # merged_data['book_re'] = merged_data['ppe'] - merged_data['dpact']
        # merged_data['re_ratio'] = merged_data['book_re'] / merged_data['at']
        
        # # Exclusions
        # sample = merged_data[
        #     (merged_data['ppe'].notna()) &
        #     (merged_data['ppe'] > 0) &
        #     (merged_data['at'] > 0) &
        #     (merged_data['re_ratio'] <= 0.90)
        # ]
        
        # if exclude_re_firms:
        #     # Exclude primary REIT companies by SIC
        #     sample = sample[~sample['sic'].between(6790, 6799)]
        
        print("  ✓ Sample constructed")
        print(f"    - Final N: {len(merged_data)} firm-years")
        
        return None

# ==============================================================================
# PHASE 2: DESCRIPTIVE STATISTICS
# ==============================================================================

class DescriptiveAnalysis:
    """Generate summary statistics, trends, and exploratory visualizations"""
    
    def __init__(self, data, output_dir='./output/descriptive'):
        self.data = data
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def summary_statistics_table(self):
        """
        Generate Table 1: Descriptive Statistics
        
        Shows mean, median, SD, percentiles for:
        - Tobin's q, Price-to-Book
        - Book RE / Total Assets
        - Market RE Index (CoStar)
        - Control variables (size, leverage, profitability, etc.)
        """
        
        print("[Phase 2] Computing summary statistics...")
        
        # TODO: Compute summary stats by variable
        # summary_stats = self.data[[
        #     'tobins_q', 'ptb', 're_ratio', 'costar_index',
        #     'ln_market_cap', 'leverage', 'roa', 'cash_ratio'
        # ]].describe(percentiles=[0.05, 0.25, 0.5, 0.75, 0.95])
        
        print("  ✓ Summary statistics computed")
        print("\nTable 1: Descriptive Statistics (Preview)")
        print("=" * 80)
        # print(summary_stats.to_string())
        
    def time_trends(self):
        """
        Generate Figure 1: Time Trends in Book RE Holdings
        
        Plots over 1980-2024:
        - Median RE/TA ratio by year
        - Median Tobin's q by year
        - CoStar real estate price index (national)
        """
        
        print("[Phase 2] Plotting time trends...")
        
        fig, axes = plt.subplots(3, 1, figsize=(14, 10))
        
        # TODO: Plot trends
        # by_year = self.data.groupby('year')[['re_ratio', 'tobins_q', 'costar_index']].median()
        # by_year['re_ratio'].plot(ax=axes[0], marker='o')
        # axes[0].set_ylabel('Median RE / Total Assets')
        # axes[0].set_title('Figure 1: Time Trends in Book Real Estate Holdings')
        
        plt.tight_layout()
        plt.savefig(f'{self.output_dir}/figure1_trends.png', dpi=300, bbox_inches='tight')
        print(f"  ✓ Saved: {self.output_dir}/figure1_trends.png")
        
    def book_market_correlation(self):
        """
        Generate correlation matrix and heatmap
        
        Shows correlation between:
        - Book RE / TA
        - Market RE Index (CoStar)
        - Tobin's q
        - Price-to-Book
        """
        
        print("[Phase 2] Computing book-market RE correlations...")
        
        # TODO: Compute correlations by period
        # corr = self.data[['re_ratio', 'costar_index', 'tobins_q']].corr()
        
        # sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
        # plt.title('Correlation Matrix: Book RE, Market RE, Valuations')
        # plt.savefig(f'{self.output_dir}/correlation_matrix.png', dpi=300)
        
        print("  ✓ Correlation matrix computed")

# ==============================================================================
# PHASE 3: MAIN FAMA-MACBETH REGRESSION
# ==============================================================================

class FamaMacBethAnalysis:
    """
    Fama-MacBeth cross-sectional regression analysis
    
    Model: q_{i,t} = α_t + β₁(RE/TA)_{i,t} + β₂ln(CoStar)_{t-1} + X'γ + ε_{i,t}
    
    Procedure:
    1. For each year t, run cross-sectional OLS
    2. Collect coefficient vector
    3. Pool across years (simple mean)
    4. Compute Newey-West standard errors
    """
    
    def __init__(self, data, output_dir='./output/main_analysis'):
        self.data = data
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
    def fm_regression(self):
        """Main Fama-MacBeth estimation"""
        
        print("[Phase 3] Running Fama-MacBeth regressions...")
        
        # TODO: Implement FM procedure
        # years = sorted(self.data['year'].unique())
        # coefficients_by_year = []
        
        # for year in years:
        #     year_data = self.data[self.data['year'] == year].copy()
        #     
        #     # Specification: q = α + β₁(RE/TA) + β₂ln(CoStar) + Controls
        #     formula = "tobins_q ~ re_ratio + ln_costar_index + ln_market_cap + roa + leverage + cash_ratio + rd_ratio"
        #     
        #     model = ols(formula, data=year_data).fit()
        #     coefficients_by_year.append({
        #         'year': year,
        #         'n': len(year_data),
        #         'const': model.params['Intercept'],
        #         're_ratio': model.params['re_ratio'],
        #         'ln_costar': model.params['ln_costar_index'],
        #         # ... other coefficients
        #     })
        
        # fm_results = pd.DataFrame(coefficients_by_year)
        # 
        # # Compute Newey-West standard errors with 3-lag MA
        # # ... implementation details ...
        
        print("  ✓ Fama-MacBeth regression completed")
        
    def robustness_fe(self):
        """Panel fixed effects robustness check"""
        
        print("[Phase 3] Running panel FE robustness...")
        
        # TODO: FE specification
        # formula = "tobins_q ~ re_ratio + ln_costar_index + ln_market_cap + roa + leverage + cash_ratio + C(year)"
        # fe_model = ols(formula, data=self.data).fit()
        # print(fe_model.summary())
        
        print("  ✓ Panel FE regression completed")
    
    def robustness_iv(self):
        """Instrumental variables (2SLS) robustness"""
        
        print("[Phase 3] Running IV (2SLS) specifications...")
        
        # TODO: IV specification
        # Instruments: lagged RE/TA, geographic IV (HQ metro × national trend)
        
        print("  ✓ IV regression completed")

# ==============================================================================
# PHASE 4: FAIR VALUE SIMULATION
# ==============================================================================

class FairValueAnalysis:
    """
    Simulate revalued balance sheets using CoStar indices
    
    Approach:
    1. Estimate market value: Book RE × (CoStar_t / CoStar_t0)
    2. Create pro forma revalued balance sheets
    3. Compare Tobin's q under book vs. revalued assumptions
    4. Event study around IFRS 13 / ASC 820 adoption
    """
    
    def __init__(self, data, output_dir='./output/fair_value'):
        self.data = data
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def estimate_market_re_value(self):
        """Estimate market value of RE using CoStar index inflation"""
        
        print("[Phase 4] Estimating market value of corporate real estate...")
        
        # TODO: Implement market value estimation
        # self.data['market_re_value'] = (
        #     (self.data['ppe'] - self.data['dpact']) *
        #     (self.data['costar_index'] / self.data['costar_index_baseline'])
        # )
        
        print("  ✓ Market RE values estimated")
    
    def create_revalued_statements(self):
        """Create pro forma revalued financial statements"""
        
        print("[Phase 4] Creating revalued balance sheets...")
        
        # TODO: Create revalued metrics
        # self.data['revalued_assets'] = (
        #     self.data['at'] + 
        #     (self.data['market_re_value'] - self.data['book_re'])
        # )
        # self.data['revalued_roa'] = self.data['ni'] / self.data['revalued_assets']
        # self.data['revalued_leverage'] = self.data['debt'] / self.data['revalued_assets']
        
        print("  ✓ Revalued statements created")
        print(f"    - Average ROA change: {(self.data['roa'] - self.data['revalued_roa']).mean():.4f}")
        print(f"    - Average leverage change: {(self.data['revalued_leverage'] - self.data['leverage']).mean():.4f}")
    
    def test_valuation_relevance(self):
        """Test whether revalued metrics improve valuation model"""
        
        print("[Phase 4] Testing valuation relevance of revalued metrics...")
        
        # TODO: Compare model fit
        # model_book = ols('tobins_q ~ re_ratio + controls', data=self.data).fit()
        # model_revalued = ols('tobins_q ~ revalued_re_ratio + controls', data=self.data).fit()
        # 
        # r2_improvement = model_revalued.rsquared - model_book.rsquared
        
        print("  ✓ Valuation relevance tested")

# ==============================================================================
# PHASE 5: EVENT STUDIES
# ==============================================================================

class EventStudyAnalysis:
    """
    Event studies for:
    1. Sale-leaseback transactions (event window: 8-K announcement)
    2. REIT spin-offs (event window: completion date)
    """
    
    def __init__(self, returns_data, event_data, output_dir='./output/events'):
        self.returns = returns_data
        self.events = event_data
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def calculate_abnormal_returns(self, event_type='sale_leaseback', window=(-10, 60)):
        """
        Calculate cumulative abnormal returns (CAR)
        
        Method: Fama-French 5-factor benchmark
        - Estimate model over days [-150, -11]
        - Calculate AR_d = R_d - R^FF5_d
        - Cumulate over event window
        """
        
        print(f"[Phase 5] Calculating abnormal returns for {event_type}...")
        
        # TODO: Implement event study
        # For each event:
        # 1. Estimate FF5 parameters on pre-event window
        # 2. Calculate expected returns
        # 3. Compute abnormal returns
        # 4. Cumulate over window
        
        print(f"  ✓ Abnormal returns calculated")
        
    def propensity_score_matching(self):
        """Match event firms to control firms on pre-event characteristics"""
        
        print("[Phase 5] Conducting propensity score matching...")
        
        # TODO: Implement PSM
        # 1. Estimate logit: Pr(Event) ~ controls (size, leverage, profitability, RE intensity)
        # 2. Match on propensity score (caliper = 0.01)
        # 3. Compute treatment effect = CAR_treated - CAR_control
        
        print("  ✓ Propensity score matching completed")

# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

def main():
    """Execute analysis pipeline"""
    
    import argparse
    parser = argparse.ArgumentParser(description='Real Estate Valuation Analysis')
    parser.add_argument('--phase', type=int, default=1, choices=[1, 2, 3, 4, 5],
                        help='Analysis phase to run')
    args = parser.parse_args()
    
    print("\n" + "="*80)
    print("REAL ESTATE VALUATION ANALYSIS PIPELINE")
    print("="*80 + "\n")
    
    if args.phase == 1:
        print("[PHASE 1] DATA ASSEMBLY")
        assembler = DataAssembly()
        comp = assembler.pull_compustat()
        crsp = assembler.pull_crsp()
        costar = assembler.pull_costar_indices()
        # merged = assembler.merge_ccm(comp, crsp)
        # sample = assembler.create_sample(merged)
        
    elif args.phase == 2:
        print("[PHASE 2] DESCRIPTIVE STATISTICS")
        # Load sample data
        # desc = DescriptiveAnalysis(sample)
        # desc.summary_statistics_table()
        # desc.time_trends()
        # desc.book_market_correlation()
        
    elif args.phase == 3:
        print("[PHASE 3] FAMA-MACBETH MAIN ANALYSIS")
        # fm = FamaMacBethAnalysis(sample)
        # fm.fm_regression()
        # fm.robustness_fe()
        # fm.robustness_iv()
        
    elif args.phase == 4:
        print("[PHASE 4] FAIR VALUE SIMULATION")
        # fv = FairValueAnalysis(sample)
        # fv.estimate_market_re_value()
        # fv.create_revalued_statements()
        # fv.test_valuation_relevance()
        
    elif args.phase == 5:
        print("[PHASE 5] EVENT STUDIES")
        # Load event and returns data
        # events = EventStudyAnalysis(returns, events)
        # events.calculate_abnormal_returns('sale_leaseback')
        # events.propensity_score_matching()
    
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE")
    print("="*80 + "\n")

if __name__ == '__main__':
    main()
