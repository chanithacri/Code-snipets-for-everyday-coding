-- subqueries: Common subquery patterns.
-- Includes IN, EXISTS, and scalar subqueries.

-- Customers who have placed an order (IN)
SELECT * FROM customers
WHERE customer_id IN (
    SELECT DISTINCT customer_id FROM orders
);

-- Products never ordered (NOT EXISTS)
SELECT p.*
FROM products p
WHERE NOT EXISTS (
    SELECT 1 FROM order_items oi WHERE oi.product_id = p.product_id
);

-- Latest order total per customer using scalar subquery
SELECT c.customer_id, c.full_name,
       (
           SELECT o.order_total
           FROM orders o
           WHERE o.customer_id = c.customer_id
           ORDER BY o.placed_at DESC
           LIMIT 1
       ) AS last_order_total
FROM customers c;
