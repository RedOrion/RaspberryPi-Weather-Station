#!/usr/bin/python3

import pymysql
from credentials import User, Password, Database, DatabaseServer

# To connect MySQL database
conn = pymysql.connect(host=DatabaseServer, user=User, passwd=Password, db=Database)
    
cur = conn.cursor()

# Select query
cur.execute("select * from sensors")
output = cur.fetchall()

for i in output:
    print(i)
    
# To close the connection
conn.close()
