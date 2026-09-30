from modules.database import load_table, save_table
import msvcrt


# Password input with asterisks
def get_password():

    password = ""

    while True:

        ch = msvcrt.getch()

        # Enter key
        if ch == b'\r':
            print()
            break

        # Backspace
        elif ch == b'\x08':

            if len(password) > 0:
                password = password[:-1]
                print("\b \b", end="", flush=True)

        # Normal character
        else:
            password += ch.decode()
            print("*", end="", flush=True)

    return password

def setup_auth():

    users = load_table("users")

    if not users:
        users["admin"] = {
            "username": "admin",
            "password": "admin123"
        }

        save_table("users", users)


# Registering a new staff user

def register_user():

    users = load_table("users")

    print("\n====== REGISTER NEW USER ======\n")

    username = input("Enter Username : ")

    if username in users:
        print("Username Already Exists!")
        return

    print("Enter Password : ", end="", flush=True)
    password = get_password()

    users[username] = {
        "username": username,
        "password": password
    }

    save_table("users", users)

    print("\nUser Registered Successfully!")


# Logging in

def login():

    users = load_table("users")

    print("\n====== LOGIN ======\n")

    for attempt in range(3):

        username = input("Username : ")

        print("Password : ", end="", flush=True)
        password = get_password()

        user = users.get(username)

        if user and user["password"] == password:
            print(f"\nWelcome, {username}!")
            return True

        print(f"Invalid Credentials! Attempts left: {2 - attempt}\n")

    print("Too Many Failed Attempts. Exiting.")

    return False