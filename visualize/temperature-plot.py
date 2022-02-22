#!/usr/bin/python3

from datetime import date
import pymysql
import matplotlib.pyplot as plt
import sys, getopt
from collections import defaultdict

sys.path.insert(0, '../server/')

from credentials import User, Password, Database, DatabaseServer


def main(argv):
    outputFile = ''
    plotTitle = ''
    zone = False
    try:
        opts, args = getopt.getopt(argv,"o:ht:z:",["o=", "t=", "z="])
    except getopt.GetoptError:
        print("arg failure")
    for opt, arg in opts:
        if opt == '-h':
            print("temperature-plot.py (for default path)")
            print("-o   output file")
            print("-t   graph title")
            print("-z   zone")
            sys.exit()
        if opt == '-o':
            outputFile = arg
        if opt == '-t':
            plotTitle = arg
        if opt == '-z':
            zone = arg

    print(f"plot title is {plotTitle}")

    print(f"outputfile is {outputFile}")

    # To connect MySQL database
    conn = pymysql.connect(host=DatabaseServer, user=User, passwd=Password, db=Database)
        
    curr = conn.cursor()

    # Select query
    if zone != False:
        curr.execute(f"select * from tempData where zone = '{zone}' order by temp_id desc limit 5")
    else:
        curr.execute("select * from tempData order by temp_id desc limit 5")
    output = curr.fetchall()

    sqlID = []
    sqlDate = []
    sqlZoneLoc = []
    sqlTempF = []
    sqlDict = defaultdict(dict)
    # print(output)
    for i in output:
        valueID = i[0]
        valueDate = i[1]
        valueZoneLoc = i[2]
        valueTempF = i[3]
        
        sqlID.append(valueID)
        sqlDate.append(valueDate)
        sqlZoneLoc.append(valueZoneLoc)
        sqlTempF.append(valueTempF)
        # print(valueID, valueDate, valueZoneLoc, valueTempF)
        sqlDict[valueID]["zone"] = valueZoneLoc
        sqlDict[valueID]["date"] = valueDate
        sqlDict[valueID]["tempF"] = valueTempF

    # To close the connection
    conn.close()

    # print(sqlDict)

    for id in sqlDict.items():
        zone = id[1]["zone"]
        date = id[1]["date"]
        tempF = id[1]["tempF"]
        print(id, zone, date, tempF)

    plt.plot(sqlDate,sqlTempF,label=zone)

    plt.title(plotTitle)
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