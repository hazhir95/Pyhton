import hashlib
import getpass
#
# from Demos.win32ts_logoff_disconnected import username
# from docutils.parsers.rst.directives import choice

password_manager = {}

def createAccount():
    username = input("Enter your desired username: ")
    password = getpass.getpass("Enter your desired password: ")
    hashed_password = hashlib.sha512(password.encode()).hexdigest()
    password_manager[username] = hashed_password
    print("Account created successfully!")

def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha512(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

def main():
    while True:
        choice = input("Enter 1 to create an account, 2 to login, or 0 to exit: ")
        match choice:
            case "1":
                createAccount()
            case "2":
                login()
            case "0":
                break
            case _:
                print("Invalid choice.")

if __name__ == "__main__": #running "main" function first
    main()