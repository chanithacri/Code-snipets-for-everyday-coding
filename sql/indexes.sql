-- indexes: Create/use indexes.
-- Mix of relational index patterns with notes for Postgres/MySQL.

-- Simple btree index on lookup column
CREATE INDEX IF NOT EXISTS idx_products_sku ON products (sku);

-- Composite index to speed up order item lookups by order and product
CREATE INDEX IF NOT EXISTS idx_items_order_product ON order_items (order_id, product_id);

-- Partial (filtered) index: Postgres only
-- CREATE INDEX CONCURRENTLY idx_products_active ON products (active) WHERE active IS TRUE;

-- Unique index across multiple columns
CREATE UNIQUE INDEX IF NOT EXISTS idx_customers_email_name
    ON customers (email, full_name);

-- Drop an index when no longer needed
DROP INDEX IF EXISTS idx_products_sku;

-- Inspect index usage (Postgres example)
SELECT relname AS table_name, indexrelname AS index_name, idx_scan, idx_tup_read
FROM pg_stat_user_indexes
ORDER BY idx_scan DESC;
