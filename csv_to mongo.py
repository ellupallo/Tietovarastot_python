
# from pymongo import MongoClient
# from dotenv import load_dotenv
# import pandas as pd
# import os
# from mongo_connection import connect

# client = connect()

# df = pd.read_csv("metacritic_games.csv")

# # Muutetaan dataframe ensin dictionaryksi
# data =df.to_dict(orient="records") # orient oletuksena "dict", löytyy myös list, series, split ja index

# # luodaan tietokanta (jos ei löydy) tai luodaan uusi kanta (jos ei löydy)
# db=client["gamesDB"]

# # vastavast luodaan/käytetään collection
# # coll = db["games"]

# # voidaan myös suoraan dataa lisätessä luoda collection
# db.games.insert_many(data) # coll.inseert_many(data)