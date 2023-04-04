CREATE DATABASE Exercise1;
CREATE TABLE exercise1.EMP_1 (EMP_NUM CHAR(3) NOT NULL, EMP_Lname VARCHAR(15) NULL, EMP_Fname VARCHAR(15) NULL, EMP_INITIAL CHAR(1) NULL, 
	EMP_HIREDATE DATE NULL, JOB_CODE CHAR(3) NULL, PRIMARY KEY (EMP_NUM));
INSERT INTO exercise1.emp_1 (EMP_NUM, EMP_Lname, EMP_Fname, EMP_INITIAL, EMP_HIREDATE, JOB_CODE) VALUES ('111', 'Red', 'Jeralph', 'O', '2001-09-18', '502');
INSERT INTO exercise1.emp_1 (EMP_NUM, EMP_Lname, EMP_Fname, EMP_INITIAL, EMP_HIREDATE, JOB_CODE) VALUES ('112', 'Yumang', 'James Bernard', 'G', '2003-07-25', '502');
INSERT INTO exercise1.emp_1 (EMP_NUM, EMP_Lname, EMP_Fname, EMP_INITIAL, EMP_HIREDATE, JOB_CODE) VALUES ('113', 'Banta', 'Jan Rusell', 'V', '2002-07-19', '502');
TRUNCATE TABLE exercise1.emp_1
INSERT INTO exercise1.emp_1 (EMP_NUM, EMP_Lname, EMP_Fname, EMP_INITIAL, EMP_HIREDATE, JOB_CODE) 
VALUES ('101', 'Nevas', 'John', 'G', '1994-11-08', '502'),
('102', 'Senior', 'David', 'H', '1987-07-12', '501'),
('103', 'Arbos', 'June', 'E', '1996-12-01', '500'),
('104', 'Ramoras', 'Anne', 'K', '1998-11-15', '501'),
('105', 'Joson', 'Alice', 'P', '1993-02-01', '502'),
('106', 'Smith', 'William', 'D', '1990-06-23', '500'),
('107', 'Alonso', 'Maria', 'F', '1991-10-10', '500'),
('108', 'Washington', 'Raf', 'S', '1989-08-22', '501'),
('109', 'Field', 'Larry', 'W', '1999-07-18', '501');
UPDATE exercise1.emp_1 SET JOB_CODE = '502' WHERE EMP_NUM = '106';
DELETE from exercise1.emp_1 WHERE EMP_NUM = '106';