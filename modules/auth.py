from modules.database import load_table, save_table
import getpass

# Setting up a default admin account (runs once) :

def setup_auth():

    users = load_table("users")

    if not users:
        users["admin"] = {
            "username": "admin",
            "password": "admin123"
        }
        save_table("users", users)

# Registering a new staff user :

def register_user():

    users = load_table("users")

    print("\n====== REGISTER NEW USER ======\n")

    username = input("Enter Username : ")

    if username in users:
        print("Username Already Exists!")
        return

    password = getpass.getpass("Enter Password : ")

    users[username] = {
        "username": username,
        "password": password
    }

    save_table("users", users)

    print("\nUser Registered Successfully!")

# Logging in :

def login():

    users = load_table("users")

    print("\n====== LOGIN ======\n")

    for attempt in range(3):
        username = input("Username : ")
        password = getpass.getpass(("Password : "))

        user = users.get(username)

        if user and user["password"] == password:
            print(f"\nWelcome, {username}!")
            return True

        print(f"Invalid Credentials! Attempts left: {2 - attempt}\n")

    print("Too Many Failed Attempts. Exiting.")
    return False