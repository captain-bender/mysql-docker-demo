# Exercise: Exploring Business Insights in Classicmodels

## Objective
Use SQL queries to extract business insights from the Classicmodels database.

## Instructions
1. Connect to the Database

    - Make sure the stack is running (`docker compose up -d --build`, see the [README](./README.md)).

    - Open phpMyAdmin in your browser at **http://localhost:8080** and click `classicmodels` in the left-hand panel.

    - Write your queries in the **SQL** tab and press **Go** to run them.

    - Prefer a desktop client such as DBeaver? Connect with host `localhost`, port `3306`, user `root`, password `passwd`, database `classicmodels`.

<br>
<br>
<br>

## Project: Basics

Before moving on to the larger [mini-projects](./mini_projects.md), try one or more of these short, stand-alone exercises to practice simple SQL commands. They are independent (not cumulative) so you can pick any order.

- Basics 1 — Select a few columns

    Write a SELECT that returns `customerNumber`, `customerName`, and `country` from the `customers` table. Limit the result to 10 rows.

- Basics 2 — WHERE + ORDER BY

    Find products with `quantityInStock` greater than 5000. Return `productCode`, `productName`, and `quantityInStock`, ordered by `quantityInStock` descending.

- Basics 3 — COUNT and GROUP BY

    Count how many customers are in each `country`. Return `country` and `customer_count`, ordered by `customer_count` descending (and then by `country`, so that countries with the same count appear alphabetically).

    When you get your result, read through the list carefully. Does anything look odd?

- Basics 4 — Simple JOIN

    List the first 10 orders, by `orderNumber`, with the customer's name: return `orderNumber`, `orderDate`, and `customerName` by joining `orders` with `customers`.

- Basics 5 — Aggregate numeric values

    Calculate the total `amount` of all payments in the `payments` table and the average payment amount. Return two columns: `total_payments` and `avg_payment`. *Extra:* round the average to 2 decimal places.

Hints: use `LIMIT`, `WHERE`, `ORDER BY`, `COUNT()`, `GROUP BY`, `JOIN ... ON`, `SUM()`, `AVG()` and `ROUND()` as appropriate. These are small, friendly exercises for absolute beginners.

> **Note:** table names are case-sensitive in this setup. Write `customers`, not `Customers`.

If you want some help, check [sample answers](./basic_exercises_solutions.md)

<br>
<br>
<br>

## Write and Run Your Queries

Use SELECT statements, JOINs, GROUP BY, and ORDER BY as needed.

Example queries for inspiration:

```sql
-- Top 5 customers by total payments
SELECT customerNumber, customerName, SUM(amount) AS total_payments
FROM customers
JOIN payments USING (customerNumber)
GROUP BY customerNumber
ORDER BY total_payments DESC
LIMIT 5;
```
