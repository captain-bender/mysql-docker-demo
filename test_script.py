import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Update with your credentials
engine = create_engine("mysql+mysqlconnector://root:passwd@localhost:3306/classicmodels")

# Example: Top 5 customers by total payments
query = """
SELECT c.customerName, SUM(p.amount) AS total_payments
FROM customers c
JOIN payments p ON c.customerNumber = p.customerNumber
GROUP BY c.customerName
ORDER BY total_payments DESC
LIMIT 5
"""
df = pd.read_sql(query, engine)
print(df)

# Bar plot
df.plot(kind="bar", x="customerName", y="total_payments", legend=False)
plt.title("Top 5 Customers by Total Payments")
plt.ylabel("Total Payments")
plt.xlabel("Customer Name")
plt.tight_layout()
plt.show()