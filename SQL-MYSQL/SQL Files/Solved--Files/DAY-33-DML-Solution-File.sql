-- =============================================================================
-- DAY 33: DATA MANIPULATION LANGUAGE (DML) - SOLUTION
-- =============================================================================


-- =============================================================================
-- SECTION 1: USE DATABASE
-- =============================================================================

USE student_db;


-- =============================================================================
-- SECTION 2: INSERT DATA
-- =============================================================================

-- Insert data into departments table
INSERT INTO departments (dept_id, dept_name) VALUES
(1, 'HR'),
(2, 'IT'),
(3, 'Finance');

-- Insert data into employees table
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    salary INT,
    dept_id INT
);

INSERT INTO employees (emp_id, emp_name, salary, dept_id) VALUES
(101, 'Arjun', 50000, 2),
(102, 'Rahul', 60000, 2),
(103, 'Sneha', 45000, 1),
(104, 'Priya', 70000, 3);


-- =============================================================================
-- SECTION 3: SELECT DATA
-- =============================================================================

-- View all data
SELECT * FROM employees;

-- View specific columns
SELECT emp_name, salary FROM employees;

-- Filter using WHERE
SELECT * FROM employees WHERE salary > 50000;

-- Multiple conditions
SELECT * FROM employees WHERE salary > 40000 AND dept_id = 2;

-- Pattern matching
SELECT * FROM employees WHERE emp_name LIKE 'A%';


-- =============================================================================
-- SECTION 4: UPDATE DATA
-- =============================================================================

-- Update salary of one employee
UPDATE employees
SET salary = 55000
WHERE emp_id = 101;

-- Update multiple rows
SET SQL_SAFE_UPDATES = 0;

UPDATE employees
SET salary = salary + 5000
WHERE dept_id = 2;


-- =============================================================================
-- SECTION 5: DELETE DATA
-- =============================================================================

-- Delete one record
DELETE FROM employees
WHERE emp_id = 104;

-- Delete based on condition
DELETE FROM employees
WHERE salary < 40000;


-- =============================================================================
-- SECTION 6: PRACTICE QUERIES
-- =============================================================================

-- Find employees from IT department
SELECT * FROM employees WHERE dept_id = 2;

-- Find highest salary
SELECT MAX(salary) AS highest_salary FROM employees;

-- Count total employees
SELECT COUNT(*) AS total_employees FROM employees;