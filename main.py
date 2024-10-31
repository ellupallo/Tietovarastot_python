import sqlite_connection as db # tuodan sqlite_connection eli virhe-homma ja aliaksella db
connection = db.conn # connection on vain nimi, joka annetaan fileelle

# JOMPI KUMPI TAPA, RIVITETTY TAI EI
# rows = connection.execute("SELECT title, popularity FROM movies WHERE popularity >=20") 
cursor = connection.execute("SELECT title, popularity \
                          FROM movies \
                          WHERE popularity >=20") 

# SELECT onnistuu ilman kursoria, mutta kursori on mekanisimi, joka mahdollistaa liikkumisen rivien ja kolumnien välillä (lukupää)
# Pakko käyttää, kun resulttina palautuu
# https://docs.python.org/3/library/sqlite3.html -- ohje

# for row in rows: >>> fileen nimi olisi voinut olla mitä vaan
#     print(row)

# for row in cursor: >>> toimii
#     print(row)

# print(rows[0]) >> ei toimi

# result = cursor.fetchone() >>> tällä ottaa eka rivin 
# print(result)

# rivien hakeminen
iteraattori = iter(cursor)
rivi = next(iteraattori) # next siirtyy indexissä yhdellä eteepäin, HUOM! HAKEE VAIN kursoriin valitusta!!
rivi2 = next(iteraattori)
print(rivi2)

# suositellaan aina käyttämään
connection.close()

