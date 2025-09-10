#ex1
select c.first_name , c.last_name ,c.email  from customer c 
select * from film 

select f.title, f.description , f.release_year  from film f
where f.rating ='R';

select title ,rental_duration , f.special_features as name  from  film f
where f.rental_duration between 6 and 7