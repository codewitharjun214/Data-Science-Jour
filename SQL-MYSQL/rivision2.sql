CREATE DATABASE CompanyDB;
USE CompanyDB;

create table department(
department_id int primary key,
department_name varchar(50),
location varchar(50)
);

INSERT INTO Department (department_id, department_name, location)
VALUES
(101, 'Human Resources', 'Pune'),
(102, 'Finance', 'Mumbai'),
(103, 'IT', 'Bengaluru'),
(104, 'Sales', 'Delhi'),
(105, 'Marketing', 'Hyderabad'),
(106, 'Operations', 'Chennai'),
(107, 'Customer Support', 'Pune'),
(108, 'Research & Development', 'Bengaluru'),
(109, 'Legal', 'Mumbai'),
(110, 'Administration', 'Nagpur');

select * from department;

-- 1 Display all departments.
   
   select * from department;
   
-- 2 Display only the department names.
   
   select department_name from department;
   

-- 3 Show all departments located in Pune.
  
  select department_name from department
   where location = "Pune";

-- 4 Show all departments except those in Mumbai.
   
   select * from department 
   where location != "Mumbai";
   
   
-- 5 Display unique locations.

   select distinct location from department;
   

-- 6 Sort departments alphabetically by department name.
select department_name from department
order by department_name asc ;


-- 7 Sort locations in descending order.
select location from department
order by location desc;

-- 8 Find departments whose name starts with 'M'.

SELECT department_name
FROM Department
WHERE department_name LIKE 'M%';


-- 9 Find departments whose location ends with 'i'.

select location
from department
where location like '%I';

-- 10 Count the total number of departments.
select count(*) from department;

-- all questions of departemnt table are solved 


create table employess (
emp_id int primary key,
first_name varchar (50),
last_name varchar (50),
gender varchar (10),
age int not null ,
salary int,
hire_date date,
department_id int,
manager_id int,
city varchar(50),
email varchar(50),
experiance int,

foreign key (department_id)  REFERENCES department(department_id)
);

INSERT INTO Employess
(emp_id, first_name, last_name, gender, age, salary, hire_date, department_id, manager_id, city, email, experiance)
VALUES
(101, 'Rahul', 'Sharma', 'Male', 28, 45000, '2022-01-15', 103, NULL, 'Pune', 'rahul.sharma@company.com', 4),

(102, 'Priya', 'Patil', 'Female', 30, 60000, '2021-06-10', 102, 101, 'Mumbai', 'priya.patil@company.com', 6),

(103, 'Amit', 'Verma', 'Male', 26, 38000, '2023-03-12', 104, 101, 'Delhi', 'amit.verma@company.com', 2),

(104, 'Sneha', 'Kulkarni', 'Female', 35, 85000, '2019-08-25', 103, NULL, 'Bengaluru', 'sneha.kulkarni@company.com', 10),

(105, 'Rohit', 'Joshi', 'Male', 31, 72000, '2020-11-20', 105, 104, 'Hyderabad', 'rohit.joshi@company.com', 7),

(106, 'Neha', 'Deshmukh', 'Female', 27, 50000, '2022-07-18', 107, 104, 'Pune', 'neha.deshmukh@company.com', 4),

(107, 'Karan', 'Mehta', 'Male', 29, 56000, '2021-09-05', 106, 104, 'Chennai', 'karan.mehta@company.com', 5),

(108, 'Pooja', 'Singh', 'Female', 24, 35000, '2024-01-08', 104, 107, 'Delhi', 'pooja.singh@company.com', 1),

(109, 'Vikram', 'Nair', 'Male', 38, 98000, '2018-04-17', 108, NULL, 'Bengaluru', 'vikram.nair@company.com', 13),

(110, 'Anjali', 'Gupta', 'Female', 32, 67000, '2020-05-30', 101, 109, 'Nagpur', 'anjali.gupta@company.com', 8);

select * from employess;

-- Display all employees.
select * from employess;


-- Display only first name and salary.
select first_name,salary from employess;


-- Find employees earning more than ₹50,000.
select * from employess
where salary > 50000;


