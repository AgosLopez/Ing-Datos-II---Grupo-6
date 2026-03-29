from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client["countries"]

coleccion = db["countries"]

for doc in coleccion.find():
    print(doc)