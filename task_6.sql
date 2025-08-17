-- Select the database to ensure the script runs in the correct context
USE alx_book_store;

-- Insert multiple customers. For any customer_id that already exists,
-- update one of the fields to the same value to prevent an error.
INSERT INTO Customers (customer_id, customer_name, email, address) VALUES
(2, 'Blessing Malik', 'bmalik@sandtech.com', '124 Happiness Ave.'),
(3, 'Obed Ehoneah', 'eobed@sandtech.com', '125 Happiness Ave.'),
(4, 'Nehemial Kamolu', 'nkamolu@sandtech.com', '126 Happiness Ave.')
ON DUPLICATE KEY UPDATE customer_name = VALUES(customer_name);