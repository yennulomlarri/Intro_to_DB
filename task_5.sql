-- Use INSERT IGNORE to prevent an error if the record already exists.
INSERT IGNORE INTO Customers (customer_id, customer_name, email, address)
VALUES (1, 'Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.');