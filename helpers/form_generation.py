import string
import random
from helpers.form_dto import Form


def generate_form():
    name = generate_name()
    email = generate_email()
    current_address = generate_address()
    permanent_address = generate_address()

    form = Form(name, email, current_address, permanent_address)
    return form


def generate_email():
    return generate_string(6).lower() + "@test.com"


def generate_address():
    return generate_string(random.randint(10, 30))


def generate_name():
    length_name = random.randint(3, 10)
    length_surname = random.randint(3, 15)
    return generate_string(length_name).lower().capitalize() + ' ' + generate_string(length_surname).lower().capitalize()


def generate_string(length):
    letters = string.ascii_letters
    result = "".join(random.choice(letters) for i in range(length))
    return result
