select a.name, count(b.name) as books from Books b right join Authors a
on a.id = b.author_id
group by a.name
order by 2 desc