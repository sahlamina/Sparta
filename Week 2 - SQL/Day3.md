select * from Customers

-- where clause
-- this also shows how to add a title to your filter result with count () as and the string in the qute marks
select Count (*) AS "Number of Customers with in Paris" from customers
where city='Paris'

select * from Employees

select  Count (*) as "number of employees from london" from employees 
where city = 'London'
-- 4


select * from employees 
where TitleOfCourtesy = 'Dr.'
--1

select * from Products 
where Discontinued ='0';

-- where to use apostrophes:

-- table aliasing
SELECT c.CompanyName, c.City, c.Region
FROM Customers c
WHERE c.Region = 'BC'

-- SELECT TOP allows you to run test queries against very large tables without hitting performance issues
SELECT COUNT * FROM Customers

-- And/ OR
-- and: all the criteria has to be fulfilled
-- or: either of the criteria needs to be fulfilled

SELECT p.ProductName , p.UnitPrice 
FROM Products p
WHERE CategoryID = 1 AND p.Discontinued = 0

-- operators are the same as any other lang but <> also means !=
SELECT p.ProductName, p.UnitPrice
FROM Products p
WHERE UnitsInStock > 0 AND UnitPrice > 29.99
-- can also use or in this query

--DISTINCT helps to eradicate duplicate values, only returns distinct values

SELECT DISTINCT c.Country
FROM Customers c

-- wildcard characters can be used as a substitute for any other characters in a string when using the LIKE operator
-- %
SELECT c.Country
FROM Customers c WHERE Country LIKE 'G%'

-- countries ending with letter 'A'
SELECT DISTINCT c.Country
FROM Customers c WHERE Country LIKE '%A'

-- countries starting with u, and end with a
SELECT DISTINCT c.Country
FROM Customers c WHERE Country LIKE 'U%A'

--countries starting with u or a or m, this is called charlist
SELECT c.Country
FROM Customers c WHERE Country LIKE '[UAM]%'

-- countries either ending with U A or M in descending order
SELECT DISTINCT c.Country
FROM Customers c WHERE Country LIKE '%[UAM]'
ORDER BY c.Country DESC 
-- order by is ascending by default so adding the desc will tell it to return results in descending order

-- countries not starting with u or a or m
SELECT DISTINCT c.Country
FROM Customers c WHERE Country LIKE '[^UAM]%'

-- countries where tihrd letter is a, the _ is a substitute for a single char
SELECT DISTINCT c.Country
FROM Customers c WHERE Country LIKE '__a%'

-- products where the first two charactera are ch
SELECT p.ProductName
FROM Products p WHERE p.ProductName LIKE 'Ch%'

-- if we need to find regions ending in a made of 2 characters, neither of there worm MAKE SURE TO ASK HELP

Select *
FROM Customers c WHERE c.Region LIKE '_A%'

Select *
FROM Customers c WHERE c.Region LIKE '%A'

SELECT *
FROM Customers WHERE Region IN ('WA','SP')

-- IN Operator supports equation to multiple values
SELECT *
FROM Customers WHERE Region EXISTS ('WA','SP')

-- without in statement

SELECT *
FROM Customers WHERE Region = 'WA' OR Region = 'SP'

-- without in statement and country should be Brazil
-- brackets tell the language which queries to group together

SELECT *
FROM Customers WHERE (Region = 'WA' OR Region = 'SP') 
AND Country = 'Brazil'

SELECT * FROM Customers WHERE Region IN ('WA', 'SP')
AND Country In ('Brazil', 'USA')

-- BETWEEN includes values between and as welll as the boundary values
-- below code helps if we want to find territories in range of IDs

SELECT *
FROM EmployeeTerritories
WHERE TerritoryID BETWEEN 06800 AND 09999

--names and prod IDs of prods with UNIT pric3s < 5.00
SELECT p.ProductName, p.productID, p.UnitPrice
FROM Products p
WHERE unitprice  < 5.00 

-- which categories have a category name with initials beginning with b or s

SELECT c.CategoryName, c.[Description]
FROM Categories c
WHERE c.CategoryName LIKE 'B%' OR c.CategoryName LIKE 's%'

SELECT *
FROM Categories AS "c"
WHERE c.CategoryName LIKE '[BS]%';




