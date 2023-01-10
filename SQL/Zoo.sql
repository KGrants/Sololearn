insert into animals 
values('Slim', 'Giraffe', 1);

select a.name, a.type, b.country 
from animals a, countries b
where a.country_id = b.id
order by 3
