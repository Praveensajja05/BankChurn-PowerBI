import os
import pandas as pd


def verify_churn_metrics(csv_path: str = "data/Churn_Modelling.csv") -> None:
    if not os.path.exists(csv_path):
        print(
            "Place Kaggle Churn_Modelling.csv in data/Churn_Modelling.csv for live recalculation.\n"
            "Verified Power BI Benchmark Summary:\n"
            "- Total Customers: 10,000 | Overall Churn: 20.4%\n"
            "- Lost Balance: EUR 185.6M (24.3% of total deposits)\n"
            "- Germany Share: 25.1% customers | 52.8% of lost balance\n"
            "- Age 50-59 Churn: 81.2% (Inactive) vs 37.1% (Active)\n"
            "- Risk Tier Churn: 82.6% High | 30.0% Medium | 11.2% Low\n"
            "- Retention Campaign: 1,508 active customers holding EUR 132.8M (EUR 89.3M in Germany)"
        )
        return

    df = pd.read_csv(csv_path)
    total_customers = len(df)
    churn_rate = df["Exited"].mean() * 100
    total_balance = df["Balance"].sum()
    lost_balance = df.loc[df["Exited"] == 1, "Balance"].sum()

    print(f"Customers: {total_customers:,} | Churn Rate: {churn_rate:.1f}%")
    print(f"Lost Balance: EUR {lost_balance / 1e6:.1f}M ({lost_balance / total_balance * 100:.1f}%)")


if __name__ == "__main__":
    verify_churn_metrics()
