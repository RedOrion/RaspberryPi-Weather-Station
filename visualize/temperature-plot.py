#!/usr/bin/python3

from datetime import date
from itertools import count
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

    print(f"plot title: {plotTitle}")

    print(f"output file: {outputFile}")

    # To connect MySQL database
    conn = pymysql.connect(host=DatabaseServer, user=User, passwd=Password, db=Database)
        
    curr = conn.cursor()

    # Select query
    if zone != False:
        curr.execute(f"select * from tempData where zone = '{zone}' order by temp_id desc limit 5")
    else:
        curr.execute("select * from tempData")
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

        from datetime import datetime, timedelta
        now = datetime.now()

    # To close the connection
    conn.close()

    # print(sqlDict)

    # Get unique zones
    uniqueZones = []
    for id, value in sqlDict.items():
        zone = value["zone"]
        dateZ = value["date"]
        tempF = value["tempF"]
        # print(id, zone, date, tempF)
        if zone not in uniqueZones:
            uniqueZones.append(zone)
    totalUnique = len(uniqueZones)
    print(f"Total Unique: {totalUnique}")
    countUnique = 0

    # Plot for each unique zone
    
    fig, ax = plt.subplots(totalUnique, 3, figsize = (30,4))
    print(fig)
    print(ax)
    
    for uZones in uniqueZones:
        print(uZones)
        plotX = []
        plotY = []
        hours12X = []
        hours12Y = []
        hours24X = []
        hours24Y = []
        for id, value in sqlDict.items():
            zone = value["zone"]
            dateZ = value["date"]
            tempF = value["tempF"]
            if zone == uZones:
                plotX.append(dateZ)
                plotY.append(tempF)
                if now-timedelta(hours=24) <= dateZ <= now:
                    hours24X.append(dateZ)
                    hours24Y.append(tempF)
                if now-timedelta(hours=12) <= dateZ <= now:
                    hours12X.append(dateZ)
                    hours12Y.append(tempF)
        if totalUnique == 1:
            print("Single Zone")
            ax[2].plot(plotX, plotY, 'r')
            ax[2].set_title("All Time")

            ax[0].plot(hours12X, hours12Y, 'g')
            ax[0].set_title("12 Hours")
            
            ax[1].plot(hours24X, hours24Y, 'b')
            ax[1].set_title("24 Hours")
        else:
            print("Multiple Zones")

            ax[countUnique, 2].plot(plotX, plotY, 'r')
            ax[countUnique, 2].set_title("All Time")

            ax[countUnique, 0].plot(hours12X, hours12Y, 'g')
            ax[countUnique, 0].set_title("12 Hours")

            ax[countUnique, 1].plot(hours24X, hours24Y, 'b')
            ax[countUnique, 1].set_title("24 Hours")

        countUnique += 1

    #plt.show()
    if not outputFile:
        outputFile = "temperature.png"
    plt.savefig(outputFile, bbox_inches='tight')

if __name__ == "__main__":
   main(sys.argv[1:])