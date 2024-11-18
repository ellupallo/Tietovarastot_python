import sqlite3

movie_id = 17711 
# movie_id = "1;DROP TABLE movies" # SQL injection esimerkki -> tämä hakukenttään

with sqlite3.connect("./databases/movies.db") as conn:
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM movies WHERE id = {movie_id}") # ei turvallinen eli injektoitavissa