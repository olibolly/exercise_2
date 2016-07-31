# exercise_2
# olivier zimmer July 2016

# Pre-requisite:
#Storm running on amazon EC2
#Postgres running on the same instance

#Packages required:
#psycopg2, tweepy, streamparse, python 2.7, virtualenv


# How to run the application
#1. Need to create a database and a table in postgres

#From root linux shell 
 
psql --username=postgres
CREATE USER w205 WITH PASSWORD 'postgres';
DROP DATABASE Tcount;
CREATE DATABASE Tcount;
ALTER DATABASE Tcount OWNER TO w205;
GRANT ALL ON DATABASE Tcount TO w205;
\q

psql --host=localhost --username=w205 --password --dbname=tcount
# Password for user w205: postgres

#Create a table
CREATE TABLE tweetwordcount (id BIGSERIAL PRIMARY KEY, word TEXT PRIMARY KEY NOT NULL, count INT NOT NULL);
\q

#2. Run Tweet count]
#You will need to update your Twitter API credentials in src/spout/tweets.py
cd tweetcount
sparse run
#Control+C to interrupt the streaming

#3. Serving scripts
python finalresults.py hello
python finalresults.py hello
python histogram.py 5 10
