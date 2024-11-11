from pymongo import MongoClient
from dotenv import load_dotenv
import pandas
import os

# from mongo_connection import connect
client = MongoClient("mongodb+srv://oilikalm:mongokokeilu@cluster0.jfqoq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
# client = connect()
if client is not None:
    db = client["sample_mflix"]
    collection = db["movies"]

    cursor= collection.find().limit(3) # hakee kaikki dokumentit collectionissa cursor 
    for document in cursor:
        print(document)

# Mongo DB query - tsekkaa...

client.close()