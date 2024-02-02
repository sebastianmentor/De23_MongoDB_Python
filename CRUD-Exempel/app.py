from pymongo import MongoClient

# Ansluta till MongoDB (ändra denna sträng om din MongoDB har en annan konfiguration)
client = MongoClient("mongodb://localhost:27017/")
db = client.min_databas
users = db.users

# CRUD-operationer
def add_user(name, age):
    users.insert_one({"name": name, "age": age})
    print(f"Lade till användare: {name}")

def get_user(name):
    user = users.find_one({"name": name})
    if user:
        print(f"Hittade användare: {user}")
    else:
        print("Användare hittades inte")

def get_all_users(name):
    multiple_users = users.find({"name":name})
    if multiple_users:
        for user in multiple_users:
            print(f"Hittade användare: {user}")
    else:
        print("Användare hittades inte")

def update_user(name, age):
    result = users.update_one({"name": name}, {"$set": {"age": age}})
    # result_many = users.update_many({"name": name}, {"$set": {"age": age}})
    if result.modified_count:
        print(f"Uppdaterade användare: {name}")
    else:
        print("Ingen uppdatering utförd")

def delete_user(name):
    result = users.delete_one({"name": name})
    if result.deleted_count:
        print(f"Raderade användare: {name}")
    else:
        print("Ingen användare att radera")

def show_users(name):
    result = users.find({"name":name})
    if result:
        for user in result:
            print(user)
    else:
        print(f"Finns inga användare vid namn {name}")

def show_all_users():
    result = users.find()
    if result:
        for user in result:
            print(user)
    else:
        print('Din databas är tom! Get some users!!!!!')

def kill_button():
    result = users.find()
    if result:
        for user in result:
            users.delete_one({"_id":user['_id']})
    else:
        print('Din databas är tom! Get some users!!!!!')


# CLI för att interagera med databasen
while True:
    action = input("Välj en åtgärd (add, get, get_all, update, delete, exit, show): ")
    if action == "exit":
        break
    name = input("Ange namn: ")
    if action in ["add", "update"]:
        age = int(input("Ange ålder: "))
        if action == "add":
            add_user(name, age)
        else:
            update_user(name, age)
    elif action == "get":
        get_user(name)
    elif action == "delete":
        delete_user(name)
    elif action == "get_all":
        get_all_users(name)
    elif action == "show":
        show_users(name)
    elif action == "KILL":
        kill_button()
    elif action == "Show_all":
        show_all_users()
    else:
        print("Ogiltig åtgärd")

client.close()
