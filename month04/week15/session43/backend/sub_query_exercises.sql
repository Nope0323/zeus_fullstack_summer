--Дасгал 1: (WHERE ба IN) 'Penelope Guiness' гэдэг жүжигчний тоглосон бүх киноны нэрийг ол.
select 
payment_id,
amount
FROM
payment
WHERE
amount > (SELECT AVG(amount) FROM payment);

SELECT
customer_id, total_spent
FROM(select customer_id,
SUM(amount) AS total_spent
FROM
payment
GROUP BY
customer_id) AS customer_totals
WHERE
total_spent > 100;

SELECT
f.title,
(SELECT COUNT(*)
FROM film_actor fa
WHERE fa.film_id = f.film_id) AS number_of_actors
FROM
film f;

select title
from film f where film_id in(
	select film_id from film_actor fa
	where actor_id = (
		select actor_id 
		from actor
		where 
		first_name = 'Penelope'
		and
		last_name = 'Guiness'
	)
);

select  title from film where rental_rate > (select avg(rental_rate)from film);

select title from film 
where exists select from inventory i join rental r on r.inventory_id = i.inventory_id
where i.film_id = f.film_id
)
order by 

select * from customer c 

select first_name, last_name from customer c 
where address_id not in(
	select address_id from address a 
	where city_id in(
		select city_id from city where country_id=(
			select country_id 
			from country c 
			where country ='Canada' 
		)
	)
);
--ex05
 select c.first_name, c.last_name,   
 (select count(*) from rental r where r.customer_id = c.customer_id) as rental_count from customer c 
 
 --ex06
 select first_name, last_name
 from actor a where actor_id  in (
 select actor_id
 from film_actor fa 
 group by actor_id
 having count(film_id)>30)
 
 --ex07
 select customer_id, amount,payment_date from payment p1
 where p1.payment_date= (
 	select max(p2.payment_date)
 	from payment p2
 	where p2.customer_id = p1.customer_id
 	);
 --ex08
select title, length from film f
where f.length >ALL(
	select f.length  from film f
	join film_category fc  on fc.film_id = f.film_id 
	join category c on c.category_id = fc.category_id
	where c.name = 'Action'
) 
order by length asc;

  --ex09
select title, length from film f
where f.length >ALL(
	select f.length  from film f
	join film_category fc  on fc.film_id = f.film_id 
	join category c on c.category_id = fc.category_id
	where c.name = 'Action'
);
--ex10

select 
	f.title,
	rental_counts.count
from
	(select 
			i.film_id,
			Count(r.rental_id) as count
	from rental r 
	join inventory i on r.inventory_id= i.inventory_id
	group by 
	i.film_id
	order by 
	count desc
	limit 10
	) as rental_counts
join film f 
on f.film_id = rental_counts.film_id;

--ex11
select 
	distinct
	customer_id 
from payment p 
where 
	amount < (
		select 
			avg(amount)
		from payment p 
	)
--ex10
	
select  
	count(*)
from film
where film_id  not in (
	select 
	fc.film_id 
	from film_category fc 
	join category c 
	on fc.category_id = c.category_id 
	where c."name" = 'family'
);

--ex13

select 
	distinct 
	c.email 
from customer c 
join rental r on c.customer_id = r.customer_id 
join inventory i on r.inventory_id = i.inventory_id 
where i.film_id  in (
	select film_id
	from film f where length >(select avg(length) from film)
);



