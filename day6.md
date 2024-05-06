


# equi,inner,natural joins

## inner join
- can be written as


>select name,depname from empl
inner join dep
on salary> minsalary;

### creating from cmd line
- to create db:
create database fun

- to switch db
use fun;
dont know if that works

- renames db
Exec sp_renamedb 'old_db' , 'new_db'

u cant rename if u are in that particular db

## usage of documentation reference

1. updation
2. first handed
3. as it is written by the ones who wrote it
4. with examples


### fromating date

> select FORMAT( ord_date, 'D', 'en-gb' ) 'British English' from oil;

or 
> select FORMAT( ord_date, 'dd MMM yyyy' )  from oil;

# INTERSECT

>select department from employes
intersect 
select appliedfor from applicants;

## grouping 2 or 3 select queries into 1
 - final grouped set
>select region,category,quarter, sum(salesamount)
from Employeesales
group by grouping sets(
(region,category),
(region,quarter),region,quarter)
order by grouping(region), grouping(category), grouping(quarter)
;



- input stamt fro ass
>
DECLARE @name INT = 3;
SELECT *, FORMAT(ord_date, 'dd MMM yyyy')
FROM oil 
Order by purch_amt desc
    OFFSET 0 ROWS  
    FETCH NEXT @name ROWS ONLY;


>
select city,max(commission) 
from salesman i
where city = 'Paris'
group by city;

## 
- self joins

>select o.name,o.city,o.commission 
from salesman o
inner join (
select city,max(commission) as maxcommission
from salesman
where city is not null
group by city
) i
on o.commission = i.maxcommission;


## use of  EXISTS and NOT EXISTS

- gives true or false
- used in subqu

>
select name from employs o
where department= 'Engineering' and exists(
select employee_id from projects);