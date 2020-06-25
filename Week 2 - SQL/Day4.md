#We learned a bunch of functions and for SQL toda
#Joins, Dates, Having

-- DATE Functions
-- GETDATE select GETDATE() to return the current date and time
-- SYSDATETIME select sysdatetime() to retutn the date and time of the computer being used
-- DATEADD DATEADD(d,5,OrderDate) AS "DueDate" to add 5 days
-- DATEDIFF DATEDIFF(d,OrderDate,ShippedDate) AS "Ship Time" to calculate difference between dates
-- YEar SELECT YEAR(OrderDATE) AS "Order Year" to extract the year from a date.
-- MONTH: SELECT MONTH(OrderDate) AS "Order Month" to extract the year from a date
-- DAY: SELECT DAY (OrderDate) AS "Order Day" to extract the day from a date



SELECT DATEADD(d,5, Orderdate) AS "Due Date",
    DATEDIFF(d,OrderDate,ShippedDate) AS "Ship Days"
FROM Orders
/* DATEADD has 3 arguments
1. d or dd means day m or mm month, yy or yyyy year
2. the date has to be added to 
3. how many units to had
DATEDIFF uses the same datepart argument abbreviations followed by the two dates for the calculation*/

-- this was an exercise in which we had to get the names to display as full names and use DATEDIFF to calculate their ages
SELECT
CONCAT(e.FirstName, ' ', e.LastName) AS 'Full Name',
DATEDIFF(YEAR, e.BirthDate, GetDate())  as Age
FROM Employees e

SELECT
CONCAT(e.FirstName, ' ', e.LastName) AS "Full Name",
DATEDIFF(YEAR, e.BirthDate, GETDATE()) AS "Age"
FROM Employees e 


SELECT
CONCAT(e.FirstName, ' ', e.LastName) AS "Full Name",
DATEDIFF(DAY, e.BirthDate, GETDATE()) / 365.25 AS "Exact Age"
FROM Employees e 

-- Case statments when you want to vary the result based on a type of output
-- CASE statements can be useful when you need varying results output based on differing data
SELECT CASE 
WHEN DATEDIFF(d, o.OrderDate,o.ShippedDate) <10 THEN 'On Time'
ELSE 'Overdue'
END AS "Status"
FROM orders o

/*Use CASE to add a column to the previous activity solution called retirement status as follows
agw > 65 retired
age > 60 retirement DEFAULTage < 60 5 more than 5 yers to go*/

SELECT 
CONCAT(e.FirstName, ' ', e.LastName) AS "Full Name",
DATEDIFF(YEAR, e.BirthDate, GETDATE()) AS "Age",
CASE 
WHEN DATEDIFF(YEAR, e.BirthDate, GETDATE()) >65 THEN 'Retired'
WHEN DATEDIFF(YEAR, e.BirthDate, GETDATE()) >=60 THEN  'Retirement due'
WHEN DATEDIFF(YEAR, e.BirthDate, GETDATE()) <60 THEN 'More than 5 years to go'
END AS "Status"
FROM Employees e 

-- Aggregate Functions
/* Sum SUM

*/

SELECT 
SUM(p.UnitsOnOrder) AS "Total On Order",
AVG(p.UnitsOnOrder) AS "Avg on Order",
MIN(p.UnitsOnOrder) AS "Min on order",
MAX(p.UnitsOnOrder) AS "Max on order"
From Products p 

SELECT * FROM Products

/* Calculate units on orders using aggregate functions per supplier*/

SELECT 
SupplierID,
SUM(p.UnitsOnOrder) AS "Total On Order",
AVG(p.UnitsOnOrder) AS "Avg on Order",
MIN(p.UnitsOnOrder) AS "Min on order",
MAX(p.UnitsOnOrder) AS "Max on order"
From Products p
GROUP BY SupplierID

-- use group by to calculate the average recorder level for all prods by category id, select caluse must match the group by clause apart from any aggregates

SELECT p.CategoryID,
AVG(p.reorderlevel) AS "AVG reorder level"
From Products p 
GROUP BY p.CategoryID 
ORDER BY "AVG reorder level" DESC;


-- HAVING is used instead of WHERE when filtering on subtotals/ grouped data
--column aliases cannot be used in the HAVINF caluse
-- aggregate funcions are not available for use in the where sequence due to the SQL processing sequence

