create database payment_system;

use payment_system;

CREATE TABLE payment (
    customer_id INT PRIMARY KEY,
    customer VARCHAR(50),
    mode VARCHAR(20),
    city VARCHAR(50),
    amount DECIMAL(10,2)
);

INSERT INTO payment (customer_id, customer, mode, city, amount) VALUES
(101, 'Olivia Barrett', 'Netbanking', 'Portland', 2500),
(102, 'Ethan Sinclair', 'Credit Card', 'Miami', 4200),
(103, 'Maya Hernandez', 'Credit Card', 'Seattle', 1800),
(104, 'Liam Donovan', 'Netbanking', 'Denver', 3500),
(105, 'Sophia Nguyen', 'Credit Card', 'New Orleans', 2900),
(106, 'Caleb Foster', 'Debit Card', 'Minneapolis', 1500),
(107, 'Ava Patel', 'Debit Card', 'Phoenix', 2300),
(108, 'Lucas Carter', 'Netbanking', 'Boston', 4700),
(109, 'Isabella Martinez', 'Netbanking', 'Nashville', 3200),
(110, 'Jackson Brooks', 'Credit Card', 'Boston', 3900),
(111, 'Emma Wilson', 'UPI', 'Chicago', 2100),
(112, 'Noah Johnson', 'Cash', 'Dallas', 1200),
(113, 'Charlotte Brown', 'UPI', 'Houston', 2800),
(114, 'James Taylor', 'Debit Card', 'Atlanta', 3600),
(115, 'Amelia Davis', 'Cash', 'San Diego', 1700);

select * from payment;

select count(customer_id) from payment;

select mode ,count(customer)
from payment
group by mode
order by count(customer) desc;

