from __future__ import absolute_import, print_function, unicode_literals
from collections import Counter
from streamparse.bolt import Bolt
import psycopg2
import sys



conn = psycopg2.connect(database="tcount", user="w205", password="postgres", host="localhost", port="5432")
cur = conn.cursor()

# If no arg then render all thw words in the stream
if len(sys.argv) == 1:
	cur.execute("SELECT word, sum(count) as sum_count from tweetwordcount group by word order by word")
	records = cur.fetchall()
	for rec in records:
	  print("word = ", rec[0])
	  print("count = ", rec[1], "\n")
	conn.commit()
	conn.close()

# If one arg then render that word with total number of counts
if len(sys.argv) == 2:
	input_word = str(sys.argv[1])
	print('Total number of occurences of', input_word)

	input_string = "SELECT word, sum(count) as sum_count from tweetwordcount where word = '%s' group by word" % str(sys.argv[1])
	cur.execute(input_string)
	#cur.execute("SELECT word, sum(count) as sum_count from tweetwordcount where word = %s group by word", (input_word))
	records = cur.fetchall()
	for rec in records:
	  print("word = ", rec[0])
	  print("count = ", rec[1], "\n")
	conn.commit()
	conn.close()	
