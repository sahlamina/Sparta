/*SQL day 5*/

SELECT o.OrderID, CONVERT(VARCHAR(10), o.OrderDate,103) AS
[dd,MM,yyy]
FROM Orders o; /* Before 2012*/

SELECT OrderID, FORMAT (OrderDAte, 'dd/MM/yyy')
FROM Orders; /* After 2010*/
-- Prior to SQL Server 2012 CONVERT was uses to format dates
-- in 2012 FORMAT() ws introduced to make it easier
--we are using 2017

SELECT 
c.CompanyName AS "Customer"
FROM Customers c
WHERE c.CustomerID NOT IN
    (SELECT CustomerID FROM Orders o)
-- this is an example of a subquery in the WHERE clause check to see which Customers have not placed any orders
-- this could also be achieved using JOINs


-- this didnt work for me
SELECT 
c.CompanyName AS "Customer"
FROM Customers c
FULL JOIN Orders o ON o.CustomerID=c.CustomerID
GROUP BY o.CustomerID, c.CompanyName
Where o.CustomerID IS NULL

SELECT c.CompanyName AS "Customer"
FROM Customers c
FULL JOIN Orders o ON c.CustomerID=o.CustomerID
WHERE o.CustomerID IS NULL

SELECT OrderID, ProductID, UnitPrice, Quantity, Discount,
    (SELECT MAX(od.UnitPrice) FROM [Order Details] od) AS "Max Price"
FROM [Order Details]


SELECT od.ProductID,sq1.totalamt AS "Total Sold for this Product",
od.UnitPrice, od.UnitPrice/totalamt*100 AS "% of Total"
    FROM [Order Details] od
    INNER JOIN
        (SELECT ProductID, SUM (o.UnitPrice*o.Quantity) AS "totalamt"
        FROM [Order Details]
        GROUP BY ProductID) sq1.ProductID=od.ProductID


-- 
    

SELECT 
od.OrderID, od.ProductID, od.UnitPrice, od.Quantity
FROM [Order Details] od
WHERE od.ProductID 
IN (SELECT p.ProductID p FROM Products p WHERE p.Discontinued =1)

SELECT 
od.OrderID, od.ProductID, od.UnitPrice, od.Quantity
FROM [Order Details] od
JOIN Products p
ON od.ProductID=od.ProductID
WHERE p.Discontinued =1

-- this is a contrived example, showinf how you could list all employee IDs in the same column as all suppleir ID
-- UNION ALL returns 38 rows and includes duplicate results
-- UNION removes any duplicates and returns 29 rows
-- both SELECT statements must have the same number of colimns in the SELECT clause (same type)
-- only the column alias in the first SELECT will be applied
-- ORDER BY  1 may be more appropriate if column names differ

SELECT e.EmployeeID AS "Employee/Supplier"
FROM Employees e
UNION ALL
SELECT s.SupplierID
From Suppliers s 

SELECT e.EmployeeID AS "Employee/Supplier"
FROM Employees e
UNION
SELECT s.SupplierID
From Suppliers s 