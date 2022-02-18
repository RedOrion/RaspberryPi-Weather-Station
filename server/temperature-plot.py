#!/usr/bin/python3

import pymysql
import matplotlib.pyplot as plt
from credentials import User, Password, Database, DatabaseServer

# To connect MySQL database
conn = pymysql.connect(host=DatabaseServer, user=User, passwd=Password, db=Database)
    
cur = conn.cursor()

# Select query
cur.execute("select * from tempData")
output = cur.fetchall()

for i in output:
    print(i)
    
# To close the connection
conn.close()

plt.plot(output[1],output[3])
plt.show()