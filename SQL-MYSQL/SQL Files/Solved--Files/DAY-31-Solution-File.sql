-- =============================================================================
-- DAY 31: GETTING STARTED WITH SQL & DATABASES (SOLVED)
-- =============================================================================


-- =============================================================================
-- SECTION 7: VIEW ALL DATABASES
-- =============================================================================

-- Show all databases in MySQL
SHOW DATABASES;


-- =============================================================================
-- SECTION 8: CREATE DATABASE
-- =============================================================================

-- Create a new database
CREATE DATABASE student_db;


-- =============================================================================
-- SECTION 9: USE DATABASE
-- =============================================================================

-- Select (use) the database to work on it
USE student_db;


-- =============================================================================
-- SECTION 10: VERIFY CURRENT DATABASE
-- =============================================================================

-- Check which database is currently selected
SELECT DATABASE();


-- =============================================================================
-- SECTION 11: CREATE ANOTHER DATABASE
-- =============================================================================

-- Create one more database
CREATE DATABASE college_db;


-- =============================================================================
-- SECTION 12: SWITCH TO ANOTHER DATABASE
-- =============================================================================

-- Switch to college_db
USE college_db;


-- =============================================================================
-- SECTION 13: DROP DATABASE
-- =============================================================================

-- Delete database permanently (be careful ⚠️)
DROP DATABASE college_db;


-- =============================================================================
-- EXTRA PRACTICE (VERY IMPORTANT)
-- =============================================================================

-- Create multiple databases
CREATE DATABASE company_db;
CREATE DATABASE test_db;

-- Switch between databases
USE company_db;
USE student_db;

-- Check current database again
SELECT DATABASE();


-- =============================================================================
-- SECTION 16: PRACTICE TASKS (SOLVED)
-- =============================================================================

-- TASK 1: Create database
CREATE DATABASE IF NOT EXISTS student_db;

-- TASK 2: Use database
USE student_db;

-- TASK 3: Verify database
SELECT DATABASE();