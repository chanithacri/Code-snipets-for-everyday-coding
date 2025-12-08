-- joins_all: INNER/LEFT/RIGHT/FULL joins.
-- Examples using customers, orders, products, and order_items tables.

-- INNER JOIN: orders with their customers
SELECT o.order_id, c.full_name, o.order_total
FROM orders o
INNER JOIN customers c ON c.customer_id = o.customer_id;

-- LEFT JOIN: include customers with zero orders
SELECT c.customer_id, c.full_name, o.order_id
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id
ORDER BY c.customer_id;

-- RIGHT JOIN: all orders even if customer missing (rare; alternative to LEFT)
SELECT c.customer_id, o.order_id, o.order_total
FROM customers c
RIGHT JOIN orders o ON o.customer_id = c.customer_id;

-- FULL OUTER JOIN: who ordered and who did not (Postgres)
SELECT c.full_name, o.order_id
FROM customers c
FULL OUTER JOIN orders o ON o.customer_id = c.customer_id;

-- Join across three tables to show line items
SELECT o.order_id, c.full_name, p.name AS product, oi.quantity, oi.unit_price
FROM order_items oi
JOIN orders o ON oi.order_id = o.order_id
JOIN customers c ON c.customer_id = o.customer_id
JOIN products p ON p.product_id = oi.product_id;
