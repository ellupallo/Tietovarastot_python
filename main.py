import sqlite_connection as db # tuodan sqlite_connection eli virhe-homma ja aliaksella db
import pandas as pd
import csv
connection = db.conn # connection on vain nimi, joka annetaan fileelle

# JOMPI KUMPI TAPA, RIVITETTY TAI EI
# rows = connection.execute("SELECT title, popularity FROM movies WHERE popularity >=20") 
# cursor = connection.execute("SELECT title, popularity \
#                           FROM movies \
#                           WHERE popularity >=20") 

# with db.conn as connection:
#     cursor = connection.execute("SELECT title, popularity FROM movies WHERE popularity >=10") 

# EKA RIVIN TULOSTUS:
# result = cursor.fetchone() # >>> tällä ottaa eka rivin 
# print(result)

# ***************************************************
# !) CSV fileen luominen PANDAS >>>> KOKEILU.CSV
with db.conn as connection:
    # Execute the query and read the result into a DataFrame
    df = pd.read_sql("SELECT title, popularity FROM movies WHERE popularity >= 20", connection) # parametriksi yhteys=connection perään
    
    # Save the DataFrame to a CSV file
    df.to_csv('kokeilu.csv', index=False)


# 2) CSV fileen luominen CSV >>>>> LEFFAT.CSV
# Open a CSV file to write the results
cursor = connection.execute("SELECT title, popularity \
                           FROM movies \
                           WHERE popularity >=20") 
# 1) Tallenna joka rivi listaan
# 2) Tallenna listan data csv-tiedostoon csv-writerilla

lista =[]
for row in cursor: # fetchall - > palauttaa suoraan listan, ei tarvitse for -luuppia
    lista.append(list(row))
#print(lista)
with open('leffat.csv', mode='w', encoding="utf-8", newline='') as file:
    writer = csv.writer(file) # annetaan parametriksi file, jona tyhjä on perustettu
    # Write all rows
    writer.writerows(lista)


# *******************************************************
# CSV:n luku sisään näin PANDAS
# leffat = pd.read_csv("kokeilu.csv")
# print(leffat.head(5))

# with open('kokeilu.csv', mode='r') as file:
#     kokeilu = csv.reader(file)
# kokeilu = pd.read_csv('kokeilu.csv')
# print(kokeilu.head(5))


# SELECT onnistuu ilman kursoria, mutta kursori on mekanisimi, joka mahdollistaa liikkumisen rivien ja kolumnien välillä (lukupää)
# Pakko käyttää, kun resulttina palautuu
# https://docs.python.org/3/library/sqlite3.html -- ohje

# for row in rows: >>> fileen nimi olisi voinut olla mitä vaan
#     print(row)

# for row in cursor: >>> toimii
#     print(row)

# print(rows[0]) >> ei toimi



# rivien hakeminen
# iteraattori = iter(cursor)
# rivi = next(iteraattori) # next siirtyy indexissä yhdellä eteepäin, HUOM! HAKEE VAIN kursoriin valitusta!!
# rivi2 = next(iteraattori)
# print(rivi2)


# suositellaan aina käyttämään
# connection.close()