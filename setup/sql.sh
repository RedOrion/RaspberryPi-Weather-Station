#!/bin/bash

while getopts s: flag
do
    case "${flag}" in
        s) mysqlserver=${OPTARG};;
    esac
done
echo "MysqlServer: $mysqlserver";

sudo mysql -u root -p -h $mysqlserver << EOF
CREATE DATABASE IF NOT EXISTS sensors;
USE sensors;
CREATE TABLE IF NOT EXISTS tempData (temp_id INT AUTO_INCREMENT KEY, takeDate DATE, takeTime TIME, zone VARCHAR(64), temperature DOUBLE);
CREATE USER IF NOT EXISTS 'sensors'@'localhost' IDENTIFIED by 'sensorsTest';                                                
GRANT INSERT ON sensors.* TO 'sensors'@'localhost';
CREATE USER IF NOT EXISTS 'website'@'localhost' IDENTIFIED by 'websiteTest';
GRANT SELECT ON sensors.* TO 'website'@'localhost';
FLUSH PRIVILEGES;

EOF
