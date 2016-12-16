
drop database if exists superstore;
create database superstore;
use superstore;
drop table Customer;
drop table Customer_Orders;
drop table Product;
drop table Product_Subcategory;
drop table Product_Category;
drop table Order_Items;

CREATE TABLE Product_Category (
  product_category varchar(50) PRIMARY KEY
);

CREATE TABLE Product_Subcategory (
   product_subcategory varchar(50) PRIMARY KEY,
   product_category varchar(50),
   FOREIGN KEY(product_category) REFERENCES Product_Category(product_category)
);


CREATE TABLE Customer (
   customer_id INT PRIMARY KEY,
   customer_name varchar(50),
   city varchar(50),
   state varchar(20),
   postal_code INT,
   region varchar(20)
);

CREATE TABLE Product_Names (

  product_name varchar(100) PRIMARY KEY
);

CREATE TABLE Products (
  product_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  product_name varchar(100),
  unit_price decimal(10,2),
  product_subcategory varchar(50),
  FOREIGN KEY(product_subcategory) REFERENCES Product_Subcategory(product_subcategory),
  FOREIGN KEY(product_name) REFERENCES Product_Names(product_name)
);
CREATE TABLE Customer_Orders(
  order_id INT,
  customer_id INT,
  order_date DATE,
  PRIMARY KEY (order_id,customer_id),
  FOREIGN KEY (customer_id) REFERENCES Customer(Customer_ID)
);


CREATE TABLE Order_Items(
   order_item_id INT PRIMARY KEY,
   order_id INT,
   product_name varchar(100),
   order_quantity INT,
   FOREIGN KEY(product_name) REFERENCES Product_Names(product_name),
   FOREIGN KEY(order_id) REFERENCES Customer_Orders(order_id)
 );










