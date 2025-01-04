import random
import string


def generate_password(length: int = 8):
    # Use a breakpoint in the code line below to debug your script.
    # Press F9 to toggle the breakpoint.

    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range(length))
    return password

Password = generate_password()
print(f"Generated Password: {Password}")