

## all and any
- All & Any
- Want all the orders which are greater than the Poojitha's orders
 
>SELECT * 
FROM orders 
where purch_amt > All(
			SELECT purch_amt
			FROM orders
			where customer_id = 3005)
 