#check that the following has been done
# mysql is installed
# mysql is downloaded (dl is different from install)
# mysql-connector and/or mysql-connector-python is installed

import mysql.connector

db = mysql.connector.connect(
    host= 'localhost',
    user = 'root',
    passwd = 'password123'
)

#cursor obj
cursor = db.cursor()

#create db
cursor.execute("CREATE DATABASE anonco")

