import pymongo
from pymongo import MongoClient

client = MongoClient("mongodb+srv://sam9977:codered1234@cluster0.bsjir.mongodb.net/project?retryWrites=true&w=majority", ssl=True,ssl_cert_reqs='CERT_NONE')
db = client["project"]
collection = db["test1"]

post = {"id": "hello3"}
collection.insert_one(post)
