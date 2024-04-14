sudo apt-get update
sudo apt-get install libmysqlclient-dev pkg-config
export MYSQLCLIENT_CFLAGS=-I/usr/include/mysql
export MYSQLCLIENT_LDFLAGS=-L/usr/lib/mysql
brew --prefix mysql
ls $(brew --prefix mysql)/include/mysql.h
export CPPFLAGS="-I$(brew --prefix mysql)/include"
export LDFLAGS="-L$(brew --prefix mysql)/lib"
pip install mysqlclient

########################### MYSQL DB SETUP ##########################################

#sh-4.4# mysql -u root -p
#Enter password:
#Welcome to the MySQL monitor.  Commands end with ; or \g.
#Your MySQL connection id is 8
#Server version: 8.3.0 MySQL Community Server - GPL
#
#Copyright (c) 2000, 2024, Oracle and/or its affiliates.
#
#Oracle is a registered trademark of Oracle Corporation and/or its
#affiliates. Other names may be trademarks of their respective
#owners.
#
#Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
#
#mysql> show databases
#    -> ;
#+--------------------+
#| Database           |
#+--------------------+
#| information_schema |
#| mysql              |
#| performance_schema |
#| sys                |
#+--------------------+
#4 rows in set (0.02 sec)
#
#mysql> create database easyLifeDB
#    -> ;
#Query OK, 1 row affected (0.01 sec)
#
#mysql> show databases
#    -> ;
#+--------------------+
#| Database           |
#+--------------------+
#| easyLifeDB         |
#| information_schema |
#| mysql              |
#| performance_schema |
#| sys                |
#+--------------------+
#5 rows in set (0.01 sec)
