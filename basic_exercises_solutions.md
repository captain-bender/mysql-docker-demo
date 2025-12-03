# Solutions — Basics Exercises

This file contains short, reference answers for the independent "Project: Basics" tasks in `basic_exercises.md`.

## Basics 1 — Select a few columns

Task: Return `customerNumber`, `customerName`, and `country` from `customers`, limit to 10 rows.

Solution:

```sql
SELECT customerNumber, customerName, country
FROM customers
LIMIT 10;
```

Note: `LIMIT` without `ORDER BY` returns an arbitrary slice; for reproducible results add `ORDER BY customerNumber`.

```sql
SELECT customerNumber, customerName, country
FROM customers
ORDER BY customerNumber
LIMIT 10;
```

Explanation:
- `SELECT customerNumber, customerName, country`: choose which columns to return.
- `FROM customers`: query the `customers` table as the data source.
- `ORDER BY customerNumber`: (optional) sort results so the same rows are returned each time.
- `LIMIT 10`: return only the first 10 rows — useful for a quick sample or preview.

## Basics 2 — WHERE + ORDER BY

Task: Find products with `quantityInStock > 5000` and show `productCode`, `productName`, `quantityInStock`, ordered by `quantityInStock` descending.

Solution:

```sql
SELECT productCode, productName, quantityInStock
FROM products
WHERE quantityInStock > 5000
ORDER BY quantityInStock DESC;
```

Explanation:
- `SELECT productCode, productName, quantityInStock`: choose which product fields to show.
- `FROM products`: query the `products` table.
- `WHERE quantityInStock > 5000`: filter to only products with more than 5000 units in stock.
- `ORDER BY quantityInStock DESC`: sort the results by stock quantity from highest to lowest so the largest inventories appear first.

## Basics 3 — COUNT and GROUP BY

Task: Count how many customers are in each `country`.

Solution:

```sql
SELECT country, COUNT(*) AS customer_count
FROM customers
GROUP BY country
ORDER BY customer_count DESC;
```

Explanation:
- `SELECT country, COUNT(*) AS customer_count`: return each country and the number of customers in it (the `COUNT(*)` is the aggregation).
- `FROM customers`: use the `customers` table as input.
- `GROUP BY country`: aggregate rows by `country` so the COUNT() is computed per country.
- `ORDER BY customer_count DESC`: show countries with the most customers first.

## Basics 4 — Simple JOIN

Task: List the first 10 orders with the customer's name: `orderNumber`, `orderDate`, `customerName`.

Solution:

```sql
SELECT o.orderNumber, o.orderDate, c.customerName
FROM orders o
JOIN customers c ON o.customerNumber = c.customerNumber
ORDER BY o.orderNumber
LIMIT 10;
```

Explanation:
- `SELECT o.orderNumber, o.orderDate, c.customerName`: choose the three columns to return (order fields from `orders` and the customer's name from `customers`).
- `FROM orders o`: start from the `orders` table and give it the alias `o` for shorter references.
- `JOIN customers c ON o.customerNumber = c.customerNumber`: an inner join that matches each order to its customer using the `customerNumber` key; only orders with matching customers are returned.
- `ORDER BY o.orderNumber`: sort results by `orderNumber` so the output is predictable.
- `LIMIT 10`: return only the first 10 rows — useful for quick previews.

## Basics 5 — Aggregate numeric values

Task: Compute the total amount of payments and the average payment amount.

Solution:

```sql
SELECT SUM(amount) AS total_payments,
       AVG(amount) AS avg_payment
FROM payments;
```

Explanation:
- `SUM(amount)`: adds up all values in the `amount` column — gives the total of all payments.
- `AVG(amount)`: computes the arithmetic mean of the `amount` column — gives the average payment amount.
- `AS total_payments` / `AS avg_payment`: name the result columns so the output is readable.
- `FROM payments`: run the aggregation over the `payments` table.
