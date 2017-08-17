import time
import json
import pymysql
import re
import os
import tweepy
from db_connect import *

API_KEY=os.environ['API_KEY']
API_SECRET=os.environ['API_SECRET']
TOKEN_KEY=os.environ['TOKEN_KEY']
TOKEN_SECRET=os.environ['TOKEN_SECRET']
def get_api_instance():
  auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
  auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)
  api_inst = tweepy.API(auth)
  return api_inst

def do_data_pull(api_inst):

  sql_query = "select product_id, product_name from Calculators_Keyboards"
  try:
    conn = create_connection()
    db_cursor = conn.cursor()
    query_status = run_stmt(db_cursor, sql_query)
    resultset = db_cursor.fetchall()
    print("result set ", resultset)
    for record in resultset:
      product_id = record[0]
      product_name = record[1]
      # print("DEBUG: here is the mention: ", product_name)


      twitter_query = product_name
      print "twitter_query: " + twitter_query
      twitter_cursor = tweepy.Cursor(api_inst.search, q=twitter_query, lang="en")

      for page in twitter_cursor.pages():
        for item in page:
          json_str = json.dumps(item._json)
          print "found a " + product_name + " tweet"

          insert_stmt = "insert into Tweet(tweet_doc, product_id) values(%s, %s)"
          run_prepared_stmt(db_cursor, insert_stmt, (json_str, product_id))
          do_commit(conn)

  except pymysql.Error as e:
    print "pymysql error: " + e.strerror

  except tweepy.TweepError as twe:
    print "got a TweepError: " + twe.message
    if twe.message.endswith("429"):
      print "got rate limit error, sleeping for 15 minutes"
      time.sleep(60*15)
      print "finished sleeping. re-trying do_data_pull"
      do_data_pull(api_inst)

api_inst = get_api_instance()
do_data_pull(api_inst)
