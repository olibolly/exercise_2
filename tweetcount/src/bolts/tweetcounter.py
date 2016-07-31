from __future__ import absolute_import, print_function, unicode_literals
from collections import Counter
from streamparse.bolt import Bolt
import psycopg2
      
class TweetCounter(Bolt):
  def initialize(self, conf, ctx):
    self.counts = Counter()
    #self.redis = StrictRedis()

  def process(self, tup):
    word = tup.values[0]

    conn = psycopg2.connect(database="tcount", user="w205", password="postgres", host="localhost", port="5432")
    # try:
    #   cur = conn.cursor()
    #   cur.execute("CREATE DATABASE Tcount")
    #   cur.close()
    #   conn.close()
    # except:
    #   print "could not create Tcount"

    cur = conn.cursor()
    cur.execute("DROP TABLE tweetwordcount;")
    cur.execute('''CREATE TABLE tweetwordcount
            (word TEXT PRIMARY KEY NOT NULL,
             count INT NOT NULL);''')
    conn.commit()
    
    #conn.close()
    
    # Write codes to increment the word count in Postgres
    # Use psycopg to interact with Postgres
    # Database name: Tcount 
    # Table name: Tweetwordcount 
    # you need to create both the database and the table in advance.

    self.counts[word] += 1
    self.emit([word, self.counts[word]])
    # Log the count - just to see the topology running
    self.log('%s: %d' % (word, self.counts[word]))

    #cur = conn.cursor()

    #Insert
    cur.execute("INSERT INTO tweetwordcount (word,count) VALUES (%s, %s);", (word, self.counts[word]))
    conn.commit()

    #Update
    #Assuming you are passing the tuple (uWord, uCount) as an argument
    #cur.execute("UPDATE Tweetwordcount SET count=%s WHERE word=%s", (uWord, uCount))
    #cur.execute("UPDATE tweetwordcount SET count=%s WHERE word=%s", (self.counts[word], word))
    #conn.commit()

    #Select
    #cur.execute("SELECT word, count from Tweetwordcount")
    #records = cur.fetchall()
    #for rec in records:
    #  print 'word = ', rec[0]
    #  print 'count = ', rec[1], '\n'
    #conn.commit()

    conn.close()

    
