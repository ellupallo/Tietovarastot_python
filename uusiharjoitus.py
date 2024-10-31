# Luo yhteys movies.db -tiedostoon
# Hae 10 ensimäistä elokuvaa
# Kirjoita tulokset csv -tiedostoon

import sqlite3
import pandas as pd
from pathlib import Path
# import sqlite_connection as db # tuodan sqlite_connection eli virhe-homma ja aliaksella db

connection = sqlite3.connect("./databases/movies.db")
df = pd.read_sql("SELECT * FROM elokuvat LIMIT 10", connection) # parametriksi yhteys=connection perään
df.to_csv('ekat_10.csv', index=False)

connection.close()