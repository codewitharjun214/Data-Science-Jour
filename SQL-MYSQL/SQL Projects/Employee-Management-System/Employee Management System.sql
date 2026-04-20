CREATE DATABASE Employee_Management_System;
USE Employee_Management_System;

-- Job Department 

CREATE TABLE JobDepartment (
    JobID INT PRIMARY KEY,
    JobTitle VARCHAR(100),
    Department VARCHAR(100),
    Location VARCHAR(100),
    SalaryRange VARCHAR(50)
);


ALTER TABLE JobDepartment
CHANGE JobTitle JobDept VARCHAR(100);
ALTER TABLE JobDepartment
CHANGE Department JobTitle VARCHAR(100);
select * from JobDepartment;
ALTER TABLE JobDepartment
CHANGE Location Description VARCHAR(100);

SELECT * FROM JobDepartment;

-- Employee Table 


CREATE TABLE Employee (
    EmpID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Gender VARCHAR(10),
    Age INT,
    ContactAddress VARCHAR(255),
    EmpEmail VARCHAR(100),
    EmpPass VARCHAR(100),
    JobID INT,
    FOREIGN KEY (JobID) REFERENCES JobDepartment(JobID)
);

SELECT * FROM employee;

-- Salary_Bonus Table

CREATE TABLE Salary_Bonus (
    SalaryID INT PRIMARY KEY,
    JobID INT,
    Amount INT,
    Annual INT,
    Bonus INT,
    FOREIGN KEY (JobID) REFERENCES JobDepartment(JobID)
);

SELECT * FROM Salary_Bonus;

-- Qualification Table

CREATE TABLE Qualification (
    QualID INT PRIMARY KEY,
    EmpID INT,
    Position VARCHAR(100),
    Requirements VARCHAR(255),
    Date_In DATE,
    FOREIGN KEY (EmpID) REFERENCES Employee(EmpID)
);

SELECT * FROM Qualification;

-- Leaves Table

CREATE TABLE Leaves (
    LeaveID INT PRIMARY KEY,
    EmpID INT,
    Date DATE,
    Reason VARCHAR(255),
    FOREIGN KEY (EmpID) REFERENCES Employee(EmpID)
);

SELECT * FROM Leaves;

-- Payroll Table

CREATE TABLE Payroll (
    PayrollID INT PRIMARY KEY,
    EmpID INT,
    JobID INT,
    SalaryID INT,
    LeaveID INT,
    Date DATE,
    Report VARCHAR(100),
    TotalAmount INT,
    FOREIGN KEY (EmpID) REFERENCES Employee(EmpID),
    FOREIGN KEY (JobID) REFERENCES JobDepartment(JobID),
    FOREIGN KEY (SalaryID) REFERENCES Salary_Bonus(SalaryID),
    FOREIGN KEY (LeaveID) REFERENCES Leaves(LeaveID)
);

SELECT * FROM Payroll;


-- 1. EMPLOYEE INSIGHTS
-- ●	How many unique employees are currently in the system?

SELECT COUNT(DISTINCT EmpID) AS unique_employees
FROM Employee;

-- ●	Which departments have the highest number of employees?

SELECT jd.JobTitle, COUNT(e.EmpID) AS total_employees
FROM Employee e
JOIN JobDepartment jd ON e.JobID = jd.JobID
GROUP BY jd.JobTitle
ORDER BY total_employees DESC;





-- ●	What is the average salary per department?

SELECT jd.JobTitle, AVG(sb.Amount) AS avg_salary
FROM Employee e
JOIN JobDepartment jd ON e.JobID = jd.JobID
JOIN Salary_Bonus sb ON jd.JobID = sb.JobID
GROUP BY jd.JobTitle;

-- ●	Who are the top 5 highest-paid employees?

SELECT e.EmpID, e.FirstName, e.LastName, sb.Amount AS salary
FROM Employee e
JOIN JobDepartment jd ON e.JobID = jd.JobID
JOIN Salary_Bonus sb ON jd.JobID = sb.JobID
ORDER BY sb.Amount DESC
LIMIT 5;

-- ●	What is the total salary expenditure across the company?

SELECT SUM(sb.Amount) AS total_salary_expenditure
FROM Salary_Bonus sb;

-- 2. JOB ROLE AND DEPARTMENT ANALYSIS

-- ● How many different job roles exist in each department?

SELECT jd.JobTitle AS Department, COUNT(DISTINCT jd.JobDept) AS total_roles
FROM JobDepartment jd
GROUP BY jd.JobTitle;

