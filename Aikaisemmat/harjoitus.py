# Luo yhteys movies.db -tiedostoon
# Hae 10 ensimäistä elokuvaa
# Kirjoita tulokset csv -tiedostoon

import pandas as pd
from pathlib import Path
import sqlite_connection as db # tuodan sqlite_connection eli virhe-homma ja aliaksella db

connection = db.conn
df = pd.read_sql("SELECT * FROM elokuvat LIMIT 10", connection) # parametriksi yhteys=connection perään
df.to_csv('v2_ekat_10.csv', index=False)

