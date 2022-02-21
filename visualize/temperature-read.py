#!/usr/bin/python3

import pymysql
import sys

sys.path.insert(0, '../server/')

from credentials import User, Password, Database, DatabaseServer

# To connect MySQL database
conn = pymysql.connect(host=DatabaseServer, user=User, passwd=Password, db=Database)
    
curr = conn.cursor()

# Select query
curr.execute("select * from tempData")
output = curr.fetchall()

for i in output:
    print(i)
    
# To close the connection
conn.close()
