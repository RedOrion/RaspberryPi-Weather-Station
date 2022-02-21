#!/bin/bash

show_help()
{
echo "
        Usage: sql-newuser.sh [-m mysql.local] [-c currentIP] [-s MySQLSensorPass] [-w MySQLWebsitePass] [-y (sensor default pass)] [-z (website default pass)]

        -m sql server
        -c client ip/hostname
        -s mysql sensor pass
        -w mysql website pass
        -y sensor default pass
        -z website default pass

        -H Help
"
}     

while getopts m:c:swyzh flag
do
    case "${flag}" in
        m) mysqlserver=${OPTARG};;
        c) client=${OPTARG};;
        s) sensorsPass=${OPTARG};;
        w) websitePass=${OPTARG};;
        y) sensorDefaultPass="1";;
        z) websiteDefaultPass="1";;
        h) show_help
            exit
            ;;

    esac
done


if [ "$sensorDefaultPass" = "1" ]
then
      sensorsPass="testPassword"
fi

if [ "$websiteDefaultPass" = "1" ]
then
      websitePass="websiteTest"
fi

echo "MysqlServer: $mysqlserver";
echo "Server: $client";
echo "Sensors password: $sensorsPass"
echo "Website password: $websitePass"

if [ -z "$sensorsPass" ]
then
      echo "\$sensorPass is empty"
else
      echo "\$sensorPass is NOT empty"
      mysql -u root -p -h $mysqlserver << EOF
DROP USER IF EXISTS 'sensors'@'$client';
CREATE USER IF NOT EXISTS 'sensors'@'$client' IDENTIFIED by '$sensorsPass';                                                
GRANT INSERT,SELECT ON sensors.* TO 'sensors'@'$client';
FLUSH PRIVILEGES;

EOF
fi

if [ -z "$websitePass" ]
then
      echo "\$websitePass is empty"
else
      echo "\$websitePass is NOT empty"
      mysql -u root -p -h $mysqlserver << EOF
CREATE USER IF NOT EXISTS 'website'@'$client' IDENTIFIED by '${!websitePass}';
GRANT SELECT ON sensors.* TO 'website'@'$client';
FLUSH PRIVILEGES;

EOF
fi