
-- create database 

CREATE DATABASE RIVISION;

USE RIVISION;

-- create table

create table student(
id int primary key,
name varchar (50),
marks int(50),
city varchar(50)
);

select * from student;

insert into student
values
(1,"Arjun",95,"Pune"),
(2,"Shyam",85,"Mumbai"),
(3,"Ram",82,"Noida"),
(4,"Shiv",75,"Hydrabad");

select * from student;

alter table student
add column grade varchar(50) not null;

select * from student;

update student 
set grade = "A"
where id = 1;

update student 
set grade = "A"
where id = 2;

update student
set grade = "B"
where id = 3;

update student
set grade = "C"
where id = 4;

select * from student;

select city from student;

select * from student
where city = "Pune";

select * from student 
where marks >= 80;

select * from student 
where marks >= 80 and city = "Pune";

select * from student 
where marks >= 90 and city = "Pune"; 

select * from student 
where marks between 80 and 90;

select * from student 
where city in ("Pune","Mumbai");

select * from student 
where city not in ("Noida","Pune");

select * from student
where marks > 75 limit 3;

select * from student
order by city asc;

select * from student 
order by marks desc limit 2;

select * from student 
order by id desc;

select min(marks) from student;

select max(marks) from student;

select avg(marks) from student;

select count(id) from student;

SELECT city,
COUNT(id)
FROM student
GROUP BY city;

select city , marks,
count(id)
from student
group by city , marks;

select city ,avg(marks)
from student
group by city;

select city ,avg(marks)
from student 
group by city
order by avg(Marks)desc;

select marks ,count(name)
from student 
group by marks
order by marks;

select city , count(id)
from student
group by city 
having max(marks) > 90;

-- systax to write clause properly 

select city 
from student 
where grade ="A" 
group by city 
having max(marks) >= 80
order by city asc;

update student 
set grade = "0"
where grade = "A";

set sql_safe_updates = 0;

select * from student;

update student 
set grade = "B"
where marks between 80 and 90 ;

update student 
set grade = "A"
where marks > 90 ;

select * from student ;

insert into student 
(id,name,marks,city,grade)
values
(5,"sadashiv",70,"Goa","C"),
(6,"sada",72,"Goa","C"),
(7,"adesh",60,"Banglore","C");

select * from student;

update student 
set grade = "C"
where marks between 70 and 80 ;

update student 
set grade = "F"
where marks < 70;

select * from student;

update student 
set marks = marks+1;

select * from student;

delete from student 
where marks < 70 ;

select * from student;

select count(id) from student;

create table dept(
id int primary key,
name varchar(50)
);

insert into dept
values
(101,"IT"),
(102,"Comp");

create table teacher(
id int primary key ,
name varchar(50),
dept_id int ,
foreign key (dept_id) references dept(id)
on update cascade
on delete cascade
);

insert into teacher 
values
(101,"Adam",101),
(102,"Bob",102);

select * from student;
select * from dept;
select * from teacher;

update dept
set id  = 103
where id = 101;

select * from teacher;

alter table student 
add column age int not null;

select * from student;

alter table student
drop column age ;

alter table student 
rename to College;

select * from college;

alter table college
change marks newmarks int;

alter table college 
add column age int not null default 19;


--- For inner Join

create table student(
id int primary key,
name varchar(50)
);

insert into student 
values 
(101,"Arj"),
(102,"Sah");

select * from student;

create table course(
id int primary key,
course varchar(50)
);

insert into course 
values 
(102,"math"),
(103,"Science");

select * from course;

select * from student
inner join course 
on student.id = course.id;

select * 
from student
left join course
on student.id = course.id; 

select * 
from student
right join course
on student.id = course.id; 

select * 
from student
left join course
on student.id = course.id
union
select * 
from student
right join course
on student.id = course.id; 


select * 
from student 
left join course
on student.id = course.id
where course.id is null ;

select * 
from student 
right join course
on student.id = course.id
where student.id is null ;


-- Subquery 

select name,grade
from college 
where newmarks > ( select avg(newmarks) from college);

select * from college;

create view view1 as
select id,name,newmarks
from college ;

select * from view1;

use rivision;


