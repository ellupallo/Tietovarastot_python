# python -m pip install "pymongo[srv]"
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()


def connect():
    try:
      
        # client = MongoClient("MONGO")
        global client
        client = MongoClient("mongodb+srv://oilikalm:mongokokeilu@cluster0.jfqoq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        # client = MongoClient(f"mongodb+srv://oilikalm:{('MONGOPASS')}@cluster0.jfqoq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        print("connected")
        return client
    except:
        print("no connection")
        return client


if __name__== '__main__':
    connect()
# connect()

