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

conn.close()