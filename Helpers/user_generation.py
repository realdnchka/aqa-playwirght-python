import string
import random
from Helpers.user import User


def generate_user():
    email = generate_email()
    password = generate_password()

    user = User(email, password)
    return user


def generate_email():
    return generate_string(6).lower() + "@mail.com"


def generate_password():
    return generate_string(8)


def generate_string(length):
    letters = string.ascii_letters
    result = "".join(random.choice(letters) for i in range(length))
    return result