SELECT p.SupplierID,
SUM(UnitsOnOrder) AS "Total on Order",
AVG(p.UnitsOnOrder) AS "Avg on Order"
From Products p 
GROUP BY p.SupplierID
HAVING AVG(p.UnitsOnOrder)>5 

/*Syntax sequence
SELECT
DISTINCT
FROM
WHERE
GROUP BY
HAVING
ORDER BY
*/

-- Edgar F Codd the guy who coined the term relational 
-- database and innovated the way we use databases

/* Presentation notes
Aggregate Functions
An aggregate function performs a calculation on a set of values, and returns a single value.
Except for COUNT, aggregate functions ignore null values.
Aggregate functions are often used with the GROUP BY clause of the SELECT statement
AVG – calculates the average of a set of values.
COUNT – counts rows in a specified table or view.
MIN – gets the minimum value in a set of values.
MAX – gets the maximum value in a set of values.
SUM – calculates the sum of values.
*/

/*PRESEntation notes
GROUPBY: used to categorise the same values in a column
, ususally used with aggregate functions
, usually used with order by

when trying to use more than one argument in a group by, make sure youre using 

JOINSSS
join is of using values on tables with common***

inner join - command which returns rows that match in both ie only the intersection between the two tables***
matched walues are based on primary and foreign key commonality

LEft join/ left outer join
- appending two tables together
- returns all the tables of table 1(left) and returns elements of table 2 that satisfy/ match the condition

RIGHT join/ right outer join - retutns records from right table and matched records
- returns all the tables of table 1(right) and returns elements of table 2 that satisfy the condition
- any 0 values will be returned as null

FULL OUTEr join - returns all records from both tables when there is a match in either table
, this is rarely used

HAVING - added to SQL becasue WHERE could not be used with aggregate functions
different to WHERE becasue HAVING is only used 
in SELECT queries which contain aggregate functions or GROUP by

SELF join - when you join a tbale wiht itself aKA unary relationships 
- with every

CROSS Join- used to generate a paried combination of each roem of the frist table aka cartesian join
if other joins are like addition, this is like multiplication



*/


-- CODE FROM JOINS PRESENTATION --

--FUll Join
SELECT c.customerID, c.contactName, o.employeeID, o.ShipCity
FROM orders o 
FULL JOIN customers c
ON c.customerID = o.CustomerID
ORDER BY EmployeeID;

--INNER JOIN 
SELECT c.customerID, c.contactName, o.employeeID, o.ShipCity
FROM orders o 
INNER JOIN customers c
ON c.customerID = o.CustomerID
ORDER BY EmployeeID;

--Left Join
SELECT c.customerID, c.contactName, o.employeeID, o.ShipCity
FROM orders o 
LEFT JOIN customers c
ON c.customerID = o.CustomerID
ORDER BY EmployeeID;

--Right Join
SELECT c.customerID, c.contactName, o.employeeID, o.ShipCity
FROM orders o 
RIGHT JOIN customers c
ON c.customerID = o.CustomerID
ORDER BY EmployeeID
 
--Self join
SELECT o.customerID, o.employeeID, b.ShipCity, b.CustomerID
FROM orders o, orders b
WHERE o.customerID = b.CustomerID;
 
--Cross join
SELECT*
FROM Orders o 
CROSSJOIN customers c;

SELECT
COUNT(o.CustomerID)
FROM orders o

SELECT
COUNT(o.CustomerID)
FROM Customers o


/*joins
and SQL key woed used to combine matched rows from wo or more tales
*/

-- using rows from products, group by supplier showing an average of units on otfer from each suppleir

SELECT s.CompanyName AS "Supplier Name", AVG(p.UnitsOnOrder) AS "Average UnitsOnOrder"
FROM products p
INNER JOIN Suppliers s
ON p.SupplierID=s.SupplierID
GROUP BY s.SupplierID, s.CompanyName
ORDER BY "Average UnitsOnOrder" DESC

SELECT
CONCAT (e.FirstName, ' ' e.LastName) AS "Employee name"
c.CompanyName AS "Company Name"
FROM orders o INNER JOIN Customers c
ON o.customerID = c.CustomerID
INNER JOIN Employees e
ON o.EmployeeID = e.EmployeeID


o.OrderID, o.OrderDate, o.Freight


SELECT c.customerID, c.contactName, o.employeeID, o.ShipCity
FROM orders o 
INNER JOIN customers c
ON c.customerID = o.CustomerID
ORDER BY EmployeeID;