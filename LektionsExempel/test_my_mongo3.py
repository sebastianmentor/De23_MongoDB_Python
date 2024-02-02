from pymongo import MongoClient

# Skapa en anslutning till MongoDB
client = MongoClient ("mongodb://localhost:27017/")

# Valj en databas
db = client.nytt_exempel

# Valj en samling
collection = db.min_samling

# Infoga flera dokument
dokument_list = [
{" name ": " Erik ", "age": 25} ,
{" name ": " Maria ", "age": 32},
{" name ": " Adam ", "age": 3},
{" name ": " Siv ", "age": 30},
{" name ": " Mårten ", "age": 55},
{" name ": " Johan ", "age": 22},
{" name ": " Malin ", "age": 44}
]
collection.insert_many(dokument_list)

# Hitta alla dokument
for doc in collection.find():
    print(doc)

# Ta bort flera dokument
# collection.delete_many({"age": {"$gt": 30}})