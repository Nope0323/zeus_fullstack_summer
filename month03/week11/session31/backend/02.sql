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

--ex14
select c.name, avg(rental_duration) as avg_duration from film f 
join film_category fc   on f.film_id = fc.film_id 
join category c on fc.category_id = c.category_id 
group by c.name
having avg(rental_duration)>5


--ex15
select a.first_name , a.last_name, count(fa.film_id) as film_count from film_actor fa 
join actor a on fa.actor_id = a.actor_id 
group by a.actor_id
order by film_count desc
limit 10;

--ex16
select title, sum(p.amount) as total_revenue from payment p
join rental r on p.rental_id = r.rental_id
join inventory i on r.inventory_id  = i.inventory_id 
join film f on i.film_id  = f.film_id 
group by f.film_id, f.title  
order by total_revenue desc 
limit 5;

--ex 1
select f.title as film_title , c.name as category_name  
from actor a 
join film_actor fa on a.actor_id = fa.actor_id 
join film f on fa.film_id = f.film_id 
join film_category fc on f.film_id = fc.film_id 
join category c on fc.category_id = c.category_id
where a.first_name  = 'Penelope ' and a.last_name ='Guiness'
order by film_title, category_name;
