from pymongo import MongoClient

# Skapa en anslutning till MongoDB
client = MongoClient ("mongodb://localhost:27017/")

# Valj en databas
db = client.nytt_exempel

# Valj en samling
collection = db.min_samling