-- Find employees aged between 25 and 30.
select * from employess
where age between 25 and 30 ;


-- Find female employees.
select * from employess 
where gender = "Female";

-- Find employees from Pune.
select * from Employess 
where city = "Pune";


-- Find employees whose first name starts with 'A'.

select * from employess 
where first_name like 'A%';


-- Find employees hired after 1 Jan 2022.

select * from employess 
where hire_date > '2022-1-1';


-- Display unique cities.
select distinct city
from employess ;

-- Count total employees.
select count(*) from employess;

-- i have solved the all questions of the employess table 

create table projects (
project_id int primary key,
project_name varchar(100),
start_date date,
end_date date,
budget int 
);

ALTER TABLE Projects
ADD status VARCHAR(20);

alter table projects
add client_name varchar(50);

select * from projects;

INSERT INTO Projects
(project_id, project_name, client_name, start_date, end_date, budget, status)
VALUES
(201, 'E-Commerce Website', 'Amazon', '2024-01-15', '2024-09-30', 1500000, 'Completed'),

(202, 'Banking Dashboard', 'HDFC Bank', '2024-03-01', '2024-12-31', 2200000, 'Ongoing'),

(203, 'Hospital Management System', 'Apollo', '2023-07-01', '2024-04-15', 1800000, 'Completed'),

(204, 'Inventory Management', 'Reliance', '2024-05-10', '2025-01-30', 950000, 'Ongoing'),

(205, 'HR Management System', 'Infosys', '2023-11-01', '2024-08-20', 1300000, 'Completed'),

(206, 'CRM Application', 'TCS', '2024-02-10', '2025-02-15', 2500000, 'Ongoing'),

(207, 'Sales Analytics Dashboard', 'Deloitte', '2024-06-01', '2025-03-31', 1750000, 'Ongoing'),

(208, 'Retail POS System', 'DMart', '2023-10-15', '2024-06-30', 1200000, 'Completed'),

(209, 'AI Chatbot', 'Microsoft', '2024-07-01', '2025-05-31', 3200000, 'Ongoing'),

(210, 'Student Portal', 'Savitribai Phule Pune University', '2024-01-05', '2024-11-30', 850000, 'Completed');

-- lets start solving the projects table questions 

-- Projects Table Questions (Easy → Medium)

-- Don't scroll further once you start solving. Try them yourself first.

-- Q1

-- Display all projects.

select * from projects;

-- Q2

-- Display only project names.

select project_name from projects;

-- Q3

-- Show projects with budget greater than ₹15,00,000.

SELECT *
FROM projects
WHERE budget > 1500000;

-- Q4

-- Show projects whose budget is less than ₹10,00,000.

SELECT *
FROM projects
WHERE budget < 1000000;

-- Q5

-- Display only completed projects.

select * from projects 
where status = "Completed";

-- Q6

-- Display only ongoing projects.

select * from projects 
where status = "Ongoing";

-- Q7

-- Show projects that started after 1 April 2024.

select * from projects 
where start_date > '2024-4-1';

-- Q8

-- Show projects ending before 31 December 2024.

select * from projects 
where end_date < '2024-12-31';

-- Q9

-- Display project name and budget.

select project_name,budget
from projects;

-- Q10

-- Display project name, client name and status.

select project_name,client_name,status
from projects;


-- Q11

-- Find projects whose name starts with S.

select * from projects
where project_name like 'S%';

-- Q12

-- Find projects whose name ends with System.

select * from projects
where project_name like '%System';


-- Q13

-- Find client names starting with A.

select * from projects
where client_name like 'A%';

-- Q14

-- Display unique project statuses.

select distinct status
from projects;


-- Q15

-- Count total projects.
select count(*) from projects;

-- Q16

-- Find the highest budget.

select max(budget) from projects;


-- Q17

-- Find the lowest budget.
select min(budget) from projects;

-- Q18

-- Find the average budget.
select avg(budget) from projects;

-- Q19

-- Find the total budget of all projects.
select sum(budget) from projects;

