from pymongo import MongoClient

# Skapa en anslutning till MongoDB
client = MongoClient ("mongodb://localhost:27017/")

# Valj en databas
db = client.nytt_exempel

# Valj en samling
collection = db. min_samling

# Skapa ett nytt dokument
nytt_dokument = {" name ": " Anna ", "age": 99}
nytt_dokument2 = {" name ": " Kalle ", "age": 5}

# Infoga dokumentet i samlingen
resultat = collection.insert_one(nytt_dokument)
resultat2 = collection.insert_one(nytt_dokument2)




client.close()