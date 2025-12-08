-- foreign_keys: Foreign key constraints.
-- Demonstrates creation, cascading rules, and validation checks.

-- Add foreign keys after table creation
ALTER TABLE orders
    ADD CONSTRAINT fk_orders_customer
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    ON DELETE RESTRICT ON UPDATE CASCADE;

ALTER TABLE order_items
    ADD CONSTRAINT fk_items_order
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
    ON DELETE CASCADE;

ALTER TABLE order_items
    ADD CONSTRAINT fk_items_product
    FOREIGN KEY (product_id) REFERENCES products(product_id)
    ON DELETE RESTRICT;

-- Validate an existing constraint (Postgres)
ALTER TABLE orders VALIDATE CONSTRAINT fk_orders_customer;

-- Inspect foreign keys (Postgres/ANSI)
SELECT tc.table_name, tc.constraint_name, kcu.column_name, ccu.table_name AS foreign_table
FROM information_schema.table_constraints tc
JOIN information_schema.key_column_usage kcu
  ON tc.constraint_name = kcu.constraint_name
JOIN information_schema.constraint_column_usage ccu
  ON ccu.constraint_name = tc.constraint_name
WHERE tc.constraint_type = 'FOREIGN KEY';
