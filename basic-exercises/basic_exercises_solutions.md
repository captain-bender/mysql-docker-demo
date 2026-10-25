# Solutions — Basics Exercises

This file contains short, reference answers for the independent "Project: Basics" tasks in `basic_exercises.md`. Each solution also says what result to expect, so you can check your own query.

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

Expected result: 10 rows. With the `ORDER BY` version, the first row is `103 | Atelier graphique | France`.

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

Expected result: 58 rows, starting with a stock of 9997 and ending with 5088.

## Basics 3 — COUNT and GROUP BY

Task: Count how many customers are in each `country`.

Solution:

```sql
SELECT country, COUNT(*) AS customer_count
FROM customers
GROUP BY country
ORDER BY customer_count DESC, country;
```

Explanation:
- `SELECT country, COUNT(*) AS customer_count`: return each country and the number of customers in it (the `COUNT(*)` is the aggregation).
- `FROM customers`: use the `customers` table as input.
- `GROUP BY country`: aggregate rows by `country` so the COUNT() is computed per country.
- `ORDER BY customer_count DESC, country`: show countries with the most customers first; countries with the same count are sorted alphabetically, so everyone gets the same order.

Expected result: 28 rows, starting with `USA | 36`. But look closely: **Norway appears twice**, once with 2 customers and once with 1. That's not a mistake in the query.

### Lesson: real data is messy

Two of the three Norwegian customers were entered as `'Norway  '`, with two invisible trailing spaces. To MySQL, `'Norway'` and `'Norway  '` are different text values, so `GROUP BY` puts them in separate groups. (MySQL 8 compares text exactly, trailing spaces included. Some older databases and settings ignore trailing spaces, so the same query can give different answers elsewhere.)

You can make the spaces visible by wrapping the value in brackets:

```sql
SELECT customerName, CONCAT('[', country, ']') AS country_shown
FROM customers
WHERE country LIKE 'Norway%';
```

This shows `[Norway]` for one customer and `[Norway  ]` for the other two.

The same problem quietly breaks filters too: `WHERE country = 'Norway'` finds only **1** of the 3 Norwegian customers, with no error or warning.

The fix in a query is `TRIM()`, which removes leading and trailing spaces:

```sql
SELECT TRIM(country) AS country, COUNT(*) AS customer_count
FROM customers
GROUP BY TRIM(country)
ORDER BY customer_count DESC, country;
```

Expected result: 27 rows, with a single `Norway | 3`.

To find every value with stray spaces, compare each value with its trimmed version:

```sql
SELECT customerNumber, customerName, country, city
FROM customers
WHERE country <> TRIM(country) OR city <> TRIM(city);
```

This returns 4 customers: the two Norwegian ones, plus two in New Zealand whose `city` is `'Auckland  '`.

Takeaways:
- Always look at the result, not just whether the query ran. A query can be correct and still give a misleading answer if the data is dirty.
- Before grouping or filtering on a text column, check its distinct values (`SELECT DISTINCT country FROM customers ORDER BY country;`).
- In a real project you would clean the data once at the source (for example `UPDATE customers SET country = TRIM(country);`) rather than adding `TRIM()` to every query. Here we deliberately leave the data as it is so you can see the problem for yourself.

## Basics 4 — Simple JOIN

Task: List the first 10 orders, by `orderNumber`, with the customer's name: `orderNumber`, `orderDate`, `customerName`.

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

Expected result: 10 rows, from order `10100` (2003-01-06, Online Diecast Creations Co.) to order `10109` (2003-03-10, Motor Mint Distributors Inc.).

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

Expected result: one row, `total_payments = 8853839.23` and `avg_payment = 32431.645531`.

Extra — rounding the average to 2 decimal places:

```sql
SELECT SUM(amount) AS total_payments,
       ROUND(AVG(amount), 2) AS avg_payment
FROM payments;
```

- `ROUND(value, 2)`: rounds to 2 decimal places, which suits money values. This gives `avg_payment = 32431.65`.
