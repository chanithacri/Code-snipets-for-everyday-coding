-- stored_procs: Stored procedure skeleton.
-- Includes Postgres function and MySQL procedure examples.

-- Postgres: function returning a customer's total spend
CREATE OR REPLACE FUNCTION customer_total_spend(p_customer_id INT)
RETURNS NUMERIC AS $$
DECLARE
    total NUMERIC;
BEGIN
    SELECT COALESCE(SUM(order_total), 0) INTO total
    FROM orders
    WHERE customer_id = p_customer_id;
    RETURN total;
END;
$$ LANGUAGE plpgsql;

-- Call the function
SELECT customer_total_spend(1);

-- MySQL: stored procedure to insert a product
DELIMITER //
CREATE PROCEDURE insert_product(
    IN p_sku VARCHAR(64),
    IN p_name VARCHAR(255),
    IN p_price DECIMAL(10,2)
)
BEGIN
    INSERT INTO products (sku, name, price, active)
    VALUES (p_sku, p_name, p_price, TRUE);
END //
DELIMITER ;

-- Call the MySQL procedure
CALL insert_product('SKU-001', 'Example Product', 9.99);
