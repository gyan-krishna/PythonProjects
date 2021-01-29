# -*- coding: utf-8 -*-
"""
----------Phenix Labs----------
Created on Fri Dec  4 09:04:44 2020
@author: Gyan Krishna

Topic: Connecting to Database
"""

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="backtrack",
 # database="testdb"
)
mycursor = mydb.cursor()
print(mydb)

#mycursor.execute("CREATE DATABASE testdb")

mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)