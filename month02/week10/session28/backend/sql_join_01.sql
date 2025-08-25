CREATE DATABASE employees_db;

CREATE TABLE departments (
department_id INT PRIMARY KEY,
department_name VARCHAR(50)
);
-- Ажилтны мэдээллийг хадгалах хүснэгт
CREATE TABLE employees (
employee_id INT PRIMARY KEY,
first_name VARCHAR(50),
last_name VARCHAR(50),
department_id INT,
FOREIGN KEY (department_id) REFERENCES departments(department_id)
);
-- Төслийн мэдээллийг хадгалах хүснэгт
CREATE TABLE projects (
project_id INT PRIMARY KEY,
project_name VARCHAR(100),
lead_employee_id INT,
FOREIGN KEY (lead_employee_id) REFERENCES employees(employee_id)
);

INSERT INTO employees (employee_id, first_name, last_name, department_id)
VALUES
(1, 'Alice', 'Smith', 1),
(2, 'Bob', 'Johnson', 2),
(3, 'Charlie', 'Brown', 1),
(4, 'Diana', 'Prince', 3),
(5, 'Ethan', 'Hunt', NULL), -- Ethan ямар ч хэлтэст харьяалагддаггүй
(6, 'Fiona', 'Glenanne', 2);
-- departments хүснэгтэд өгөгдөл оруулах
INSERT INTO departments (department_id, department_name) VALUES
(1, 'Engineering'),
(2, 'Marketing'),
(3, 'Human Resources'),
(4, 'Sales'); 
-- Sales хэлтэст хараахан ажилтан байхгүй
-- projects хүснэгтэд өгөгдөл оруулах
INSERT INTO projects (project_id, project_name, lead_employee_id) VALUES
(101, 'Website Redesign', 2),
(102, 'Mobile App Launch', 1),
(103, 'Security Audit', 6),
(104, 'New Office Setup', NULL); -- Энэ төсөл удирдагчгүй

--inner join
select e.last_name, e.first_name, d.department_id  
from  employees e  
inner join departments d     ON d.department_id  = e.department_id ;