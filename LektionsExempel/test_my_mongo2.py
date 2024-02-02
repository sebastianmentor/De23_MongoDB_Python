from pymongo import MongoClient

# Skapa en anslutning till MongoDB
client = MongoClient ("mongodb://localhost:27017/")

# Valj en databas
db = client.nytt_exempel

# Valj en samling
collection = db.min_samling

post = {"Title":'något',
        "Meddelande": 'text text',
        "Bild": ['url1','url2']}


# Hitta ett dokument
# Ta bort ett dokument
collection.delete_one ({" name ": " Anna "})
dokument = collection.find_one({" name ": " Anna "})
print(dokument)
print(collection.find_one({"_id":'65bcbd0661c21dd2c8ab0fee'}))
dokument2 = collection.find_one({" name ": " Kalle "})
print(dokument2)

dokument3 = collection.find({" name ": " Anna "})
for name in dokument3:
    print(name)


# Uppdatera ett dokument
query = {" name ": " Anna "}
ny_data = {"$set": {"age": 30}}
collection . update_one (query , ny_data )


client.close()