from __future__ import absolute_import, print_function, unicode_literals
from collections import Counter
from streamparse.bolt import Bolt
import psycopg2
import sys

conn = psycopg2.connect(database="tcount", user="w205", password="postgres", host="localhost", port="5432")
cur = conn.cursor()

k1 = str(sys.argv[1])
k2 = str(sys.argv[2])

input_string = "SELECT word, sum(count) as sum_count from tweetwordcount group by word having sum(count) > %s and sum(count) < %s;" % (str(sys.argv[1]), str(sys.argv[2]))
cur.execute(input_string)
records = cur.fetchall()
for rec in records:
	 print(rec[0], ": ", rec[1], "\n")
conn.commit()
conn.close()