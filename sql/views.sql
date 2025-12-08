-- views: Create and query views.
-- Provides both standard and materialized view examples.

-- Simple view showing order totals with customer names
CREATE OR REPLACE VIEW v_customer_orders AS
SELECT o.order_id, c.full_name, o.order_total, o.placed_at
FROM orders o
JOIN customers c ON c.customer_id = o.customer_id;

-- Query the view
SELECT * FROM v_customer_orders WHERE order_total > 100;

-- Materialized view (Postgres) for product revenue
-- CREATE MATERIALIZED VIEW mv_product_revenue AS
-- SELECT p.product_id, p.name, SUM(oi.quantity * oi.unit_price) AS revenue
-- FROM products p
-- JOIN order_items oi ON oi.product_id = p.product_id
-- GROUP BY p.product_id, p.name;

-- Refresh materialized view when data changes
-- REFRESH MATERIALIZED VIEW CONCURRENTLY mv_product_revenue;
