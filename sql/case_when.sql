-- case_when: CASE WHEN patterns.
-- Useful for derived labels and conditional aggregates.

-- Categorize product prices into bands
SELECT name,
       price,
       CASE
           WHEN price >= 100 THEN 'premium'
           WHEN price >= 50 THEN 'standard'
           ELSE 'budget'
       END AS price_band
FROM products;

-- Count orders into buckets using conditional aggregation
SELECT
    SUM(CASE WHEN order_total >= 500 THEN 1 ELSE 0 END) AS large_orders,
    SUM(CASE WHEN order_total BETWEEN 200 AND 499.99 THEN 1 ELSE 0 END) AS medium_orders,
    SUM(CASE WHEN order_total < 200 THEN 1 ELSE 0 END) AS small_orders
FROM orders;
