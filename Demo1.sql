DROP DATABASE fiirstschema;
CREATE DATABASE testdatabase;
DROP DATABASE testdatabase;
CREATE DATABASE my_own_database;
CREATE DATABASE testdatabase;
CREATE TABLE orderstable (OrderID INT NOT NULL, OrderNumber INT NOT NULL, PRIMARY KEY (OrderID));
INSERT INTO orderstable (OrderID, OrderNumber) Values ('1','77895'), ('2', '44678'), ('3', '22456')