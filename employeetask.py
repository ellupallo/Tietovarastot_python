##  LUO databases-kansioon UUSI TYHJÄ TIEDOSTO employees.db,  

# Path('./databases/employees.db').touch() # touch päivittää aikaleiman, jos tiedosto jo olemassa

##  LUO sqlite-yhteys ja kursori luomaasi employees.db -tiedostoon 
# conn=sqlite3.connect("databases") 

## Tutki us-500.csv -tiedostoa, ja LUO TAULU employees (MIETI KOLUMNIEN TIETOTYYPIT)
##  (vain jos taulua ei ole olemassa) -

## LUO employees -niminen dataframe-tyyppinen muuttuja 
## ja lue siihen us-500.csv -tiedoston sisältö

##  MUUTA employees-dataframe SQL-MUOTOON employees.db -tiedostoon, 
## all_employees-tauluun niin, että indeksit lisätään mukaan ja data yliajetaan, 
## mikäli sitä löytyy

##   katso apua 1.päivän csv_to_sqlite.py -tiedostosta

import sqlite3
from pathlib import Path
import pandas as pd

# Create db connection to TIETOKANTA
# connection = sqlite3.connect("./databases/employees2.db") ### TÄMÄ ON OLENNAINEN 

# # # Create db cursor
# cursor = connection.cursor()### TÄMÄ ON OLENNAINEN


# # Load cursor data into panda dataframe
# us500df= pd.read_csv("us-500.csv")### TÄMÄ ON OLENNAINEN
# print(us500df.head(5))### TÄMÄ ON OLENNAINEN
# print(us500df.columns)### TÄMÄ ON OLENNAINEN
# print(us500df.dtypes)### TÄMÄ ON OLENNAINEN


# # # Write movie data into table. Index, ottaako rivinumerot vai ei
# us500df.to_sql("all2employees", connection, if_exists="replace", index=True) ### TÄMÄ ON OLENNAINEN

# #connection.commit()
# #connection.close()

# Toinen versio

# Create db connection

# import sqlite_connection as db
# connection = db.conn
import sqlite3
connection = sqlite3.connect("./databases/employees3.db") # connection voisi olla myös conn
cursor = connection.cursor()

# Create table with colums (only if table does not already exist) # """ multiline string alkuun ja loppuun
cursor.execute("CREATE TABLE IF NOT EXISTS allemployees3 \
               (first_name TEXT, \
                last_name TEXT, \
                company_name TEXT, \
                address TEXT, \
                city TEXT, \
                county TEXT, \
                state TEXT, zip TEXT,  phone1 TEXT, phone2 TEXT, email TEXT, web TEXT)")

# Load cursor data into panda dataframe
us5002df = pd.read_csv("us-500.csv")

# # Write movie data into table. Index, ottaako rivinumerot vai ei
us5002df.to_sql("allemployees4", connection, if_exists="replace", index=True)

# from faker import Faker
# fake = Faker()
# print(fake.name())
# print(fake.license_plate())
# #connection.commit()
# #connection.close()p