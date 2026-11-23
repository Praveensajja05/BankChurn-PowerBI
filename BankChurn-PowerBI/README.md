# Bank Churn & Balance-at-Risk Dashboard

Customer retention and deposit-at-risk analysis across **10,000 European retail bank customers** (Kaggle `Churn_Modelling.csv`) built with **Power BI (Power Query & DAX)** and cross-verified in **Python**.

## Key Findings
- **Overall Churn & Deposit Loss:** Identified **20.4% overall churn** costing **EUR 185.6M** (**24.3%** of total deposits).
- **Root-Cause Segmentation:** Germany held **25.1%** of customers but accounted for **52.8%** of lost deposits; inactive customers aged **50–59** churned at **81.2%** vs. **37.1%** for active peers.
- **Risk Tiering & Retention Campaign:** Built a rule-based risk segmentation (**82.6% / 30.0% / 11.2%** historical churn across High / Medium / Low tiers) and recommended a targeted retention campaign for **1,508 active customers** holding **EUR 132.8M** (**22.9%** of remaining deposits), led by re-activating at-risk accounts in Germany (**EUR 89.3M**).

## Repository Structure
- `dax/measures_and_columns.dax`: Definitions for the **18 DAX measures** and **11 calculated columns** used in the Power BI data model.
- `src/verify_churn_metrics.py`: Python verification script validating all Power Query transformations and DAX aggregations.

## Quickstart
```bash
pip install -r requirements.txt
python src/verify_churn_metrics.py
```
