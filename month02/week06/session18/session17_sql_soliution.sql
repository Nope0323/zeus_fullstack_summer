CREATE TABLE IF NOT EXISTS Book (
    title TEXT,
    director TEXT,
    published_year INTEGER);
  
CREATE TABLE IF NOT EXISTS Book_Review(
	Book_reviewer TEXT,
	Location TEXT,
	review_number INTEGER);
	
CREATE TABLE IF NOT EXISTS Greenhouse(
	Temperature INTEGER,
	Measurement_date TEXT,
	Measurement_Time INTEGER);

CREATE TABLE IF NOT EXISTS users(
	Id INTEGER,
	first_name TEXT,
	surname text,
	salary INTEGER);

	

--insert data
INSERT INTO users  VALUES(1 ,'Rolf', 'Smith' ,55000);
INSERT INTO users  VALUES(2 ,'Bob', 'Smith' ,45000);
INSERT INTO users  VALUES(3 ,'Anne', 'Pun' ,87000);

SELECT * FROM users;

--id only

SELECT  surname, salary from users;

--first_name, surename from
SELECT  surname, salary FROM users;

--WHERE clause

SELECT * FROM users;
SELECT * FROM users WHERE first_name ='John';
SELECT * FROM users WHERE surname = 'Smith';
SELECT * FROM users WHERE first_name ='Anne';
SELECT salary  FROM users WHERE first_name ='Anne';

SELECT * FROM users WHERE salary >5000;
--sql Comparison operators
--(<) ---lower than
--(>) ---Greater than
--(<=) ---lower than or equal to
--(>=) ---Greater than or equal to
--(=) ---exactly equal to
--(!=) ---not equal to
--(<>) ---not equal to


select * from users where surname  = 'Smith' and salary>50000
select * from users where salary  > 50000 or salary<40000