--ex01 
select count(f.film_id) from film f
--ex02
select sum(amount) from payment p 
---ex03
select avg(f.rental_rate) from film f 
--ex04
SELECT 
    MIN(f.length) AS short_film,
    MAX(f.length) AS longest_film
FROM film f;
--ex05
