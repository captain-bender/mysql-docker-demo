# Use Python to connect to the database

In these exercises you query the `classicmodels` database from Python, load the results into a pandas DataFrame, and turn them into charts with matplotlib.

**Before you start**
- The Docker stack must be running (`docker compose up -d --build`, see the [README](./README.md)). Python connects straight to MySQL on `localhost:3306`.
- Python 3 must be installed on your computer.
- It helps to have done the [basic SQL exercises](./basic_exercises.md) first.

<br>

## 1. Set up a Python virtual environment

It's best practice to install the packages for a project into an isolated *virtual environment* (venv), using the list of packages in `requirements.txt`. Run these commands from inside the `mysql-docker-demo` folder.

**Windows (PowerShell)**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If PowerShell refuses to run `Activate.ps1`, run the following once (no admin rights needed), then activate again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

**macOS / Linux (Terminal)**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

When the venv is active you will see **(.venv)** at the start of your terminal prompt. Keep it active while you work through the exercises.

<br>

## 2. Run the example script

The repository includes [`test_script.py`](./test_script.py), which finds the top 5 customers by total payments and draws them as a bar chart:

```python
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Connection details for the MySQL container
engine = create_engine("mysql+mysqlconnector://root:passwd@localhost:3306/classicmodels")

# Example: Top 5 customers by total payments
query = """
SELECT c.customerName, SUM(p.amount) AS total_payments
FROM customers c
JOIN payments p ON c.customerNumber = p.customerNumber
GROUP BY c.customerNumber, c.customerName
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

How it works:
- `create_engine(...)` describes how to reach the database: driver (`mysql+mysqlconnector`), user, password, host, port and database name.
- `pd.read_sql(query, engine)` runs the SQL query and returns the result as a pandas DataFrame.
- `df.plot(...)` draws a chart from the DataFrame, and `plt.show()` opens it in a window.

Run it with (use `python3` on macOS/Linux):

```
python test_script.py
```

The table is printed in the terminal and a chart window opens, with Euro+ Shopping Channel at the top. **Close the chart window to end the script.** If the script ever hangs, press `CTRL-C` in the terminal.

<br>

## 3. Exercises

Each exercise follows the same pattern as the example: write a SQL query, load it with `pd.read_sql`, and plot it. The easiest way to start is to copy `test_script.py` to a new file (e.g. `exercise1.py`) and change the query and the plot labels.

- Integration 1 — Stock by product line

    For each `productLine`, calculate the total `quantityInStock` across its products. Return `productLine` and `total_stock`, ordered from largest to smallest, and show it as a bar chart.

- Integration 2 — Sales by country

    Find the **top 10 countries by total sales**. The sales value of each order line is `quantityOrdered * priceEach` (table `orderdetails`). To get from an order line to a country you need to join `orderdetails` → `orders` → `customers`. Return `country` and `total_sales`, and show the top 10 as a bar chart.

    When your chart works, think back to Basics 3: is every country you would expect in the top 10?

- Integration 3 — Employees per office

    Count how many employees work in each office. Return the office `city` and `employee_count`, ordered from most to fewest, and show it as a bar chart. Hint: join `offices` with `employees` using `officeCode`. Think about which kind of join would still show an office that has no employees yet.

Tips:
- Get the query working in phpMyAdmin first, then paste it into Python.
- For long labels, a horizontal bar chart (`kind="barh"`) is easier to read.
- `print(df)` before plotting lets you check the numbers.

If you want some help, check the [sample answers](./integration_exercises_solutions.md).

<br>

## 4. Finish

When you have finished, deactivate the virtual environment:

```
deactivate
```

The **(.venv)** at the start of your prompt disappears. Next time, just activate it again (step 1, second command); there is no need to reinstall the packages.

<br>

## Troubleshooting

- **`ModuleNotFoundError: No module named 'pandas'`** (or similar): the venv is not active, or the packages weren't installed into it. Activate it and run `pip install -r requirements.txt` again.
- **`Can't connect to MySQL server on 'localhost:3306'`**: the Docker stack isn't running, or MySQL is still loading on first start. Check with `docker compose ps` and wait until `mysql-demo` shows `(healthy)`.
- **`python` is not found on macOS/Linux**: use `python3` instead.
- **No chart window appears**: make sure your script ends with `plt.show()`.
