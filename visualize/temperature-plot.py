#!/usr/bin/python3

import pymysql
import matplotlib.pyplot as plt
from credentials import User, Password, Database, DatabaseServer

# To connect MySQL database
conn = pymysql.connect(host=DatabaseServer, user=User, passwd=Password, db=Database)
    
curr = conn.cursor()

# Select query
curr.execute("select * from tempData")
output = curr.fetchall()

x = []
y = []
# print(output)
for i in output:
    x.append(i[1])
    y.append(i[3])
    # print(i[0],i[3])


  
# To close the connection
conn.close()

plt.plot(x,y,label="Upper Garage Field")

plt.title("Wisconsin Temperatures")
plt.ylabel('Temperature (F)')
plt.xlabel('Date')
plt.grid(True,color='#f1f1f1')

plt.legend()

plt.show()