#!/usr/bin/python3

import pymysql
import matplotlib.pyplot as plt
import sys, getopt

sys.path.insert(0, '../server/')

from credentials import User, Password, Database, DatabaseServer


def main(argv):
    outputFile = ''
    try:
        opts, args = getopt.getopt(argv,"o:h",["o="])
    except getopt.GetoptError:
        print("arg failure")
    for opt, arg in opts:
        if opt == '-h':
            print("temperature-plot.py -o <outputfile>")
            print("temperature-plot.py (for default path)")
            sys.exit()
        if opt == '-o':
            outputFile = arg
    print(f"outputfile is {outputFile}")

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

    #plt.show()
    if not outputFile:
        outputFile = "temperature.png"
    plt.savefig(outputFile)

if __name__ == "__main__":
   main(sys.argv[1:])