#!/bin/bash

sudo mysql -u root -p -h localhost << EOF
CREATE DATABASE sensors;
USE sensors;
CREATE TABLE tempData (temp_id INT AUTO_INCREMENT KEY, takeDate DATE, takeTime TIME, zone VARCHAR(64), temperature DOUBLE);
CREATE USER 'sensors'@'localhost' IDENTIFIED by 'testPassword';                                                
GRANT INSERT ON sensors.* TO 'sensors'@'localhost';
FLUSH PRIVILEGES;

EOF
