import os
import json
import mysql.connector

DBHOST = os.getenv('DBHOST')
DBUSER = os.getenv('DBUSER')
DBPASS = os.getenv('DBPASS')
DB = os.getenv('DB')

db = mysql.connector.connect(user=DBUSER, host=DBHOST, password=DBPASS, database=DB)
cur=db.cursor()

#def get_db_connection():
    #connection = mysql.connector.connect(
     #   host=DBHOST,
      #  user=DBUSER,
       # password=DBPASS,
        #database=DB
    #)
    #return connection
