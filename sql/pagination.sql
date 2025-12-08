-- pagination: LIMIT/OFFSET pagination.
-- Works in Postgres/MySQL compatible dialects.

-- Basic limit/offset
SELECT *
FROM products
ORDER BY product_id
LIMIT 10 OFFSET 20; -- page 3 when page size = 10

-- Keyset (seek) pagination for better performance
SELECT *
FROM products
WHERE product_id > 200
ORDER BY product_id
LIMIT 10;

-- Count total rows for UI page counts
SELECT COUNT(*) AS total_products FROM products;
