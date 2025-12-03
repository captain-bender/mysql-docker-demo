# Optional Extension for Python users

**Prerequisite (quick):** create and activate a Python virtual environment and install dependencies before running the examples below.

Quick commands (PowerShell):

```powershell
cd C:\Users\capta\OneDrive\Documents\mysql-docker-demo
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If you need the longer walkthrough, a venv section appears later in this file.


## Connect to MySQL and Run a Query
In a Python script, use the following template (replace credentials as needed):
```python
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
```
- This will display a bar chart of the top 5 customers by total payments.

3. Experiment with Other Queries
- Students can modify the query variable to visualize different aspects, e.g.:

    - Product inventory

    - Sales by country

    - Employee counts by office

4. You can run your script
```
python ./test_script.py
```
and stop the execution, using the combination of CTRL-C keys on your keyboard.

## Python virtual environment (`venv`) and `requirements.txt`

These optional exercises use Python packages. It's best practice to create an isolated virtual environment and install dependencies from a `requirements.txt` file.

Recommended workflow (PowerShell on Windows):

1. Create a venv in the project folder:

```powershell
cd C:\Users\capta\OneDrive\Documents\mysql-docker-demo
python -m venv .venv
```

2. Activate the venv (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks the script, run (as admin) `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` then activate again.

3. Install dependencies from `requirements.txt`:

```powershell
pip install -r requirements.txt
```

4. Run your Python script while the venv is active:

```powershell
python optional_plot.py
```

