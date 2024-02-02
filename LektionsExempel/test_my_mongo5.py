from pymongo import MongoClient

# Skapa en anslutning till MongoDB
client = MongoClient ("mongodb://localhost:27017/")

# Valj en databas
db = client.nytt_exempel

# Valj en samling
collection = db.min_samling
print('-------------------------------')
for doc in collection.find():
    print(doc)
print('-------------------------------')

# Paginering : H m t a 5 dokument , hoppa ver de f r s t a 10
for doc in collection.find().skip(3).limit(5):
    print(doc)
print('-------------------------------')


client.close()