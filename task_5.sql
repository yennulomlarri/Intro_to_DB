-- Select the database to ensure the script runs in the correct context
USE alx_book_store;

-- Insert the customer. If the customer_id already exists,
-- update one of the fields to the same value to prevent an error.
INSERT INTO Customers (customer_id, customer_name, email, address)
VALUES (1, 'Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.')
ON DUPLICATE KEY UPDATE customer_name = VALUES(customer_name);