-- =============================================================================
-- DAY 34: JOINS + GROUP BY + HAVING - SOLUTION
-- =============================================================================


-- =============================================================================
-- SECTION 1: USE DATABASE
-- =============================================================================

USE student_db;


-- =============================================================================
-- SECTION 2: SAMPLE DATA CHECK
-- =============================================================================

-- View employees table
SELECT * FROM employees;

-- View departments table
SELECT * FROM departments;


-- =============================================================================
-- SECTION 3: JOINS
-- =============================================================================

-- INNER JOIN (common data from both tables)
SELECT e.emp_name, e.salary, d.dept_name
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id;

-- LEFT JOIN (all employees + matching department)
SELECT e.emp_name, d.dept_name
FROM employees e
LEFT JOIN departments d
ON e.dept_id = d.dept_id;


-- =============================================================================
-- SECTION 4: AGGREGATE FUNCTIONS
-- =============================================================================

-- Total employees
SELECT COUNT(*) AS total_employees FROM employees;

-- Average salary
SELECT AVG(salary) AS avg_salary FROM employees;

-- Highest salary
SELECT MAX(salary) AS max_salary FROM employees;

-- Lowest salary
SELECT MIN(salary) AS min_salary FROM employees;


-- =============================================================================
-- SECTION 5: GROUP BY
-- =============================================================================

-- Count employees in each department
SELECT dept_id, COUNT(*) AS total_employees
FROM employees
GROUP BY dept_id;

-- Average salary per department
SELECT dept_id, AVG(salary) AS avg_salary
FROM employees
GROUP BY dept_id;


-- =============================================================================
-- SECTION 6: HAVING
-- =============================================================================

-- Departments having more than 1 employee
SELECT dept_id, COUNT(*) AS total
FROM employees
GROUP BY dept_id
HAVING COUNT(*) > 1;


-- =============================================================================
-- SECTION 7: COMBINED (JOIN + GROUP BY)
-- =============================================================================

-- Total employees in each department (with names)
SELECT d.dept_name, COUNT(e.emp_id) AS total_employees
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id
GROUP BY d.dept_name;

-- Highest salary per department
SELECT d.dept_name, MAX(e.salary) AS highest_salary
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id
GROUP BY d.dept_name;