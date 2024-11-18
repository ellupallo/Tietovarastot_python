# mySQL -liitännäiset kaikki alkaa my -sanalle
# sopivat kirjasto PyMySQL tai MySQL Connectors (mysql-connector-python) - (tai pandas??)

# pip install mysql-connector-python

import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="oka",
        password="Vesseli",
        database="okan"
        )

except:
    print("CONNECTION FAILED")

# Toinen vaihtoehto:
# pip install pymysql
# import pymysql

# try:
#     conn = pymysql.connect(
#         host="localhost",
#         user="oka",
#         password="Vesseli",
#         database="okan"
#         )
#     print("connection ok")
# except:
#     print("connection failed")

