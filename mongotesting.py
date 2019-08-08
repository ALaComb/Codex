import pymongo
import json
import os

def update_spells():
    newcol = mydb["spells"]
    print('Created spell collection')
    with open("./data/spells/index.json",'r') as f:
        docs = json.load(f)
    for doc in docs:
        with open(f'./data/spells/{docs[doc]}','r') as f:
            data = json.load(f)
            x = newcol.insert_many(data["spell"])

    count = 0
    for i in newcol.find({},{"name":1}):
        count += 1
    print(f'Inserted {count} spells.')
    return

def update_monsters():
    newcol = mydb["monsters"]
    print('Created monster collection')
    with open("./data/bestiary/index.json",'r') as f:
        docs = json.load(f)
    for doc in docs:
        with open(f'./data/bestiary/{docs[doc]}','r') as f:
            data = json.load(f)
            x = newcol.insert_many(data["monster"])

    count = 0
    for i in newcol.find({},{"name":1}):
        count += 1
    print(f'Inserted {count} creatures.')
    return

db_conn = pymongo.MongoClient("mongodb://CodexDB:Llqlmfxmv3iY5XEP@codexcluster-shard-00-00-rje0a.mongodb.net:27017,codexcluster-shard-00-01-rje0a.mongodb.net:27017,codexcluster-shard-00-02-rje0a.mongodb.net:27017/test?ssl=true&replicaSet=CodexCluster-shard-0&authSource=admin&retryWrites=true&w=majority")
mydb = db_conn["5eContent"]
if "spells" in mydb.list_collection_names():
    mydb["spells"].drop()
update_spells()
if "monsters" in mydb.list_collection_names():
    mydb["monsters"].drop()
update_monsters()



# mydb = db_conn["hello"]
# mycol = mydb["customers"]
# db_conn.drop_database('mydatabase')
# mydict = {"name": "John", "address": "Highway 37" }
# x = mycol.insert_one(mydict)
# print(db_conn.list_database_names())
# print(mydb.list_collection_names())

# print(x.inserted_id)

# mylist = [
#   { "name": "Amy", "address": "Apple st 652"},
#   { "name": "Hannah", "address": "Mountain 21"},
#   { "name": "Michael", "address": "Valley 345"},
#   { "name": "Sandy", "address": "Ocean blvd 2"},
#   { "name": "Betty", "address": "Green Grass 1"},
#   { "name": "Richard", "address": "Sky st 331"},
#   { "name": "Susan", "address": "One way 98"},
#   { "name": "Vicky", "address": "Yellow Garden 2"},
#   { "name": "Ben", "address": "Park Lane 38"},
#   { "name": "William", "address": "Central st 954"},
#   { "name": "Chuck", "address": "Main Road 989"},
#   { "name": "Viola", "address": "Sideway 1633"}
# ]

# x = mycol.insert_many(mylist)
# print(x.inserted_ids)

#Account name: MongoDB
#PW: password
#Account Domain: mongodb
#Service Name: MongoDB

