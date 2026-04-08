-- =====================================================
-- SQL MASTER FILE (FINAL CLEAN VERSION)
-- =====================================================

-- =========================
-- 1. DATABASE
-- =========================
CREATE DATABASE IF NOT EXISTS ak_sql_master_db;
USE ak_sql_master_db;

-- =========================
-- 2. CLEAN START (IMPORTANT)
-- =========================
DROP TABLE IF EXISTS ak_employees;
DROP TABLE IF EXISTS ak_departments;

-- =========================
-- 3. CREATE TABLES
-- =========================

-- Parent Table
CREATE TABLE ak_departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50) UNIQUE,
    location VARCHAR(50)
);

-- Child Table
CREATE TABLE ak_employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50) NOT NULL,
    salary DECIMAL(10,2),
    dept_id INT,
    email VARCHAR(100) UNIQUE,
    FOREIGN KEY (dept_id) REFERENCES ak_departments(dept_id)
);

-- =========================
-- 4. INSERT DATA
-- =========================

INSERT INTO ak_departments (dept_id, dept_name, location) VALUES
(1, 'HR', 'Pune'),
(2, 'IT', 'Mumbai'),
(3, 'Finance', 'Bangalore'),
(4, 'Marketing', 'Delhi');

INSERT INTO ak_employees (emp_id, emp_name, salary, dept_id, email) VALUES
(101, 'Arjun', 50000, 2, 'arjun@gmail.com'),
(102, 'Rahul', 60000, 2, 'rahul@gmail.com'),
(103, 'Sneha', 45000, 1, 'sneha@gmail.com'),
(104, 'Priya', 70000, 3, 'priya@gmail.com'),
(105, 'Amit', 30000, 4, 'amit@gmail.com');

-- =========================
-- 5. BASIC SELECT
-- =========================

SELECT * FROM ak_employees;
SELECT emp_name, salary FROM ak_employees;

-- =========================
-- 6. WHERE CONDITIONS
-- =========================

SELECT * FROM ak_employees WHERE salary > 50000;
SELECT * FROM ak_employees WHERE salary > 40000 AND dept_id = 2;
SELECT * FROM ak_employees WHERE salary BETWEEN 40000 AND 70000;
SELECT * FROM ak_employees WHERE dept_id IN (1,2);
SELECT * FROM ak_employees WHERE emp_name LIKE 'A%';

-- =========================
-- 7. ORDER BY
-- =========================

SELECT * FROM ak_employees ORDER BY salary ASC;
SELECT * FROM ak_employees ORDER BY salary DESC;

-- =========================
-- 8. AGGREGATE FUNCTIONS
-- =========================

SELECT COUNT(*) AS total_employees FROM ak_employees;
SELECT AVG(salary) AS avg_salary FROM ak_employees;
SELECT MAX(salary) AS max_salary FROM ak_employees;
SELECT MIN(salary) AS min_salary FROM ak_employees;
SELECT SUM(salary) AS total_salary FROM ak_employees;

-- =========================
-- 9. GROUP BY + HAVING
-- =========================

SELECT dept_id, COUNT(*) AS total_employees
FROM ak_employees
GROUP BY dept_id;

SELECT dept_id, COUNT(*) AS total
FROM ak_employees
GROUP BY dept_id
HAVING COUNT(*) > 1;

SELECT dept_id, MAX(salary) AS highest_salary
FROM ak_employees
GROUP BY dept_id;

-- =========================
-- 10. JOINS
-- =========================

-- INNER JOIN
SELECT e.emp_name, d.dept_name
FROM ak_employees e
INNER JOIN ak_departments d
ON e.dept_id = d.dept_id;

-- LEFT JOIN
SELECT e.emp_name, d.dept_name
FROM ak_employees e
LEFT JOIN ak_departments d
ON e.dept_id = d.dept_id;

-- =========================
-- 11. UPDATE
-- =========================

UPDATE ak_employees
SET salary = 55000
WHERE emp_id = 101;

-- =========================
-- 12. DELETE
-- =========================

DELETE FROM ak_employees
WHERE emp_id = 105;

-- =========================
-- 13. ALTER TABLE
-- =========================

ALTER TABLE ak_employees ADD phone VARCHAR(15);
ALTER TABLE ak_employees MODIFY salary DECIMAL(12,2);
ALTER TABLE ak_employees DROP COLUMN phone;

-- =========================
-- 14. SUBQUERY
-- =========================

SELECT emp_name, salary
FROM ak_employees
WHERE salary > (SELECT AVG(salary) FROM ak_employees);

-- =========================
-- 15. VIEW
-- =========================

CREATE VIEW ak_high_salary_emp AS
SELECT emp_name, salary
FROM ak_employees
WHERE salary > 50000;

SELECT * FROM ak_high_salary_emp;

-- =========================
-- 16. INDEX
-- =========================

CREATE INDEX ak_idx_emp_name
ON ak_employees(emp_name);

-- =========================
-- 17. CLEANUP (OPTIONAL)
-- =========================

-- DROP TABLE ak_employees;
-- DROP TABLE ak_departments;
-- DROP DATABASE ak_sql_master_db;

-- =====================================================
-- END OF FILE
-- ===================================================== 