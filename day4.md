# SQL Lesson 8: A short note on NULLs

### syntax:

```
 SELECT column, another_column, …
FROM mytable
WHERE column IS/IS NOT NULL
AND/OR another_condition
AND/OR …;
```

1. Find the name and role of all employees who have not been assigned to a building ✓

> SELECT name, role 
 FROM employees
 where building is null;

2. Find the names of the buildings that hold no employees

> SELECT building_name
FROM buildings
left join employees on building_name = building
where building is null
;

# SQL Lesson 9: Queries with expressions



1. List all movies and their combined sales in millions of dollars ✓

## my wrong ans
```
SELECT title , domestic_sales as ds FROM movies 
inner join boxoffice 
on movies.id = boxoffice.movie_id
where ds = (Domestic_sales + international_sales) / 1000000
;
```

- as : renames the column


## exact soln

```
SELECT title , (domestic_sales + international_sales) / 1000000 as ds FROM movies 
inner join boxoffice 
on movies.id = boxoffice.movie_id

;
```

2. List all movies and their ratings in percent

```
SELECT title , rating * 10
FROM movies
left join boxoffice on id = movie_id;
```

3. List all movies that were released on even number years

>SELECT title FROM movies
where year % 2 ==0;

# SQL Lesson 10: Queries with aggregates (Pt. 1)


>SELECT AGG_FUNC(column_or_expression) AS aggregate_description, …
FROM mytable
WHERE constraint_expression;


- COUNT(*), COUNT(column) -	A common function used to counts the number of rows in the group if no column name is specified. Otherwise, count the number of rows in the group with non-NULL values in the specified column.

- MIN(column)	
- MAX(column)	
- AVG(column)	
- SUM(column)	

- Grouped aggregate functions(summarizing the data)


syntax : SELECT AGG_FUNC(column_or_expression) AS aggregate_description, …
FROM mytable
WHERE constraint_expression
GROUP BY column;
The GROUP BY clause work



## exercise

1. Find the longest time that an employee has been at the studio ✓

> SELECT max(years_employed) FROM employees;

2. For each role, find the average number of years employed by employees in that role

>SELECT role, avg(years_employed) FROM employees
group by role;

3. Find the total number of employee years worked in each building

>SELECT building, sum(years_employed) FROM employees
group by building;

# SQL Lesson 11: Queries with aggregates (Pt. 2)

### having constraint

>SELECT group_by_column, AGG_FUNC(column_expression) AS aggregate_result_alias, …
FROM mytable
WHERE condition
GROUP BY column
HAVING group_condition;

- If you aren't using the `GROUP BY` clause, a simple `WHERE` clause will suffice.
- The HAVING clause constraints are written the same way as the WHERE clause constraints, and are applied to the grouped rows


1. Find the number of Artists in the studio (without a HAVING clause) ✓


> SELECT count(role)
FROM employees
where role = "Artist";

2. Find the number of Employees of each role in the studio

> SELECT role, count(role) FROM employees
group by role;

3. Find the total number of years employed by all Engineers

>SELECT sum(years_employed) FROM employees
where role = "Engineer";

# SQL Lesson 12: Order of execution of a Query

>SELECT DISTINCT column, AGG_FUNC(column_or_expression), …
FROM mytable
    JOIN another_table
      ON mytable.column = another_table.column
    WHERE constraint_expression
    GROUP BY column
    HAVING constraint_expression
    ORDER BY column ASC/DESC
    LIMIT count OFFSET COUNT;

1. Find the number of movies each director has directed ✓

    >SELECT count(Title), Director FROM movies
group by Director;

2. Find the total domestic and international sales that can be attributed to each director

>SELECT director, sum(domestic_sales) + sum(international_sales) FROM movies
left join boxoffice on
id = movie_id
group by director;


#  SQL Lesson 13: Inserting rows

 ### syntax

 - insert statements with values for all columns

  > INSERT INTO mytable
VALUES (value_or_expr, another_value_or_expr, …),
       (value_or_expr_2, another_value_or_expr_2, …),
       …;

  - Insert statement with specific columns
  
> INSERT INTO mytable
(column, another_column, …)
VALUES (value_or_expr, another_value_or_expr, …),
      (value_or_expr_2, another_value_or_expr_2, …),
      …;

  ### example

  insert into movies values
  (1, "toy story" , 34, 1.9);


  # SQL Lesson 14: Updating rows

  - Update statement with values

>UPDATE mytable
SET column = value_or_expr, 
    other_column = another_value_or_expr, 
    …
WHERE condition;


1. The director for A Bug's Life is incorrect, it was actually directed by John Lasseter

>update Movies
set director = "John Lasseter"
where title = "A Bug's Life";

2. The year that Toy Story 2 was released is incorrect, it was actually released in 1999

>update movies
set year = 1999
where title = "Toy Story 2";

3. Both the title and director for Toy Story 8 is incorrect! The title should be "Toy Story 3" and it was directed by Lee Unkrich


- dont use set for the second updation
>update movies
set title = "Toy Story 3" ,
director = "Lee Unkrich"
where id = 11;    


# SQL Lesson 15: Deleting rows

>DELETE FROM mytable
WHERE condition;

- If you decide to leave out the WHERE constraint, then all rows are removed


1.This database is getting too big, lets remove all movies that were released before 2005. ✓


delete FROM movies
where year < 2005;

2. Andrew Stanton has also left the studio, so please remove all movies directed by him.

delete from movies
where director = "Andrew Stanton"

# SQL Lesson 16: Creating tables

### syntax

>CREATE TABLE IF NOT EXISTS mytable (
    column DataType TableConstraint DEFAULT default_value,
    another_column DataType TableConstraint DEFAULT default_value,
    …
);


1. Create a new table named Database with the following columns:
- Name A string (text) describing the name of the database
- Version A number (floating point) of the latest version of this database
- Download_count An integer count of the number of times this database was downloaded
This table has no constraints. ✓

>create table Database (
Name text,
Version float,
Download_count int
);

# SQL Lesson 17: Altering tables


- Altering table to add new column(s)

>ALTER TABLE mytable
ADD column DataType OptionalTableConstraint 
    DEFAULT default_value;

- Altering table to remove column(s)

>ALTER TABLE mytable
DROP column_to_be_deleted;

- Altering table name

>ALTER TABLE mytable
RENAME TO new_table_name;

1. Add a column named Aspect_ratio with a FLOAT data type to store the aspect-ratio each movie was released in.

>alter table movies
add Aspect_ratio float;

2.Add another column named Language with a TEXT data type to store the language that the movie was released in. Ensure that the default for this language is English.

>alter table movies
add Language text
default English;

# SQL Lesson 18: Dropping tables

- In some rare cases, you may want to remove an entire table including all of its data and metadata, and to do so, you can use the DROP TABLE statement, which differs from the DELETE statement in that it also removes the table schema from the database entirely.

- Drop table statement

>DROP TABLE IF EXISTS mytable;

## example:

>drop table boxoffice;