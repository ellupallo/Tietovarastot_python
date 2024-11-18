from pymongo import MongoClient
from dotenv import load_dotenv
import pandas as pd
import os

# from mongo_connection import connect
client = MongoClient("mongodb+srv://oilikalm:mongokokeilu@cluster0.jfqoq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# client = connect()
if client is not None:
    db = client["sample_mflix"]
    collection = db["movies"]

    cursor= collection.find().limit(5) # hakee kaikki dokumentit collectionissa cursor, limit 5
    # find_one jne
    for document in cursor: # for loop hakee yksi kerrallaan, kunnes hakenut kaikki
        #print(document) # printaa kaikki kentät
        print(document["_id"]) # haku dictionary -tyyppisesti printtaa vain id:t
        print(document["title"])

# Mongo DB query - tsekkaa...

# client.close()