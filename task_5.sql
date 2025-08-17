-- File: task_5.sql
-- Use the database
USE alx_book_store;

-- Insert a single row into Customers table. If the key already exists, update the data.
INSERT INTO Customers (customer_id, customer_name, email, address)
VALUES (1, 'Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.')
ON DUPLICATE KEY UPDATE
    customer_name = VALUES(customer_name),
    email = VALUES(email),
    address = VALUES(address);