-- Q20

-- Sort projects by budget (Ascending).

select * from projects
order by budget asc;

-- Q21

-- Sort projects by budget (Descending).

select * from projects
order by budget desc;

-- Q22

-- Sort projects by project name alphabetically.

select * from projects
order by project_name asc;

-- Q23

-- Display the top 5 highest-budget projects.

select * from projects
order by budget desc 
limit  5 ;

-- Q24

-- Display projects with budgets between ₹10,00,000 and ₹20,00,000.

select * from projects 
where budget between 1000000 and 2000000;

-- Q25

-- Display projects whose client name contains Bank.

select * from projects
where client_name like '%Bank%';

-- Medium Questions
-- Q26

-- Count how many projects are Completed.

select count(*) from projects 
where status = "Completed";

-- Q27

-- Count how many projects are Ongoing.

select count(*) from projects 
where status = "Ongoing";

-- Q28

-- Display all completed projects sorted by budget descending.
select * from projects
having status = "Completed"
order by budget desc ;

-- Q29

-- Find the project having the highest budget.

select project_name, budget 
from projects 
where budget = (select max(budget)
from projects);

-- Q30

-- Find the project having the lowest budget.

select project_name , budget
from projects
where budget = (select min(budget)
from projects);

-- Q31

-- Display project duration (difference between start and end date) in days.

SELECT project_name,
       start_date,
       end_date,
       DATEDIFF(end_date, start_date) AS duration_days
FROM projects;


-- (Hint: DATEDIFF(end_date, start_date) in MySQL.)

-- Q32

select project_name,
start_date,
end_date,
datediff(end_date,start_date)as duration_days
from projects
where datediff(end_date,start_date) >300;

-- Q33

-- Display project name along with budget in lakhs.

select project_name , 
budget / 100000 as budget_in_lakhs
from projects;


-- Example:

-- Project	Budget (Lakhs)
-- AI Chatbot	32
-- Q34

-- Find projects where client name contains the letter o.

select project_name , client_name 
from projects 
where client_name like '%o%';

-- Q35

-- Display projects ordered by start date.

select project_name ,
start_date 
from projects 
where start_date
order by start_date asc ;

-- Interview Challenge (Without Hints)
-- Q36

-- Find the second highest budget.

select budget
from projects
order by budget desc 
limit 1 offset 1 ;


-- Q37

-- Display the top 3 most expensive projects.

select budget
from projects 
order by budget desc
limit 3 ;

-- Q38

-- Find all projects starting in 2024.

select * from projects
where start_date like '%2024%';

-- Q39

-- Display projects that are not completed.

select * from projects 
where status != "Completed";

-- Q40

-- Find projects whose budget is above the average budget.
select project_name,budget
from projects
where budget > (select avg(budget) from projects);


















create table employeeproject(
employee_id int,
project_id int,
role varchar(50),

primary key (employee_id , project_id),

FOREIGN KEY(employee_id) REFERENCES Employess(emp_id),
FOREIGN KEY(project_id) REFERENCES Projects(project_id)

);

select * from employeeproject ;

INSERT INTO EmployeeProject (employee_id, project_id, role)
VALUES
(101, 201, 'Backend Developer'),
(101, 209, 'API Developer'),

(102, 202, 'Data Analyst'),
(102, 207, 'BI Developer'),

(103, 201, 'Frontend Developer'),
(103, 204, 'UI Developer'),

(104, 203, 'Project Manager'),
(104, 209, 'Team Lead'),

(105, 205, 'Business Analyst'),
(105, 206, 'Consultant'),

(106, 207, 'QA Engineer'),
(107, 204, 'Database Developer'),
(108, 210, 'Support Engineer'),
(109, 209, 'AI Engineer'),
(110, 205, 'HR Consultant');

select * from employeeproject;


CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    city VARCHAR(50),
    email VARCHAR(100)
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    emp_id INT,
    order_date DATE,
    amount DECIMAL(10,2),

    FOREIGN KEY(customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY(emp_id) REFERENCES Employess(emp_id)
);
