


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