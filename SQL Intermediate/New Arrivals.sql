select name, year from books where year > 1900
union
select name, '2022' as year from new
order by 1 asc