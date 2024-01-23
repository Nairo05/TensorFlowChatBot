import sqlite3
import json
from datetime import datetime

timeframe = '2015-05'
sql_transaction = []
connection = sqlite3.connect('{}.db'.format(timeframe))
c = connection.cursor()

def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS parent_reply(parent_id TEXT PRIMARY KEY, comment_id TEXT UNIQUE, parent TEXT, comment TEXT, subreddit TEXT, unix INT, score INT)""")

def format_data(data):
    data = data.replace("\n"," newlinechar ")

if __name__ == '__main__':
    create_table()
    row_counter = 0
    paired_rows = 0

    # file location here f.e. "J:/chatdata/reddit_data/{}/RC_{}".format(timeframe.split('-')[0], timeframe)
    with open("../datasets/reddit_data/{}/RC_{}".format(timeframe.split('-')[0], timeframe), buffer=1000) as f:
        for row in f:
            row_counter += 1
            row = json.loads(row)
            parent_id = row['parent_id']
            body = format_data(row['body'])
            created_utc = row['created_utc']
            score = row['score']
            subreddit = row['subreddit']



