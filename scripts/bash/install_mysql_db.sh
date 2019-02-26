#!/usr/bin/env bash
# Install MySQL database v5.7
sudo apt-get update -y
sudo apt-get install mysql-server -y
wget http://dev.mysql.com/get/mysql-apt-config_0.6.0-1_all.deb
sudo dpkg -i mysql-apt-config_0.6.0-1_all.deb
sudo apt-get update -y
sudo apt-get install mysql-server
sudo service mysql start
