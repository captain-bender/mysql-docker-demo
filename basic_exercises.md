# Exercise: Exploring Business Insights in Classicmodels

## Objective
Use SQL queries to extract and visualize business insights from the Classicmodels database.

## Instructions
1. Connect to the Database

    - Use DBeaver (or your preferred SQL client) to connect to your running MySQL Docker container.

    - Database: classicmodels

    - User: root

    - Password: passwd

<br>
<br>
<br>

## Project: Basics

Before starting the larger mini-projects below, try one or more of these short, stand-alone exercises to practice simple SQL commands. They are independent (not cumulative) so you can pick any order.

- Basics 1 — Select a few columns

    Write a SELECT that returns `customerNumber`, `customerName`, and `country` from the `customers` table. Limit the result to 10 rows.

- Basics 2 — WHERE + ORDER BY

    Find products with `quantityInStock` greater than 5000. Return `productCode`, `productName`, and `quantityInStock`, ordered by `quantityInStock` descending.

- Basics 3 — COUNT and GROUP BY

    Count how many customers are in each `country`. Return `country` and `customer_count`, ordered by `customer_count` descending. Include countries with a single customer.

- Basics 4 — Simple JOIN

    List the first 10 orders with the customer's name: return `orderNumber`, `orderDate`, and `customerName` by joining `orders` with `customers`.

- Basics 5 — Aggregate numeric values

    Calculate the total `amount` of all payments in the `payments` table and the average payment amount. Return two columns: `total_payments` and `avg_payment`.

Hints: use `LIMIT`, `WHERE`, `ORDER BY`, `COUNT()`, `GROUP BY`, `JOIN ... ON`, `SUM()` and `AVG()` as appropriate. These are small, friendly exercises for absolute beginners.

If you want some help, check [sample answers](./basic_exercises_solutions.md)

<br>
<br>
<br>

## Mini projects (Difficulty level medium)
Choose One of the Following Mini-Projects:

A. Customer & Order Analysis

    1. Find the top 5 customers by total payments.

    2. List the number of orders each of these customers has placed.


B. Product & Inventory Insights

    1. List the top 5 products with the highest quantity in stock.

    2. For each product, show the total number of times it appears in orders.


C. Employee & Sales Structure

    1. List all employees who do not have any customers assigned.

If you want some help, check [sample answers](./mini_projects_solutions.md)

<br>
<br>
<br>

## Write and Run Your Queries

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