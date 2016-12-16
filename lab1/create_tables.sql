
drop database if exists superstore;
create database superstore;
use superstore;
drop table Customer;
drop table Customer_Orders;
drop table Product;
drop table Product_Subcategory;
drop table Product_Category;
drop table Order_Products;

CREATE TABLE Product_Category (
  product_category_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  product_category_name varchar(50)
);

CREATE TABLE Product_Subcategory (
   product_subcategory_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
   product_subcategory_name varchar(50),
   product_category_id INT,
   FOREIGN KEY(product_category_id) REFERENCES Product_Category(product_category_id)
);

CREATE TABLE Customer_Segment(
    customer_segment_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    customer_segment_name varchar(50)
);

CREATE TABLE Customer (
   customer_id INT,
   customer_name varchar(50),
   city varchar(50),
   state varchar(20),
   postal_code INT,
   region varchar(20),
   customer_segment_id INT,
   PRIMARY KEY(customer_id, customer_segment_id),
   FOREIGN KEY (customer_segment_id) REFERENCES Customer_Segment(customer_segment_id)
);

CREATE TABLE Products (
  product_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  product_name varchar(100),
  unit_price decimal(10,2),
  product_subcategory_id INT,
  FOREIGN KEY(product_subcategory_id) REFERENCES Product_Subcategory(product_subcategory_id)
);

CREATE TABLE Customer_Orders(
  order_id INT PRIMARY KEY,
  customer_id INT,
  order_date DATE,
  order_priority varchar(20),
  FOREIGN KEY(customer_id) REFERENCES Customer(customer_id)
);

CREATE TABLE Order_Products(
   order_id INT,
   product_id INT,
   product_name varchar(100),
   order_quantity INT,
   PRIMARY KEY(order_id, product_id)
);










