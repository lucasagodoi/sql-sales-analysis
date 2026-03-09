import pandas as pd
import sqlite3

df = pd.read_csv("data/sales_data.csv")

conn = sqlite3.connect("sales.db")

df.to_sql("sales", conn, if_exists="replace", index=False)

query = """
SELECT Region, SUM(Revenue) as Total_Revenue
FROM sales
GROUP BY Region
"""

result = pd.read_sql(query, conn)

print(result)