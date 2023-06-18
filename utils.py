from faker import Faker
import string
import random
import requests

def generate_password(length: int = 10)-> str:
    chars = string.ascii_letters + string.digits
    
    result =""
    for _ in range(length):
        result += random.choice(chars)
    return result


fake = Faker()


def generate_name(length: int = 100) ->str:
    result = ""
    for _ in range(length):
        first_name = fake.first_name()
        email = f"{first_name}.{fake.last_name()}@gmail.com".lower()
        result += first_name
        result += " "
        result += email
        result += '\n'
        
    return result


def count_astros():
    r = requests.get('http://api.open-notify.org/astros.json')
    data = r.json()
    number_astros = str(data["number"])
    return f'The number of cosmonauts at the moment is {number_astros} people!!!'