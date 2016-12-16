----------------------------------------------------------------------------------------------------------------------------------------
--create view for products
--This view is created with an inner join, left outer join, and an order by clause
CREATE VIEW product_vw
AS SELECT p.product_id, p.product_name, p.unit_price, pc.product_category_name, psc.product_subcategory_name
FROM Products p INNER JOIN Product_Subcategory psc
ON p.product_subcategory_id = psc.product_subcategory_id
LEFT OUTER JOIN Product_Category pc
ON pc.product_category_id = psc.product_category_id
ORDER BY product_id;



--This view shows product category names with average unit price
CREATE VIEW product_cat_ave_price_vw
AS SELECT pc.product_category_name, FORMAT(avg(unit_price), 2) ave_unit_price
FROM Products p INNER JOIN Product_Subcategory psc
ON p.product_subcategory_id = psc.product_subcategory_id
LEFT OUTER JOIN Product_Category pc
ON pc.product_category_id = psc.product_category_id
GROUP BY product_category_name
ORDER BY ave_unit_price DESC;

--Selecting by specific category
SELECT * FROM product_cat_ave_price_vw WHERE product_category_name = ["Technology"];
SELECT * FROM product_cat_ave_price_vw WHERE product_category_name = ["Office Supplies"];
SELECT * FROM product_cat_ave_price_vw WHERE product_category_name = ["Furniture"];

--This is for all product categories
SELECT * FROM product_cat_ave_price_vw;
--Get product counts for each category
--These select queries each have one group by with having clause and an aggregate

SELECT product_category_name, COUNT(*) num_products
FROM product_vw
GROUP BY product_category_name
HAVING product_category_name = ["Technology"];

SELECT product_category_name, COUNT(*) num_products
FROM product_vw
GROUP BY product_category_name
HAVING product_category_name = ["Office Supplies"];

SELECT product_category_name, COUNT(*) num_products
FROM product_vw
GROUP BY product_category_name
HAVING product_category_name = ["Furniture"];

SELECT product_category_name, COUNT(*) num_products
FROM product_vw
GROUP BY product_category_name;

------------------------------------------------------------------------------------------------------------------------
--create view for orders
--This view has one left outer join and an order by clause
CREATE VIEW order_vw
AS SELECT co.order_id, co.order_date, c.customer_name, c.postal_code, c.city, c.state, c.region
FROM Customer_Orders co LEFT OUTER JOIN Customer c
ON co.customer_id = c.customer_id
ORDER BY order_id;

--this view shows order counts for all regions
CREATE VIEW num_order_per_region_vw
AS SELECT region, COUNT(*) num_orders
FROM Customer
GROUP BY region
ORDER BY num_orders DESC;

--get order counts for each region
SELECT region, COUNT(*) num_orders
FROM order_vw
WHERE region =  ["South"];

SELECT region, COUNT(*) num_orders
FROM order_vw
WHERE region = ["West"];

SELECT region, COUNT(*) num_orders
FROM order_vw
WHERE region =  ["East"];

SELECT region, COUNT(*) num_orders
FROM order_vw
WHERE region = ["Central"];

--list order counts by year

SELECT EXTRACT(YEAR FROM order_date) year, COUNT(*) num_orders
FROM order_vw
GROUP BY year;

--These select statements each have a group by with having clause
SELECT EXTRACT(YEAR FROM order_date) year, COUNT(*) num_orders
FROM order_vw
GROUP BY year;
HAVING year = [2010];

SELECT EXTRACT(YEAR FROM order_date) year, COUNT(*) num_orders
FROM order_vw
GROUP BY year;
HAVING year = [2011];

SELECT EXTRACT(YEAR FROM order_date) year, COUNT(*) num_orders
FROM order_vw
GROUP BY year;
HAVING year = [2012];
------------------------------------------------------------------------------------------------------------------------
--creating view
--This view has an inner join
CREATE VIEW customer_vw
AS SELECT c.customer_id, c.customer_name, c.postal_code, c.city, c.state, c.region, cs.customer_segment_name
FROM Customer c INNER JOIN Customer_Segment cs
ON c.customer_segment_id = cs.customer_segment_id;

--getting counts for each region
--need to add a view here
SELECT region, COUNT(*) num_customers
FROM customer_vw
GROUP BY region;

SELECT region, COUNT(*) num_customers
FROM customer_vw
WHERE region = ["Central"];

SELECT region, COUNT(*) num_customers
FROM customer_vw
WHERE region =["East"];

SELECT region, COUNT(*) num_customers
FROM customer_vw
WHERE region = ["West"];

SELECT region, COUNT(*) num_customers
FROM customer_vw
WHERE region = ["South"];

--getting counts for each segment
SELECT customer_segment_name, COUNT(*) num_customers
FROM customer_vw
GROUP BY customer_segment_name;

SELECT customer_segment_name, COUNT(*) num_customers
FROM customer_vw
GROUP BY customer_segment_name
HAVING customer_segment_name = ["Corporate"];

SELECT customer_segment_name, COUNT(*) num_customers
FROM customer_vw
GROUP BY customer_segment_name
HAVING customer_segment_name = ["Home Office"];

SELECT customer_segment_name, COUNT(*) num_customers
FROM customer_vw
GROUP BY customer_segment_name
HAVING customer_segment_name = ["Small Business"];

SELECT customer_segment_name, COUNT(*) num_customers
FROM customer_vw
GROUP BY customer_segment_name
HAVING customer_segment_name = ["Consumer"];
