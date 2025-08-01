CREATE TABLE IF NOT EXISTS users(
	Id INTEGER,
	first_name TEXT,
	surname text,
	salary INTEGER,
	age INTEGER);
	
INSERT INTO users  VALUES(1 ,'Rolf', 'Smith' ,55000, 57);
INSERT INTO users  VALUES(2 ,'Bob', 'Smith' ,45000, 18);
INSERT INTO users  VALUES(3 ,'Anne', 'Pun' ,87000, 49);
INSERT INTO users  VALUES(4 ,'Elisabeth', 'Lee' ,90000, 29);

SELECT * FROM users WHERE salary >60000;

SELECT * FROM users WHERE salary >80000 or age>50;

SELECT * FROM users WHERE salary >35000 and age<20 OR salary >80000 and age<30 ;




