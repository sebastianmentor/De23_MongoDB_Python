from pymongo import MongoClient

# Skapa en anslutning till MongoDB
client = MongoClient ("mongodb://localhost:27017/")

# Valj en databas
db = client.nytt_exempel

# Valj en samling
collection = db.min_samling

# Gruppera dokument efter ålder och räkna antalet
pipeline = [
{"$group": {"_id": "$age", "antal": {"$sum": 1}}}
]
for result in collection . aggregate ( pipeline ):
    print( result )

client.close()