import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_generator():
    print("Welcome ,Here you can generate your Password")

    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return password_generator()

    if length <= 0:
        print("Invalid length. Please enter a positive number.")
        return password_generator()

    password = generate_password(length)
    print(f"Your Generated Password: {password}")

if __name__ == "__main__":
    password_generator()
