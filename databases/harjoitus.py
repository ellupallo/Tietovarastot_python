# Luo yhteys movies.db -tiedostoon
# Hae 10 ensimäistä elokuvaa
# Kirjoita tulokset csv -tiedostoon

# import sqlite3
import pandas as pd
from pathlib import Path
import sqlite_connection as db # tuodan sqlite_connection eli virhe-homma ja aliaksella db

connection = db.com

df = pd.read_sql("SELECT * FROM movies WHERE popularity >= 10", connection) # parametriksi yhteys=connection perään
df.to_csv('ekat_10.csv', index=False)

# cursor = connection.cursor()   
# Execute the query to select the first 10 rows
# cursor.execute("SELECT * FROM elokuvat LIMIT 10")

# Fetch all rows from the executed query
# rows = cursor.fetchall()

# Print the rows
# for row in rows:
#     print(row)

# Close the cursor and connection
# cursor.close()
# connection.close()
