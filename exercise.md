# Exercise: Exploring Business Insights in Classicmodels

## Objective
Use SQL queries to extract and visualize business insights from the Classicmodels database. Prepare 2–3 slides summarizing your findings and be ready to briefly present your approach and results.

## Instructions
1. Connect to the Database

    - Use DBeaver (or your preferred SQL client) to connect to your running MySQL Docker container.

    - Database: classicmodels

    - User: root

    - Password: passwd

2. Choose One of the Following Mini-Projects:

    A. Customer & Order Analysis

    - Find the top 5 customers by total payments.

    - List the number of orders each of these customers has placed.

    - Identify the most common order status among their orders.

    B. Product & Inventory Insights

    - List the top 5 products with the highest quantity in stock.

    - For each product, show the total number of times it appears in orders.

    - Find the average price of these products.

    C. Employee & Sales Structure

    - List all employees who do not have any customers assigned.

    - Show the different job titles among these employees.

    - Find the office locations where these employees work.

3. Write and Run Your Queries

    Use SELECT statements, JOINs, GROUP BY, and ORDER BY as needed.

    Example queries for inspiration:

    ```
    -- Top 5 customers by total payments
    SELECT customerNumber, customerName, SUM(amount) AS total_payments
    FROM Customers
    JOIN Payments USING (customerNumber)
    GROUP BY customerNumber
    ORDER BY total_payments DESC
    LIMIT 5;
    ```

4. Prepare Your Slides

    Slide 1: Briefly describe your chosen topic and approach.

    Slide 2: Show your key SQL queries and a summary table or chart of your findings.

    Slide 3 (optional): Reflect on any challenges, surprises, or potential business implications.

## Tips for Experimentation
- Try changing the LIMIT, sorting, or grouping to see different results.

- Modify queries to answer related questions (e.g., filter by country, date, or product line).

- Use DBeaver’s visualization features to create quick charts for your slides.

## Expected Learning Outcomes
- Practice SQL querying and data analysis.

- Gain insights into business operations using real-world data.

- Develop concise presentation skills for technical findings.

## Optional Extension for Python users

1. Install Required Python Packages
From the command line or terminal:
```
pip install pandas matplotlib sqlalchemy mysql-connector-python
```

2. Connect to MySQL and Run a Query
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

4. Include Visualizations in Slides
Save the plot as an image:
```
plt.savefig("my_plot.png")
```

