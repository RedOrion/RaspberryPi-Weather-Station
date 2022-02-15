#!/bin/bash

while getopts s:h: flag
do
    case "${flag}" in
        s) mysqlserver=${OPTARG};;
        h) weatherstationpi=${OPTARG};;
    esac
done
echo "MysqlServer: $mysqlserver";
echo "Weather Station Pi: $weatherstationpi";

mysql -u root -p -h $mysqlserver << EOF
CREATE DATABASE IF NOT EXISTS sensors;
USE sensors;
CREATE TABLE IF NOT EXISTS tempData (temp_id INT AUTO_INCREMENT KEY, Date datetime default now(), zone VARCHAR(64), temperature DOUBLE);
CREATE USER IF NOT EXISTS 'sensors'@'$weatherstationpi' IDENTIFIED by 'sensorsTest';                                                
GRANT INSERT ON sensors.* TO 'sensors'@'$weatherstationpi';
CREATE USER IF NOT EXISTS 'website'@'$weatherstationpi' IDENTIFIED by 'websiteTest';
GRANT SELECT ON sensors.* TO 'website'@'$weatherstationpi';
FLUSH PRIVILEGES;

EOF
