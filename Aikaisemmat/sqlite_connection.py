# CTRL + ö -> avaa terminaalin
import sqlite3
from sqlite3 import Error

# Hakee tästä kansiosta db kansioon
# Jos yhteyttä ei saada, tulee error, filenot found jne.
## . > nykyinen .. 2 ylöspäin

#region Versio 1

# try:
#     conn = sqlite3.connect("./databases/movies.db") # Tässä luotiin conn -muuttuja. Ottaa yhteyden annettuun fileeseen ja antaa sille nimen conn
#     if conn is None:
#         print("no connection")
#     else:
#         print("connenction OK")


# except Error as e:
#     print(e)
#     conn = None

#endregion


# region Versio 2 (tarkistetaan polku)

import os # operating system, built-in module
db_path = "./databases/movies.db"

if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)  
    print("db found and connected")
else:
    print(f"can't connect {db_path}")

#endregion
