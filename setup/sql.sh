#!/bin/bash

sudo mysql -u root -p -h localhost << EOF
CREATE DATABASE IF NOT EXISTS sensors;
USE sensors;
CREATE TABLE IF NOT EXISTS tempData (temp_id INT AUTO_INCREMENT KEY, takeDate DATE, takeTime TIME, zone VARCHAR(64), temperature DOUBLE);
CREATE USER IF NOT EXISTS 'sensors'@'localhost' IDENTIFIED by 'testPassword';                                                
GRANT INSERT ON sensors.* TO 'sensors'@'localhost';
FLUSH PRIVILEGES;

EOF
