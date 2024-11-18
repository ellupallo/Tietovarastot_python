# import sqlite_connection as db # tuodan sqlite_connection eli virhe-homma ja aliaksella db
import sqlite3
import pandas as pd
from pathlib import Path

# Create empty file
# Path("sql_leffat.db").touch()

# Create db connection
# connection = db.conn
# connection = sqlite3.connect("movies")

# # Create db cursor
# cursor = connection.cursor()

# Create table with colums (only if table does not already exist)
# cursor.execute("CREATE TABLE IF NOT EXISTS movies \
#         (id INT, title TEXT, \
#         overview TEXT, \
#         popularity REAL, \
#         release_date TEXT, \
#         vote_average REAL, \
#         vote_count INT)")

# table_name = "elokuvat"
# # sivupolku.... >cursor.execute(f"SELECT * FROM {table_name}")

# # Load cursor data into panda dataframe
# movie_data = pd.read_csv("kokeilu.csv")

# # Write movie data into table. Index, ottaako rivinumerot vai ei
# movie_data.to_sql("elokuvat", connection, if_exists="append", index=False)

# #connection.commit()
# #connection.close()