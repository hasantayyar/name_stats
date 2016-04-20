import psycopg2

conn = psycopg2.connect("dbname=onediombp user=onediombp")

cur = conn.cursor()
def iter():
  cur.execute("SELECT first,last FROM citizen limit 100;" )
  bulk = []
  if cur.rowcount < 100 :
    return False
  for r in cur:
    bulk.append(r)
  for b in bulk:
    cur.execute("SELECT count(*) FROM citizen WHERE first ='%s';"%(b[0]))
    count = cur.fetchone()[0]
    print b[0]
    cur.execute("INSERT INTO stats_citizen (name, count) VALUES('%s', %d);"%(b[0], count))
    cur.execute("DELETE FROM citizen WHERE first = '%s';"%(b[0]))
    conn.commit()
  iter()
iter()

conn.close()
