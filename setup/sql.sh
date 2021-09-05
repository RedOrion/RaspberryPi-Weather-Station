#!/bin/bash

while getopts s:w: flag
do
    case "${flag}" in
        s) mysqlserver=${OPTARG};;
        w) weatherstationpi=${OPTARG};;
    esac
done
echo "MysqlServer: $mysqlserver";
echo "Weather Station Pi: $weatherstationpi";

sudo mysql -u root -p -h $mysqlserver << EOF
CREATE DATABASE IF NOT EXISTS sensors;
USE sensors;
CREATE TABLE IF NOT EXISTS tempData (temp_id INT AUTO_INCREMENT KEY, takeDate DATE, takeTime TIME, zone VARCHAR(64), temperature DOUBLE);
CREATE USER IF NOT EXISTS 'sensors'@'$weatherstationpi' IDENTIFIED by 'sensorsTest';                                                
GRANT INSERT ON sensors.* TO 'sensors'@'$weatherstationpi';
CREATE USER IF NOT EXISTS 'website'@'$weatherstationpi' IDENTIFIED by 'websiteTest';
GRANT SELECT ON sensors.* TO 'website'@'$weatherstationpi';
FLUSH PRIVILEGES;

EOF
