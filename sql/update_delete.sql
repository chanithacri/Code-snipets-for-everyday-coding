-- update_delete: Update/Delete with WHERE.
-- Safe patterns with row counts and optional returning clauses.

-- Update product price with guard
UPDATE products
SET price = price * 1.05
WHERE product_id = 5 AND active = TRUE;

-- Update with RETURNING (Postgres)
UPDATE customers
SET full_name = 'Updated Name'
WHERE email = 'ada@example.com'
RETURNING customer_id, full_name;

-- Delete orphaned order items (orders that no longer exist)
DELETE FROM order_items oi
WHERE NOT EXISTS (
    SELECT 1 FROM orders o WHERE o.order_id = oi.order_id
);

-- Soft delete customer by toggling active flag (needs column)
-- ALTER TABLE customers ADD COLUMN active BOOLEAN DEFAULT TRUE;
-- UPDATE customers SET active = FALSE WHERE customer_id = 7;