-- ● What is the average salary range per department?

SELECT jd.JobTitle AS Department, AVG(sb.Amount) AS avg_salary
FROM JobDepartment jd
JOIN Salary_Bonus sb ON jd.JobID = sb.JobID
GROUP BY jd.JobTitle;

-- ● Which job roles offer the highest salary?

SELECT jd.JobDept AS JobRole, MAX(sb.Amount) AS highest_salary
FROM JobDepartment jd
JOIN Salary_Bonus sb ON jd.JobID = sb.JobID
GROUP BY jd.JobDept
ORDER BY highest_salary DESC;

-- ● Which departments have the highest total salary allocation?

SELECT jd.JobTitle AS Department, SUM(sb.Amount) AS total_salary
FROM JobDepartment jd
JOIN Salary_Bonus sb ON jd.JobID = sb.JobID
GROUP BY jd.JobTitle
ORDER BY total_salary DESC;


-- 3. QUALIFICATION AND SKILLS ANALYSIS

-- ●	How many employees have at least one qualification listed?

SELECT COUNT(DISTINCT EmpID) AS qualified_employees
FROM Qualification;

-- ●	Which positions require the most qualifications?

SELECT Position, COUNT(*) AS total_qualifications
FROM Qualification
GROUP BY Position
ORDER BY total_qualifications DESC;



-- ●	Which employees have the highest number of qualifications?

SELECT e.EmpID, e.FirstName, e.LastName, COUNT(q.QualID) AS total_qualifications
FROM Employee e
JOIN Qualification q ON e.EmpID = q.EmpID
GROUP BY e.EmpID, e.FirstName, e.LastName
ORDER BY total_qualifications DESC;

-- 4. LEAVE AND ABSENCE PATTERNS
-- ●	Which year had the most employees taking leaves?

SELECT YEAR(Date) AS year, COUNT(DISTINCT EmpID) AS employees_on_leave
FROM Leaves
GROUP BY YEAR(Date)
ORDER BY employees_on_leave DESC;

-- ●	What is the average number of leave days taken by its employees per department?

SELECT jd.JobTitle AS Department, AVG(leave_count) AS avg_leaves
FROM (
    SELECT EmpID, COUNT(*) AS leave_count
    FROM Leaves
    GROUP BY EmpID
) l
JOIN Employee e ON l.EmpID = e.EmpID
JOIN JobDepartment jd ON e.JobID = jd.JobID
GROUP BY jd.JobTitle;

-- ●	Which employees have taken the most leaves?

SELECT e.EmpID, e.FirstName, e.LastName, COUNT(l.LeaveID) AS total_leaves
FROM Employee e
JOIN Leaves l ON e.EmpID = l.EmpID
GROUP BY e.EmpID, e.FirstName, e.LastName
ORDER BY total_leaves DESC;

-- ●	What is the total number of leave days taken company-wide?

SELECT COUNT(*) AS total_leave_days
FROM Leaves;


-- ●	How do leave days correlate with payroll amounts?

SELECT e.EmpID, 
       COUNT(l.LeaveID) AS total_leaves, 
       SUM(p.TotalAmount) AS total_payroll
FROM Employee e
LEFT JOIN Leaves l ON e.EmpID = l.EmpID
LEFT JOIN Payroll p ON e.EmpID = p.EmpID
GROUP BY e.EmpID
ORDER BY total_leaves DESC;


-- 5. PAYROLL AND COMPENSATION ANALYSIS
-- ●	What is the total monthly payroll processed?

SELECT MONTH(Date) AS month, YEAR(Date) AS year,
       SUM(TotalAmount) AS total_monthly_payroll
FROM Payroll
GROUP BY YEAR(Date), MONTH(Date)
ORDER BY year, month;

-- ●	What is the average bonus given per department?

SELECT jd.JobTitle AS Department, AVG(sb.Bonus) AS avg_bonus
FROM JobDepartment jd
JOIN Salary_Bonus sb ON jd.JobID = sb.JobID
GROUP BY jd.JobTitle;

-- ●	Which department receives the highest total bonuses?

SELECT jd.JobTitle AS Department, SUM(sb.Bonus) AS total_bonus
FROM JobDepartment jd
JOIN Salary_Bonus sb ON jd.JobID = sb.JobID
GROUP BY jd.JobTitle
ORDER BY total_bonus DESC
LIMIT 5 ;

-- ●	What is the average value of total_amount after considering leave deductions?

SELECT AVG(TotalAmount) AS avg_final_salary
FROM Payroll;



