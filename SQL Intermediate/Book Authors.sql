select a.name, a.year, b.name as author from books a, authors b
where a.author_id = b.ID
order by b.name, a.year 