import sqlite3

conn = sqlite3.connect("albums.db")
cursor = conn.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS albums (id integer primary key \
        , artist_name text \
        , album_name text \
        ,year text \
        , genre text)"
)
conn.commit() # ilman tätä ei tallenna lisäystä ohjelman sulkeutuessa

def add_album(artist, album, year, genre):
    ##LISÄÄ INSERT-LAUSE,JOKA LISÄÄ TIETOKANTAAN ANNETUT TIEDOT OMAKSI RIVIKSEEN

  # (id, artist_name, album_name, year, genre) voi myös listata kenttien nimet, muttei ole pakko

    cursor.execute('''
    INSERT INTO albums 
    VALUES (NULL,?, ?, ?, ?)
    ''', (artist, album, year, genre))
       
    conn.commit() # ilman tätä ei tallenna lisäystä ohjelman sulkeutuessa


def fetch_albums():
    cursor.execute("SELECT * FROM albums")    
    rows = cursor.fetchall()
    result = []
    for row in rows:
        result.append(
            str(row[0])
            + "-"
            + str(row[1])
            + "-"
            + row[2]
            + "-"
            + row[3]
            + "-"
            + str(row[4])
        )
    return result


def remove(selected_album):
    # LISÄÄ DELETE-LAUSEKE->POISTETAAN ID:N MUKAAN RIVI (ID:N SAA SELVILLE parameterina tullesta selected_album:ista!)
   
    cursor.execute('''
    DELETE FROM albums 
    WHERE id = ?
    ''', (selected_album[0],)) #tuple, joka vuoksi, 

    conn.commit()  # Commit the deletion to save the change


 
def update(selected_album, artist, album, year, genre):
    #LISÄÄ UPDATE-LAUSE, JOKA PÄIVITÄÄ RIVIN ID:n MUKAAN (ID:N SAA SELVILLE parameterina tullesta selected_album:ista)
    cursor.execute(
        "UPDATE albums SET artist_name = ?, album_name = +, year = ?, genre = ?, WHERE id = ?",
        (artist, album, year, genre,selected_album[0])
    )

    conn.commit()

def get_max_id():
    cursor.execute("SELECT MAX(id) from albums")
    res = cursor.fetchone()
    if res[0] != None:
        return res[0]
    else:
        return 0

                


def __del__():  # destructor call when all instances of object has been deleted
    print("__del__ called")
    conn.close()
