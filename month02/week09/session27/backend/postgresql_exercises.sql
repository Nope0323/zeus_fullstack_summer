select * from payment limint 10;

select * from payment 
where amount between 3.00 and 5.00
order by amount asc;

select title, length from film 
where length  between 90 and 120
order by length desc;

select rental_id,rental_date
from rental 
where rental_date 
between '2005-05-25 00:00:00' and '2005-05-26 23:59:59';

select title,replacement_cost from film
where replacement_cost  between 15.00 and 20.00 

select customer_id from customer 
where customer_id  between 100 and 200 ;


--like

select title from film limit 10 ;
 select title from  film where title = 'Italian';

select title from film where title like '%Italian%';

select last_name from customer where last_name like '%D%'; 

select title from film where title like '%action%';

select first_name from customer where first_name like 'er%;'

select title from film where title like '_e%';

select last_name from actor  where last_name  like'%GEN%';

--is null

select r.rental_id, c.customer_id, c.first_name , c.last_name 
from rental r
join customer c  
on r.customer_id  = c.customer_id  
where rental_date is null;

select a.address2
from address a  
where address2  is null ;

select rental_date 
from rental r
where rental_date  is not null limit 10;

select a.address2, a.address
from customer c 
join address a on c.address_id = a.address_id 
where a.address2 is not null;

select first_name, last_name
from staff s 
where picture is null ;