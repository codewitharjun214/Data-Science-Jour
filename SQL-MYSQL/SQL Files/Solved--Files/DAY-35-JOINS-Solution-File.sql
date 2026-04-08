-- =============================================================================
-- DAY 35: ADVANCED SQL (SUBQUERY, VIEW, INDEX) - SOLUTION
-- =============================================================================


-- =============================================================================
-- SECTION 1: USE DATABASE
-- =============================================================================

USE student_db;


-- =============================================================================
-- SECTION 2: SUBQUERIES
-- =============================================================================

-- Find employees earning more than average salary
SELECT emp_name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Find employees from department 'IT'
SELECT emp_name
FROM employees
WHERE dept_id = (
    SELECT dept_id 
    FROM departments 
    WHERE dept_name = 'IT'
);


-- =============================================================================
-- SECTION 3: VIEW
-- =============================================================================

-- Create a view for high salary employees
CREATE VIEW high_salary_emp AS
SELECT emp_name, salary
FROM employees
WHERE salary > 50000;

-- View data from view
SELECT * FROM high_salary_emp;


-- =============================================================================
-- SECTION 4: INDEX
-- =============================================================================

-- Create index on emp_name (for faster search)
CREATE INDEX idx_emp_name
ON employees(emp_name);


-- =============================================================================
-- SECTION 5: PRACTICE QUERIES
-- =============================================================================

-- Employees with highest salary
SELECT emp_name, salary
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);

-- Count employees in IT department
SELECT COUNT(*)
FROM employees
WHERE dept_id = (
    SELECT dept_id FROM departments WHERE dept_name = 'IT'
);


-- =============================================================================
-- SECTION 6: OPTIONAL CLEANUP
-- =============================================================================

-- Drop view
-- DROP VIEW high_salary_emp;

-- Drop index
-- DROP INDEX idx_emp_name ON employees;