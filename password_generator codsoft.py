import random
import string

def generate_password(length_of_password):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length_of_password))
    return password

password_length = int(input("Enter the required password length: "))
Password_generated = generate_password(password_length)
print("Password generated randomly :", Password_generated)
