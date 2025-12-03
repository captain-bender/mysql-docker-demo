# Solutions — Mini Projects (Classicmodels)

This file provides sample SQL answers for the mini projects in `basic_exercises.md`.

---

## A. Customer & Order Analysis

1) Top 5 customers by total payments

```sql
SELECT c.customerNumber,
       c.customerName,
       SUM(p.amount) AS total_payments
FROM customers c
JOIN payments p ON c.customerNumber = p.customerNumber
GROUP BY c.customerNumber, c.customerName
ORDER BY total_payments DESC
LIMIT 5;
```

Notes: This returns the 5 customers who paid the most in total. You can add `country` to the SELECT/GROUP BY to filter by region.

2) Number of orders each of these customers placed

Use the previous result as a derived table (or re-run for those customerNumbers):

```sql
SELECT c.customerNumber, c.customerName, COUNT(o.orderNumber) AS orders_count
FROM customers c
LEFT JOIN orders o ON c.customerNumber = o.customerNumber
WHERE c.customerNumber IN (
  -- replace with the 5 customerNumbers from the previous query
  141, 124, 129, 131, 323
)
GROUP BY c.customerNumber, c.customerName;
```

---

## B. Product & Inventory Insights

1) Top 5 products with the highest quantity in stock

```sql
SELECT productCode, productName, quantityInStock
FROM products
ORDER BY quantityInStock DESC
LIMIT 5;
```

2) For each product, total number of times it appears in orders

(This sums `quantityOrdered` in `orderdetails` — gives units sold.)

```sql
SELECT p.productCode, p.productName, COALESCE(SUM(od.quantityOrdered),0) AS total_ordered
FROM products p
LEFT JOIN orderdetails od ON p.productCode = od.productCode
WHERE p.productCode IN (
  -- replace with productCodes from step 1
  'S10_1678','S10_1949','S10_2016','S10_4698','S10_4757'
)
GROUP BY p.productCode, p.productName
ORDER BY total_ordered DESC;
```

---

## C. Employee & Sales Structure

1) Employees who do not have any customers assigned (i.e., not referenced in `customers.salesRepEmployeeNumber`)

```sql
SELECT e.employeeNumber, e.lastName, e.firstName, e.jobTitle
FROM employees e
LEFT JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
WHERE c.customerNumber IS NULL
ORDER BY e.employeeNumber;
```