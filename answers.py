import psycopg2

DBNAME = "news"
query1 = ("select substr(path,10), count(method) from log where "
          "path like '%/article/%' group by path order by "
          "count(method) desc limit 3;")

query2 = ("select a.name,count(l.method) from authors a, articles d, "
          "log l where a.id=d.author group by a.name order "
          "by count(l.method) desc;")

query3 = ("select to_char(time,'DD/MM/YYYY'),((select count(*) "
          "from log where status like '%404%')*100/count(*))as "
          "percent from log group by to_char(time,'DD/MM/YYYY');")


def answer(query):
    conn = psycopg2.connect(database=DBNAME)
    c = conn.cursor()
    c.execute(query)
    rowcount = c.rowcount
    rows = c.fetchall()

    if rowcount > 10:
        for row in rows:
            print row[0] + " --" + str(row[1]) + " %"
    else:
        for row in rows:
            print row[0] + " --" + str(row[1]) + " views"

    conn.close()


answer(query1)
print
answer(query2)
print
answer(query3)