CREATE TABLE IF NOT EXISTS Students(
	name TEXT,
	major TEXT,
	gpa REAL);
	
INSERT INTO Students  VALUES('Alice', 'Computer Science' ,3.8);
INSERT INTO Students  VALUES('Bob', 'Art' ,3.2);
INSERT INTO Students  VALUES('Charlie', 'Computer Science' ,3.5);

SELECT * FROM major FROM students;
SELECT * FROM students;
SELECT * FROM students WHERE major = 'art';
SELECT * FROM students WHERE gpa <3.6;

CREATE TABLE IF NOT EXISTS Products(
	products_name TEXT,
	products_gategory TEXT,
	price REAL);


INSERT INTO Products (products_name, products_gategory, price)  VALUES
('Aplpes', 'Fruit', 1.50),
('Bread', 'Bakery', 2.25),
('Milk ', 'Dairy', 3.00),
('Cheese ', 'Dairy',5.50);

UPDATE Products  SET price = 1.75 WHERE products_name = 'Apples';
UPDATE  Products  SET price = price 0.9 WHERE products_gategory = 'Dairy';

INSERT  into Products (products_name, products_gategory, price ) VALUES
('Aaruul', 'Dairy', 10.0)

DELETE  FROM Products  WHERE product_name = 'Aaruul' and price =10.0;

--table ustgah
DROP TABLE Products ;

CREATE TABLE IF NOT EXISTS icode_students(
	surname TEXT,
	name TEXT,
	age INTEGER,
	phone_number INTEGER);
	
INSERT INTO icode_students (surname, name, age,phone_number)  VALUES
('Аюурзана', 'Батсуурь',23, 99698703),
('Төмөрбаатар', 'Оргил',20, 88120291),
('Баясгалан', 'Булган',28, 99069851),
('Энхцэцэг', 'Болд-Эрдэнэ',23, 80230177),
('Нацагдорж', 'Марал',20, 99861554),
('Цагаанбанди', 'Анхбаяр',29, 99090105);

SELECT *

UPDATE icode_students SET phone_number='99119911'  WHERE name ='Болд-Эрдэнэ' ;
UPDATE icode_students SET phone_number='88118811'  WHERE name ='Булган';


UPDATE icode_students SET age=age -2 WHERE name ='Марал';
UPDATE icode_students SET age=age-2  WHERE name ='Булган';

SELECT * FROM  icode_students 

DELETE  FROM icode_students ;
