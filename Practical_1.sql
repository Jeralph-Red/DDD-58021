CREATE DATABASE ABC_Computer;
CREATE TABLE ABC_Computer.Computer (SerialNumber INT Primary key Not null,Make Text(12) Not null,Model Text(24) Not null,
ProcessorType Text(24),ProcessorSpeed Float(2) Not null,MainMemory Text(15) Not null,DiskSize Text(15) Not  null);

SELECT*FROM abc_computer.computer;
INSERT INTO ABC_Computer.Computer(SerialNumber, Make, Model, ProcessorType, ProcessorSpeed, MainMemory, DiskSize)
	VALUES('9871234','HP', 'Pavillion 500-210qe', 'Intel i5-4530', '3.00', '6.0 Gigabytes', '1.0 Tbytes'),
	('9871245','HP', 'Pavillion 500-210qe', 'Intel i5-4531', '3.00', '6.0 Gigabytes', '1.0 Tbytes'),
	('9871256','HP', 'Pavillion 500-210qe', 'Intel i5-4532', '3.00', '6.0 Gigabytes', '1.0 Tbytes'),
	('9871267','HP', 'Pavillion 500-210qe', 'Intel i5-4533', '3.00', '6.0 Gigabytes', '1.0 Tbytes'),
	('9871278','HP', 'Pavillion 500-210qe', 'Intel i5-4534', '3.00', '6.0 Gigabytes', '1.0 Tbytes'),
	('9871289','HP', 'Pavillion 500-210qe', 'Intel i5-4535', '3.00', '6.0 Gigabytes', '1.0 Tbytes'),
	('6541001','Dell', 'Optiflex 9020', 'Intel i7-4770', '3.00', '8.0 Gigabytes', '1.0 Tbytes'),
	('6541002','Dell', 'Optiflex 9021', 'Intel i7-4771', '3.00', '8.0 Gigabytes', '1.0 Tbytes'),
	('6541003','Dell', 'Optiflex 9022', 'Intel i7-4772', '3.00', '8.0 Gigabytes', '1.0 Tbytes'),
	('6541004','Dell', 'Optiflex 9023', 'Intel i7-4773', '3.00', '8.0 Gigabytes', '1.0 Tbytes'),
	('6541005','Dell', 'Optiflex 9024', 'Intel i7-4774', '3.00', '8.0 Gigabytes', '1.0 Tbytes'),
	('6541006','Dell', 'Optiflex 9025', 'Intel i7-4775', '3.00', '8.0 Gigabytes', '1.0 Tbytes');

SELECT*FROM ABC_Computer.Computer where Make = 'HP';
SELECT*FROM ABC_Computer.Computer where Make = 'Dell';

ALTER TABLE ABC_Computer.Computer ADD COLUMN Graphics VARCHAR(40) Not null;

UPDATE ABC_Computer.Computer SET Graphics = 'Integrated Intel HD Graphics 4600' WHERE Make = 'HP' or Make = 'Dell';

SET sql_safe_updates = 0;

ALTER TABLE ABC_Computer.Computer DROP COLUMN ProcessorSpeed;