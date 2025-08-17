-- Select the database to ensure the script runs in the correct context
USE alx_book_store;

-- Use INSERT IGNORE to prevent a "Duplicate entry" error if the record already exists.
-- This makes the script safe to run multiple times.
INSERT IGNORE INTO Customers (customer_id, customer_name, email, address)
VALUES (1, 'Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.');