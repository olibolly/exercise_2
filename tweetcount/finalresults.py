from __future__ import absolute_import, print_function, unicode_literals
from collections import Counter
from streamparse.bolt import Bolt
import psycopg2



conn = psycopg2.connect(database="tcount", user="w205", password="postgres", host="localhost", port="5432")

cur = conn.cursor()

#Select
cur.execute("SELECT word, sum(count) as sum_count from tweetwordcount group by word order by word")
#cur.fetchall()

records = cur.fetchall()
for rec in records:
  print("word = ", rec[0])
  print("count = ", rec[1], "\n")
conn.commit()
conn.close()
