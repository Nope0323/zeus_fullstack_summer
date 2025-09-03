--ex1
select count (film_id) from film f ;
select sum(p.amount) from payment p  ;
select avg(f.rental_rate) from film f  ;
select 
	min(length) as shortest_film_duration,
	max(length) as longest_film_duration
from film f ;

select 
	rating,
	count(*) as number_of_films
from
	film f 
group by 
	rating ;

select  customer_id ,
	SUM(amount) as total_spent
from
payment p 
group by
	customer_id 
having 
	sum(amount)>150
order by 
	total_spent desc;
	
select count (a.actor_id) from actor a ;

SELECT SUM(f.replacement_cost) from film f ;

select MAX(payment_date)  from payment p  ;

--ex10
select c.name,  count(fc.category_id) as number_of_films from category c 
join film_category fc on c.category_id = fc.category_id  
group by c.name
order by number_of_films DESC;


select category_id  from film_category fc 
 
select *  from payment p 


--ex11
select  f.rating, avg(length)from film f 
group by f.rating 
--ex12
select p.staff_id,  sum(amount)from payment p 
group by staff_id

--ex13
select p.staff_id count(p.payment_id )from payment p
having payment_id <8000
group by p.staff_id; 