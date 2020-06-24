Structured query language

Data manipulation language
Has select clauses, updating and deleting data
Select
Update
Delete
Insert 
Data definition language
Play with the data structure and the table
Create
Alter
Drop 
Truncate  - does not drop the table but data within the table, not widely used
Data control language
These are privileged rights of the user which are granted by the database administrator 
Grant - give privileges 
Revoke - take away privileges
Transactional control language
we won't be dealing with these
Commit - when data is updated, deleted etc, you have to commit changes so people can see
Rollback - comparable to undo as it takes back the changes made 
Savepoint - 

CREATE DATABASE #here you're giving the software the instruction to create a new db
CREATE DATABASE agbo_db;

CREATE TABLE film_table
(
  film_name VARCHAR(10),
  film_type VARCHAR(6)
) 	#the parentheses open and close the list of columns that are to be created

Data Types

VARCHAR
is variable length character set
Is more memory efficient
If you put VARCHAR(MAX) you are allowing up to 8000 characters


CHAR 
is fixed length character set
Is 50% faster than VARCHAR 
Can be used in things like license plates or phone numbers as they are fixed
There is an alter clause that can be used when there is an exception in the number of characters eg personalised license plate

INT
Holds a whole number of number/ integer value(see also bigint, smallint and tiny int) positive 
or negative
Int take 4 byte by default
Big int takes  8/16 byte
Tiny int 2 byte

DATE or TIME or DATETIME
Stores date time or both date and time

DECIMAL or NUMERIC
Fixed Precision and scale (digits to right of decimal point) numbers.

BINARY
Used to store binary data such as an image or file.

FLOAT
Scientific use (very large numbers)

BIT
Equivalent to binary (0,1 or NULL)

INSERT INTO your_table

How to make a composite key
Make a primary key eg director_id
Then you join it with another column by using the below code
PRIMARY KEY( director_id, directorNumber)

This is how to make a foreign key
FOREIGNKEY(film_id) REFERENCES film_table(film_id)

Data integrity 

Insert breakdows
Changing the order of columns
If you've already created a table, the order in which you add the data doesnt have to be the same as the original column order as long as the values match the order you are now inserting

Omitting column names
You don't have to put the column names in, but the values have to be in the same order as the original columns

Leaving some columns out
You can leave some info out, it doesn't have to be inserted with the rest. For this you will have to specify the column names the values are going into

VARCHAR CHAR DATE all use quotes for their values

NULL
is not nothing but it does not equate to zero
It is not even an empty string
A value can be NULL, but NULL never equals null because null is an undefined value


DELETE
Deletes data from entire row depends on the parameters passed in the command
Pay attention of the WHERE clause because it can delete the entire table 

*/ DELETE FROM person WHERE person_id=1*/

Database consideration
Data security
So administrator won't give access to drop tables from other databases
Data recovery


Integrity 
When you insert something that does not exist in the parent table
Normal form

1 st NORMAL FORM
A database is in first normal form when the conditions are satisfied
Make sure you have no repeating values
Make everything Atomic
Data should be presented as small as it can be
They should have 1 and only one value
There should be no repeating groups
Eg a table that records data on a book and its author(s) with the following columns: [book ID], [author 2. [author3] is not in 1NF because [author 2], [author3] is not in 1nf because [author 1], [author 2], and [author 3] are all repeating the same attribute
2nd Normal Form
2NF is satisfied when:

All non-key attributes are fully functional dependent on the Primary Key
3rd Normal Form
