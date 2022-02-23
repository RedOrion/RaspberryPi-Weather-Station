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

        from datetime import datetime, timedelta
        now = datetime.now()

    # To close the connection
    conn.close()

    # print(sqlDict)

    uniqueZones = []
    allTimeX = []
    allTimeY = []
    hour24X = []
    hour24Y = []


    for id, value in sqlDict.items():
        zone = value["zone"]
        dateZ = value["date"]
        tempF = value["tempF"]
        # print(id, zone, date, tempF)
        if zone not in uniqueZones:
            uniqueZones.append(zone)
        if now-timedelta(hours=24) <= dateZ <= now:
            allTimeX.append(dateZ)
            allTimeY.append(tempF)

    print(uniqueZones)

    fig = plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.plot(allTimeX, allTimeY)
    plt.subplot(1, 2, 2)
    plt.plot(hour24X, hour24Y)
    fig.tight_layout()

    # fig, ((ax1, ax2)) = plt.subplots(1, 2)

    # ax1.plot(sqlDate, sqlTempF)
    # ax2.plot(sqlDate, sqlTempF, 'tab:orange')
    # ax1.set_title("All time")
    # ax2.set_title("24 hours")

    for ax in fig.get_axes():
        ax.label_outer()

    # plt.plot(sqlDate,sqlTempF,label=zone)

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