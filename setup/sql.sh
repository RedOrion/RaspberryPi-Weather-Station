#!/bin/bash

while getopts s:h: flag
do
    case "${flag}" in
        s) mysqlserver=${OPTARG};;
        h) weatherstationpi=${OPTARG};;
        c) sensorsPass=${OPTARG};;
        d) websitePass=${OPTARG};;

    esac
done
echo "MysqlServer: $mysqlserver";
echo "Server: $weatherstationpi";
echo "Sensors password: $sensorsPass"
echo "Website password: $websitePass"


if [ -z "$sensorPass" ]
then
      echo "\$sensorPass is empty"
      sensorPass = testPassowrd
else
      echo "\$sensorPass is NOT empty"
fi

if [ -z "$websitePass" ]
then
      echo "\$sensorPass is empty"
      sensorPass = websiteTest
else
      echo "\$sensorPass is NOT empty"
fi

mysql -u root -p -h $mysqlserver << EOF
CREATE DATABASE IF NOT EXISTS sensors;
USE sensors;
CREATE TABLE IF NOT EXISTS tempData (temp_id INT AUTO_INCREMENT KEY, Date datetime default now(), zone VARCHAR(64), temperature DOUBLE);
CREATE USER IF NOT EXISTS 'sensors'@'$weatherstationpi' IDENTIFIED by '${!sensorsPass}';                                                
GRANT INSERT,SELECT ON sensors.* TO 'sensors'@'$weatherstationpi';
CREATE USER IF NOT EXISTS 'website'@'$weatherstationpi' IDENTIFIED by '${!websitePass}';
GRANT SELECT ON sensors.* TO 'website'@'$weatherstationpi';
FLUSH PRIVILEGES;

EOF
