

CREATE DATABASE ak_private_limited;

USE ak_private_limited;

CREATE TABLE employee (

id INT PRIMARY KEY,
emp_name VARCHAR(50),
salary INT

);

INSERT INTO employee
(id,emp_name,salary)
VALUES
(1,"adam",25000),
(2,"bob", 30000),
(3,"casey",40000);

SELECT * FROM  employee;


-- Practice 

USE ak_private_limited; 


INSERT INTO employee
(id,emp_name,salary)
VALUES
(4,"sam",25000),
(5,"bobby", 30000),
(6,"caseey",40000);



-- Lets Start DTL Commands 

START TRANSACTION;

UPDATE employee SET salary = 35000 WHERE id = 1;

SAVEPOINT sp1;

DELETE FROM employee WHERE id = 2;

SAVEPOINT sp2;

UPDATE employee SET salary = 50000 WHERE id = 3;

ROLLBACK TO sp2;

ROLLBACK TO sp1;

COMMIT;

SELECT * FROM employee;

--- DCL Commands: GRANT & REVOKE  

-- Step 1: Create user first
CREATE USER 'user1'@'localhost' IDENTIFIED BY 'password123';

-- Step 2: Grant permission
GRANT SELECT ON ak_private_limited.employee TO 'user1'@'localhost';

--- Common Aggregate Functions
-- 1. COUNT()
-- Counts number of rows

SELECT COUNT(*) FROM employee;

SELECT COUNT(emp_name) FROM employee;

-- 2. SUM()

SELECT SUM(salary) FROM employee;

-- 3. AVG()
-- Finds average

SELECT AVG(salary) FROM employee;

-- MAX()

-- Highest value

SELECT MAX(salary) FROM employee;

--- 5. MIN()
--- Lowest value

SELECT MIN(salary) FROM employee;


-- TASK TO FIND EMP ID FROM NAME AND SALARY 

SELECT id FROM employee 
WHERE emp_name = 'adam' AND salary = 35000;


-- Group by and order by combine 

SELECT salary, COUNT(*) 
FROM employee
GROUP BY salary
ORDER BY salary DESC;

-- PRACTICE QUESTIONS 

SELECT * FROM employee ;

-- ON DELETE CASCADE
-- ON UPDATE CASCADE


