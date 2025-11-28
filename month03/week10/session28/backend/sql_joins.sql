select * from country c;

select * from city;


select * from city where country_id =86;
-- south korea улсынх  нь 

select * from city ci  join country co on ci.country_id = co.country_id;

select city_id, city, co.country_id 
from city ci  
join country co
on ci.country_id  = co.country_id;

--left join 

select  a.first_name, a.last_name, COUNT (fa.film_id) as number_of_films
from actor a
left join film_actor fa on a.actor_id = fa.actor_id 
group by a.actor_id 
order by number_of_films asc;


select  c.first_name  , c.last_name, p.payment_id 
from customer c
left join payment p on c.customer_id = p.customer_id 
order by p.payment_id  DESC;

--null
select  c.first_name  , c.last_name, p.payment_id 
from customer c
left join payment p on c.customer_id = p.customer_id 
where p.payment_id is null 
order by p.payment_id  DESC;

--RIGHT
select c.first_name ,c.last_name ,r.rental_date 
from rental r 
right join customer c  on r.customer_id = c.customer_id  
order by r.rental_id  desc;

--ex

select  f.title ,i.inventory_id ,i.store_id  
from film f 
right join inventory i  on i.film_id  = f.film_id   
order by i.inventory_id  desc ;

--ex

select fa. film_id, a.first_name ,a.last_name  
from film_actor fa 
right join actor a ON a.actor_id = fa.actor_id 
order by fa.film_id 

--inner join
--
select c.lastname,c.firstname, a.district 
from  customer c 
inner join address a     ON c.adress_id = a.adress_id 


select f.title,c.name as category_name
from  film f
inner join film_category fc   ON f.film_id = fc.film_id
inner join category c on fc.category_id = c.category_id ;

select r.rental_id, s.first_name, s.last_name
from  rental r 
inner join staff s   ON r.staff_id = s.staff_id 




