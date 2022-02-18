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
else
      echo "\$sensorPass is NOT empty"
      mysql -u root -p -h $mysqlserver << EOF
CREATE USER IF NOT EXISTS 'sensors'@'$weatherstationpi' IDENTIFIED by '${!sensorsPass}';                                                
GRANT INSERT,SELECT ON sensors.* TO 'sensors'@'$weatherstationpi';
FLUSH PRIVILEGES;

EOF
fi

if [ -z "$websitePass" ]
then
      echo "\$sensorPass is empty"
else
      echo "\$sensorPass is NOT empty"
      mysql -u root -p -h $mysqlserver << EOF
CREATE USER IF NOT EXISTS 'website'@'$weatherstationpi' IDENTIFIED by '${!websitePass}';
GRANT SELECT ON sensors.* TO 'website'@'$weatherstationpi';
FLUSH PRIVILEGES;

EOF
fi