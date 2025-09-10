--ex1
select f.title, f.release_year  from film f 
--ex2
select f.title, f.release_year  from film f 
where f.release_year =2006 limit 5;
--ex3
    SELECT f.title, f.length
    FROM film f
    WHERE f.length < 186
    ORDER BY f.length DESC limit 5;
--ex4 
   select c.first_name ,c.last_name from customer c 
   order by last_name asc limit 5;
--ex5 
  
select c.first_name, c.last_name, cr.country  from customer c 
join address a on c.address_id  = a.address_id  
join city ct  on a.city_id = ct.city_id
join country cr on ct.country_id = cr.country_id
where cr.country = 'Canada' limit 5;