-- how many orders are there for employeeIDs 5 and 7 (the total for both)
-- 114
SELECT Count (*) AS "Number of orders placed by between 5 and 7"
FROM Orders
where EmployeeID IN ('5', '7')


-- groups by number of orders per employee id
SELECT o.EmployeeID, Count (*) AS "Number of orders placed by between 5 and 7"
FROM Orders o
where o.EmployeeID IN (5,7)
GROUP BY o.EmployeeID

-- concatenation
-- concatenate usin g+ along woth single quptes
-- alias column using AS (optional) and souble quotes (if more than one word) to change column headers

SELECT c.CompanyName AS "Company Name",
CONCAT (c.City, ', ', c.Country) AS "City"
FROM Customers c

/*Write a SELECT statement using the employees table and concatenate
 first name and last name together. use a column alias to rename the clumn to employee name*/

 SELECT e.FirstName, e.LastName,
 CONCAT (e.FirstName,', ', e.LastName) AS "Employee Name"
 FROM Employees e
-- more advanced method
 SELECT 
 CONCAT (e.FirstName,', ', e.LastName) AS "Employee Name"
 FROM Employees e

 -- null and not null
 -- in order to filter based on NULLs simply used IS NULL or IS NOT NULL

 SELECT c.CompanyName AS 'Company Name', City + ',' + Country AS 'City'
 FROM Customers c
 WHERE Region IS NULL

 /*write a SELECT statement to list the six countries that have Region Codes in the Customers Table */
SELECT * FROM Customers;

 SELECT TOP 6 c.Country, c.Region
 FROM Customers c 
 WHERE c.Region IS NOT NULL

 -- modulus is the remainder of a division so 76%3=1 88/2= 44, 90%7=6

 -- Apples --> Price-->2pounds, quantity=10, Discount-25%
 -- Gross Total(The cost of apples excluding the discount)20
 --Net total(the amount I pay the shopkeeper at the end) 15
 SELECT UnitPrice, Quantity, Discount
 FROM [Order Details]

-- add a new column to the SQL below to SHOW the 'net total' which has the discount coumn applied to it
-- be sure to sanity check your answers
SELECT * FROM [Order Details]

SELECT UnitPrice, 
Quantity, 
Discount,
UnitPrice * Quantity AS "Gross Total",
ROUND((UnitPrice * Quantity * (1.00-Discount)),2) AS 'Net Total'
FROM [Order Details]; 
 
-- use order by to identify the highest net total in the order details table
-- what are the two order numbers with the highest total


SELECT TOP 2 UnitPrice, 
Quantity, 
Discount,
UnitPrice * Quantity AS "Gross Total",
ROUND((UnitPrice * Quantity * (1.00-Discount)),2) AS "Net Total"
FROM [Order Details] 
ORDER BY "Net Total" DESC;

-- indexing in SQL starts from 1
/* string functions
charstring - search for a string e.g. find 'a' in a column called 'text'
substring -  finds characters within a string, the format (film_name, 1, 3) will return first 3 letters from name of film
Left or right - (name,5) for the first (or last) 5 characters
LTRIM or RTRIM - used to remove spaces at the beginning or end of a string
LEN - LEN(name) for the length of the name
REPLACE - replaces spaces with so REPLACE(name,' ','_') replaces name with underscores
UPPER or LOWER - UPPER(name) to convert to all upper or (lower) case 
*/

-- This SQL uses nested functions: CHARINDEX inside LEFT
SELECT c.PostalCode "Post Code",
LEFT(c.PostalCode, CHARINDEX(' ',c.PostalCode)-1) AS "Post Code Region",
    CHARINDEX(' ', c.PostalCode) AS "Space Found", c.Country 
FROM Customers c
WHERE c.Country = 'UK'

-- use CHARINDEX to list only product names that contain a single quote
-- note: column alias cannot be used in a WHERE
-- For single quote use two single quotes to escape it


SELECT p.ProductName 
FROM  Products p
WHERE p.ProductName LIKE '%''%'

SELECT p.ProductName "Product Names",
CHARINDEX('''',p.ProductName) AS "Index of Quote"
FROM Products p 
WHERE CHARINDEX('''',p.ProductName) > 0