# Solutions — Integration Exercises

This file contains reference answers for the exercises in `integration_exercises.md`. Each solution is a complete script: save it as a `.py` file in the `mysql-docker-demo` folder and run it with the venv active. Each one also says what result to expect, so you can check your own version.

## Integration 1 — Stock by product line

Task: total `quantityInStock` per `productLine`, largest first, as a bar chart.

Solution:

```python
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://root:passwd@localhost:3306/classicmodels")

query = """
SELECT productLine, SUM(quantityInStock) AS total_stock
FROM products
GROUP BY productLine
ORDER BY total_stock DESC
"""
df = pd.read_sql(query, engine)
print(df)

df.plot(kind="bar", x="productLine", y="total_stock", legend=False)
plt.title("Total Stock by Product Line")
plt.ylabel("Units in stock")
plt.xlabel("Product line")
plt.tight_layout()
plt.show()
```

Explanation:
- `SUM(quantityInStock)` with `GROUP BY productLine` adds up the stock of every product in each line.
- `ORDER BY total_stock DESC` sorts the result, so the bars appear from tallest to shortest. pandas plots rows in the order they arrive.
- Everything else is the same as `test_script.py`; only the query and the labels change.

Expected result: 7 rows, from `Classic Cars | 219183` down to `Trains | 16696`. pandas prints these as `219183.0`: MySQL's `SUM()` returns a decimal number, which pandas converts to a float. The values are the same.

## Integration 2 — Sales by country

Task: top 10 countries by total sales (`quantityOrdered * priceEach`), as a bar chart.

Solution:

```python
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://root:passwd@localhost:3306/classicmodels")

query = """
SELECT TRIM(c.country) AS country,
       SUM(od.quantityOrdered * od.priceEach) AS total_sales
FROM orderdetails od
JOIN orders o    ON od.orderNumber = o.orderNumber
JOIN customers c ON o.customerNumber = c.customerNumber
GROUP BY TRIM(c.country)
ORDER BY total_sales DESC
LIMIT 10
"""
df = pd.read_sql(query, engine)
print(df)

df.plot(kind="barh", x="country", y="total_sales", legend=False)
plt.gca().invert_yaxis()   # largest at the top
plt.title("Top 10 Countries by Total Sales")
plt.xlabel("Total sales")
plt.ylabel("Country")
plt.tight_layout()
plt.show()
```

Explanation:
- `od.quantityOrdered * od.priceEach` is the value of one order line; `SUM(...)` adds up all lines for a country.
- The two `JOIN`s walk from each order line to its order, and from the order to its customer, which is where the country is stored.
- `TRIM(c.country)` removes stray spaces from the country names (see the lesson below).
- `kind="barh"` draws horizontal bars, which keeps country names readable. A horizontal chart draws the first row at the bottom, so `invert_yaxis()` puts the largest at the top.
- The small `1e6` at the end of the sales axis means the numbers are in millions, so `3.0` is 3,000,000.

Expected result: 10 rows, from `USA | 3273280.05` down to `Singapore | 263997.78`, with `Norway | 270846.30` in 9th place.

### Lesson: the Norway problem again, and this time it changes the answer

In Basics 3 you saw that two customers have their country stored as `'Norway  '`, with trailing spaces. If you write the query with a plain `c.country` instead of `TRIM(c.country)`, Norway's sales are split across two groups: 166,621.51 and 104,224.79. On their own, these rank 16th and 18th, so **Norway disappears from the top 10 completely**, even though its true total of 270,846.30 puts it 9th. The query runs without any error and the chart looks perfectly reasonable, but it's wrong.

In Basics 3 the problem only made a list look odd. Here, it silently changes a business conclusion. That's why it pays to check text columns before you group by them.

You can also fix the problem in pandas instead of SQL: load the data *without* `LIMIT`, clean the column, and group again.

```python
query = """
SELECT c.country, SUM(od.quantityOrdered * od.priceEach) AS total_sales
FROM orderdetails od
JOIN orders o    ON od.orderNumber = o.orderNumber
JOIN customers c ON o.customerNumber = c.customerNumber
GROUP BY c.country
"""
df = pd.read_sql(query, engine)
df["country"] = df["country"].str.strip()   # remove stray spaces
df = (df.groupby("country", as_index=False)["total_sales"].sum()
        .sort_values("total_sales", ascending=False)
        .head(10)
        .reset_index(drop=True))   # renumber the rows 0-9
print(df)
```

Notice that `LIMIT 10` must not be in the SQL here: if you cut the list to 10 rows before cleaning, the two halves of Norway are already gone.

Going further: this total includes every order, including the 6 cancelled ones. Try adding `WHERE o.status <> 'Cancelled'` and see whether the ranking changes.

## Integration 3 — Employees per office

Task: number of employees in each office, most first, as a bar chart.

Solution:

```python
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://root:passwd@localhost:3306/classicmodels")

query = """
SELECT o.city, COUNT(e.employeeNumber) AS employee_count
FROM offices o
LEFT JOIN employees e ON e.officeCode = o.officeCode
GROUP BY o.officeCode, o.city
ORDER BY employee_count DESC, o.city
"""
df = pd.read_sql(query, engine)
print(df)

df.plot(kind="bar", x="city", y="employee_count", legend=False)
plt.title("Employees per Office")
plt.ylabel("Number of employees")
plt.xlabel("Office")
plt.tight_layout()
plt.show()
```

Explanation:
- `LEFT JOIN` keeps every office, even one with no employees; an inner `JOIN` would silently drop it.
- `COUNT(e.employeeNumber)` counts only matching employees, so an empty office shows `0`. `COUNT(*)` would show `1` for an empty office, because the office row itself is counted.
- `GROUP BY o.officeCode, o.city` groups by the office's unique key, so two offices in cities with the same name would never be merged.

Expected result: 7 rows, starting with `San Francisco | 6`, then `Paris | 5` and `Sydney | 4`, followed by Boston, London, NYC and Tokyo with 2 each. (Every office currently has staff, so an inner `JOIN` gives the same result today, but the `LEFT JOIN` is the version that stays correct when a new office opens.)
