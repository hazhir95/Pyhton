import hashlib
import getpass

password_manager = {}

def createAccount():
    username = input("Enter your desired username: ")
    password = getpass.getpass("Enter your desired password: ")
    hashed_password = hashlib.sha512(password.encode()).hexdigest()
    password_manager[username] = hashed_password


    print("Account created successfully!")

def