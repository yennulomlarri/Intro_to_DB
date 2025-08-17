-- File: task_5.sql
-- Use the database
USE alx_book_store;

-- Insert a single row into Customers table.
-- If a customer with the same primary key (customer_id) already exists,
-- update the customer_name to prevent the script from failing.
INSERT INTO Customers (customer_id, customer_name, email, address)
VALUES (1, 'Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.')
ON DUPLICATE KEY UPDATE customer_name = VALUES(customer_name);