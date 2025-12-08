-- aggregations: SUM/AVG/COUNT etc.
-- Examples aggregated over the shop schema.

-- Total revenue across all orders
SELECT SUM(order_total) AS revenue
FROM orders;

-- Average order value per customer
SELECT c.customer_id, c.full_name, AVG(o.order_total) AS avg_order
FROM customers c
JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.full_name
ORDER BY avg_order DESC;

-- Count products per active/inactive status
SELECT active, COUNT(*) AS product_count
FROM products
GROUP BY active;
