import psycopg2

DBNAME = "news"


def question1():
    conn = psycopg2.connect(database=DBNAME)
    c = conn.cursor()
    query = ("select count(method), substr(path,10) from log where "
             "path like '%/article/%' group by path order by "
             "count(method) desc limit 3;")
    c.execute(query)
    rows = c.fetchall()
    for row in rows:
	print row[1] + " --" + str(row[0]) + " views"
    conn.close()


def question2():
    conn = psycopg2.connect(database=DBNAME)
    c = conn.cursor()
    query = ("select a.name,count(l.method) from authors a, articles d, "
             "log l where a.id=d.author group by a.name order "
             "by count(l.method) desc;")
    c.execute(query)
    rows = c.fetchall()

    for row in rows:
	print row[0] + " -- " + str(row[1]) + " views"
    
	conn.close()


def question3():
    conn = psycopg2.connect(database=DBNAME)
    c = conn.cursor()
    query = ("select to_char(time,'DD/MM/YYYY'),((select count(*) "
             "from log where status like '%404%')*100/count(*))as "
             "percent from log group by to_char(time,'DD/MM/YYYY');")

    c.execute(query)
    rows = c.fetchall()

    for row in rows:
	print row[0] + " --" + str(row[1]) + " %"
    
	conn.close()


question1()
print ""
question2()
print ""
question3()

