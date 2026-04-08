-- =============================================================================
-- DAY 32: DATA DEFINITION LANGUAGE (DDL) - SOLUTION
-- =============================================================================


-- =============================================================================
-- SECTION 4: DATABASE SELECTION
-- =============================================================================

-- Select database to work on
USE student_db;


-- =============================================================================
-- SECTION 6: CREATE TABLE
-- =============================================================================

-- Create Departments Table
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,       -- unique id for department
    dept_name VARCHAR(50)          -- department name
);


-- Create Employees Table
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,        -- unique employee id
    emp_name VARCHAR(50),          -- employee name
    salary INT,                    -- salary
    dept_id INT                    -- department id
);


-- =============================================================================
-- SECTION 7: ALTER TABLE
-- =============================================================================

-- Add new column (email) in employees table
ALTER TABLE employees
ADD email VARCHAR(100);


-- Modify column datatype (salary INT → BIGINT)
ALTER TABLE employees
MODIFY salary BIGINT;


-- Drop column (remove email column)
ALTER TABLE employees
DROP COLUMN email;


-- =============================================================================
-- SECTION 8: TRUNCATE TABLE
-- =============================================================================

-- Delete all data but keep table structure
TRUNCATE TABLE employees;


-- =============================================================================
-- SECTION 9: RENAME TABLE
-- =============================================================================

-- Rename employees table to Staff
RENAME TABLE employees TO staff;


-- =============================================================================
-- SECTION 10: DROP TABLE
-- =============================================================================

-- Delete table permanently
DROP TABLE staff;