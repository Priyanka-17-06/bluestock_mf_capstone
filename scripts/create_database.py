import sqlite3
import pandas as pd

conn = sqlite3.connect("data/mutual_funds.db")

datasets = {
    "fund_master": "data/raw/01_fund_master.csv",
    "nav_history": "data/raw/02_nav_history.csv",
    "aum": "data/raw/03_aum_by_fund_house.csv",
    "sip": "data/raw/04_monthly_sip_inflows.csv",
    "category": "data/raw/05_category_inflows.csv",
    "folio": "data/raw/06_industry_folio_count.csv",
    "performance": "data/raw/07_scheme_performance.csv",
    "transactions": "data/raw/08_investor_transactions.csv",
    "portfolio": "data/raw/09_portfolio_holdings.csv",
    "benchmark": "data/raw/10_benchmark_indices.csv"
}

for table_name, file_path in datasets.items():
    df = pd.read_csv(file_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    print(f"{table_name} imported successfully.")

conn.close()

print("All datasets imported into SQLite successfully!")