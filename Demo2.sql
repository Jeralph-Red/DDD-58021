CREATE DATABASE Demo2;
CREATE TABLE Demo2.Customer (CustommerID INT Primary Key Not Null, CustomerName TEXT(50) Not Null, Municipality TEXT(50) Not Null, City TEXT(50));
SELECT*FROM demo2.Customer;
INSERT INTO demo2.Customer (CustommerID, CustomerName, Municipality, City)
VALUES	('1','Gina de Leon', 'Apalit', 'Pampanga'),
		('2','Amara Luna', 'Mexico', 'Pampanga'),
        ('3','Lucila Maulon', 'Anga', 'Bulacan'),
        ('4','Rafael Santos', 'Lumban', 'Laguna'),
        ('5','Maricel Moran', 'Calumpit', 'Bulacan'),
        ('6','Antonio Moreno', 'Santa Maria', 'Bulacan'),
        ('7','Hanna Moos', 'Alaminos', 'Laguna'),
        ('8','Fred Gregorio', 'Lumban', 'Laguna'),
        ('9','Maria Andres', 'Porac', 'Pampanga'),
        ('10','Liza Ramos', 'Alaminos', 'Laguna');

SELECT*FROM demo2.Customer WHERE City = 'Bulacan';
SELECT*FROM demo2.Customer WHERE Municipality = 'Alaminos';
SELECT*FROM demo2.Customer WHERE Municipality = 'Alaminos' AND City = 'Laguna';
SELECT*FROM demo2.Customer WHERE City NOT LIKE 'Pampanga';

