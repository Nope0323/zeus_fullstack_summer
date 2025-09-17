--ex01 09-12
select * from actor a 

INSERT INTO actor (first_name, last_name)
VALUES ('CHINGGIS', 'KHAN');

--ex02

insert into category (name)
values ('iopic')

select category_id ,name from category

update category 
set name='Biopic'
where category_id=17;

--ex03
update actor 
set first_name = 'CHINGGIS' , last_name = 'KHAN'
where actor_id = 202;

--ex04

select* from film f
where rating ='G'

update film  
set rental_duration= rental_duration+1 
where rating= 'G'

--ex05
delete from actor

where actor_id= 202

select actor_id , first_name , last_name  from actor a 

--ex06
select * from customer c 

select c.customer_id, c.first_name, c.last_name
FROM customer c
WHERE LOWER(c.first_name) = 'mary';

DELETE FROM customer
WHERE customer_id = 1;

select *from payment p

select p.customer_id, p.payment_id
FROM  payment p
WHERE customer_id=1;

delete from payment  
where customer_id=1;

select customer_id from rental
where customer_id=1;

delete from rental  
where customer_id=1;

--ex07
select *from "language" l 


INSERT INTO "language"  (name)
VALUES ('Mongolia');

--ex08

select c.country from country c 

INSERT INTO country  (country)
VALUES ('Mongolia');

select *  from city c 

INSERT INTO country (country)
VALUES ('Mongolia')
RETURNING country_id;

INSERT INTO city (city, country_id)
VALUES 
 ('Ulaanbaatar',
  (SELECT country_id 
   FROM country 
   WHERE country = 'Mongolia'
   LIMIT 1));

--ex09
  
  select * from film f
  select * from film_category fc
  select * from category c
  

  
 select f.rental_rate  from film f 
  join film_category fc on f.film_id = fc.film_id 
  join category c  on fc.category_id =c.category_id;
 
 select fc.film_id, c.name from film_category fc
 join category c  on fc.category_id =c.category_id
where c.name = 'Horror';
 
 update film 
 set rental_rate = rental_rate + 0.5
where film_id in (
select fc.film_id from film_category fc
 join category c  on fc.category_id =c.category_id
 where c.name = 'Horror'
);

  --ex10
 select release_year ,rating  from film
 where  rating='NC-17'

delete from film 
where release_year<2006 and rating='NC-17'

select * from inventory i 