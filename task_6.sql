-- File: task_6.sql
-- Use the database
USE alx_book_store;

-- Insert multiple rows into Customers table.
-- If any customer with the same primary key (customer_id) already exists,
-- update their customer_name to prevent the script from failing.
INSERT INTO Customers (customer_id, customer_name, email, address)
VALUES
    (2, 'Blessing Malik', 'bmalik@sandtech.com', '124 Happiness Ave.'),
    (3, 'Obed Ehoneah', 'eobed@sandtech.com', '125 Happiness Ave.'),
    (4, 'Nehemial Kamolu', 'nkamolu@sandtech.com', '126 Happiness Ave.')
ON DUPLICATE KEY UPDATE customer_name = VALUES(customer_name);