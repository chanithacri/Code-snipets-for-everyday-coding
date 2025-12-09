-- insert_bulk: Insert multiple rows.
-- Demonstrates multi-row VALUES and bulk loading patterns.

-- Insert multiple customers
INSERT INTO customers (email, full_name)
VALUES
    ('ada@example.com', 'Ada Lovelace'),
    ('grace@example.com', 'Grace Hopper'),
    ('alan@example.com', 'Alan Turing');

-- Insert order with items in a transaction
BEGIN;
INSERT INTO orders (customer_id, order_total)
VALUES (1, 125.00)
RETURNING order_id;
-- Assume returned order_id = 42
INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES
    (42, 3, 2, 25.00),
    (42, 5, 1, 75.00);
COMMIT;

-- Bulk import from CSV (Postgres)
-- \COPY products(sku, name, price, active) FROM 'products.csv' CSV HEADER;

-- MySQL equivalent
-- LOAD DATA LOCAL INFILE 'products.csv'
-- INTO TABLE products
-- FIELDS TERMINATED BY ',' ENCLOSED BY '"'
-- LINES TERMINATED BY '\n'
-- IGNORE 1 LINES;
