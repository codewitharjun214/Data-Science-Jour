-- ============================================================
-- PROJECT: Student Performance & Course Analytics System
-- TOOL: MySQL
-- ============================================================

-- ============================================================
-- STEP 1: CREATE DATABASE
-- ============================================================

CREATE DATABASE student_analytics;
USE student_analytics;

-- ============================================================
-- STEP 2: CREATE TABLES
-- ============================================================

-- Department Table
-- Stores department information
CREATE TABLE department (
    dept_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(100)
);

-- Student Table
-- Each student belongs to one department
CREATE TABLE student (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    student_name VARCHAR(100),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES department(dept_id)
);

-- Courses Table
-- Stores all available courses
CREATE TABLE courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100)
);

-- Enrollments Table
-- Handles many-to-many relationship between students and courses
CREATE TABLE enrollments (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    marks INT,
    FOREIGN KEY (student_id) REFERENCES student(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- ============================================================
-- STEP 3: INSERT DATA
-- IMPORTANT: Follow order (Parent → Child)
-- ============================================================

-- Insert Departments
INSERT INTO department (dept_name) VALUES
('Computer Science'),
('Mechanical'),
('Civil');

-- Insert Students
INSERT INTO student (student_name, dept_id) VALUES
('Arjun', 1),
('Rohit', 2),
('Sneha', 1),
('Priya', 3),
('Amit', 2);

-- Insert Courses
INSERT INTO courses (course_name) VALUES
('SQL'),
('Java'),
('Python'),
('Data Structures');

-- Insert Enrollments
INSERT INTO enrollments (student_id, course_id, marks) VALUES
(1, 1, 90),
(1, 2, 85),
(2, 1, 70),
(3, 3, 88),
(4, 2, 60),
(5, 4, 75),
(3, 1, 95);

-- ============================================================
-- STEP 4: ANALYTICAL QUERIES
-- ============================================================

-- Q1: Students per department
SELECT d.dept_name, COUNT(s.student_id) AS total_students
FROM department d
LEFT JOIN student s ON d.dept_id = s.dept_id
GROUP BY d.dept_name;

-- Q2: Course popularity
SELECT c.course_name, COUNT(e.student_id) AS total_enrollments
FROM courses c
JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_name
ORDER BY total_enrollments DESC;

-- Q3: Student with department
SELECT s.student_name, d.dept_name
FROM student s
JOIN department d ON s.dept_id = d.dept_id;

-- Q4: Average marks per course
SELECT c.course_name, AVG(e.marks) AS avg_marks
FROM courses c
JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_name;

-- Q5: Students scoring more than 85
SELECT s.student_name, c.course_name, e.marks
FROM student s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id
WHERE e.marks > 85;

-- Q6: Number of courses per student
SELECT s.student_name, COUNT(e.course_id) AS total_courses
FROM student s
LEFT JOIN enrollments e ON s.student_id = e.student_id
GROUP BY s.student_name;

-- Q7: Students enrolled in more than 1 course
SELECT s.student_name, COUNT(e.course_id) AS course_count
FROM student s
JOIN enrollments e ON s.student_id = e.student_id
GROUP BY s.student_name
HAVING COUNT(e.course_id) > 1;

-- Q8: Department-wise average marks
SELECT d.dept_name, AVG(e.marks) AS avg_marks
FROM department d
JOIN student s ON d.dept_id = s.dept_id
JOIN enrollments e ON s.student_id = e.student_id
GROUP BY d.dept_name;

-- Q9: Top performing student
SELECT s.student_name, SUM(e.marks) AS total_marks
FROM student s
JOIN enrollments e ON s.student_id = e.student_id
GROUP BY s.student_name
ORDER BY total_marks DESC
LIMIT 1;

-- Q10: Most popular course
SELECT c.course_name, COUNT(e.student_id) AS enrollment_count
FROM courses c
JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_name
ORDER BY enrollment_count DESC
LIMIT 1;

-- Q11: Students scoring above average
SELECT s.student_name, e.marks
FROM student s
JOIN enrollments e ON s.student_id = e.student_id
WHERE e.marks > (SELECT AVG(marks) FROM enrollments);

-- Q12: Department stats (students + enrollments)
SELECT d.dept_name,
       COUNT(DISTINCT s.student_id) AS total_students,
       COUNT(e.course_id) AS total_enrollments
FROM department d
LEFT JOIN student s ON d.dept_id = s.dept_id
LEFT JOIN enrollments e ON s.student_id = e.student_id
GROUP BY d.dept_name;

-- Q13: Students not enrolled in any course
SELECT s.student_name
FROM student s
LEFT JOIN enrollments e ON s.student_id = e.student_id
WHERE e.course_id IS NULL;

-- Q14: Course-wise highest and lowest marks
SELECT c.course_name,
       MAX(e.marks) AS highest_marks,
       MIN(e.marks) AS lowest_marks
FROM courses c
JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_name;

-- Q15: Course ranking by average marks
SELECT c.course_name, AVG(e.marks) AS avg_marks
FROM courses c
JOIN enrollments e ON c.course_id = e.course_id
GROUP BY c.course_name
ORDER BY avg_marks DESC;

-- ============================================================
-- END OF PROJECT
-- ============================================================

-- KEY CONCEPTS USED:
-- ✔ Database Design
-- ✔ Primary & Foreign Keys
-- ✔ Joins (INNER, LEFT)
-- ✔ Aggregation (COUNT, AVG, SUM)
-- ✔ GROUP BY & HAVING
-- ✔ Subqueries
-- ✔ Real-world analytics queries