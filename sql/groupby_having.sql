-- groupby_having: GROUP BY with HAVING.
-- Filter aggregated groups for insights.

-- Customers with more than 5 orders
SELECT c.customer_id, c.full_name, COUNT(o.order_id) AS order_count
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.full_name
HAVING COUNT(o.order_id) > 5
ORDER BY order_count DESC;

-- Products with revenue above a threshold
SELECT p.product_id, p.name, SUM(oi.quantity * oi.unit_price) AS product_revenue
FROM products p
JOIN order_items oi ON oi.product_id = p.product_id
GROUP BY p.product_id, p.name
HAVING SUM(oi.quantity * oi.unit_price) >= 1000
ORDER BY product_revenue DESC;
