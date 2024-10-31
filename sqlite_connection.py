# CTRL + ö -> avaa terminaalin
import sqlite3
from sqlite3 import Error

# Hakee tästä kansiosta db kansioon
# Jos yhteyttä ei saada, tulee error, filenot found jne.
## . > nykyinen .. 2 ylöspäin

try:
    conn = sqlite3.connect("./databases/movies.db")
except Error as e:
    print(e)
