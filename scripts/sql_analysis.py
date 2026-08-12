import sqlite3

conn = sqlite3.connect("data/mutual_funds.db")

query = """
SELECT
    fund_house,
    COUNT(*) AS scheme_count
FROM fund_master
GROUP BY fund_house
ORDER BY scheme_count DESC;
"""

result = conn.execute(query).fetchall()

print("Schemes by Fund House:")

for row in result:
    print(row)
query = """
SELECT
    fm.amfi_code,
    fm.scheme_name,
    sp.return_1yr_pct
FROM performance sp
JOIN fund_master fm
    ON sp.amfi_code = fm.amfi_code
ORDER BY sp.return_1yr_pct DESC
LIMIT 10;
"""

result = conn.execute(query).fetchall()

print("Top 10 Schemes by 1-Year Return:")

for row in result:
    print(row)
