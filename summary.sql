select count(method), substr(path,10) as "Articles" from log where path like '%/article/%' group by path order by count(method) desc limit 3;

select a.name,count(l.method) as "Page Views" from authors a, articles d, log l where a.id=d.author group by a.name order by count(l.method) desc;



select count(status), to_char(time,'DD/MM/YYYY') from log where status like '%404%' and count(status) > =2222 group by to_char(time,'DD/MM/YYYY') order by count(status) desc;

select count (*), to_char(time,'DD/MM/YYYY') from log group by to_char(time,'DD/MM/YYYY') order by count(*) desc;

select count(status), to_char(time,'DD/MM/YYYY') from log where count(status)/(select count (*), to_char(time,'DD/MM/YYYY')>=0.01 from log group by to_char(time,'DD/MM/YYYY') order by count(*) desc)
and status like '%404%' group by to_char(time,'DD/MM/YYYY') order by count(status) desc;
