import random
import string

import requests

def RandomCharacterGenerator(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def RandomStringGenerator(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

def RandomDigitGenerator(length):
    return ''.join(random.choices(string.digits, k=length))

def IPAddressGenerator():
    ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    return ip

def UserAgentGenerator():
    # Random iOS version
    ios_version = f"{random.randint(10, 14)}_{random.randint(0, 9)}"

    # Random iPhone model
    iphone_models = ["iPhone 12", "iPhone 11", "iPhone XS", "iPhone XR", "iPhone X", "iPhone 8", "iPhone 7"]
    iphone_model = random.choice(iphone_models)

    # Random Safari version
    safari_version = f"{random.randint(600, 605)}.{random.randint(0, 9)}.{random.randint(10, 99)}"

    # Constructing the user agent string
    user_agent = f"Mozilla/5.0 (iPhone {iphone_model}; CPU iPhone OS {ios_version} like Mac OS X) AppleWebKit/{safari_version} (KHTML, like Gecko) Version/{safari_version} Mobile/15E148 Safari/{safari_version}"
    
    return user_agent

def PhoneNumberGenerator():
    phone_number = "9"  # Start with 9

    for _ in range(9):  # Add 9 more random digits
        phone_number += str(random.randint(0, 9))

    return phone_number

def RandomEmailAddressGenerator():
    url = 'https://randomuser.me/api/?nat=us'
    response = requests.get(url)
    responseData = response.json()
    email1 = f"{responseData['results'][0]['email']}".replace(".", "").strip()
    email2 = email1.replace('@examplecom', f'{RandomDigitGenerator(5)}@gmail.com')
    lower_case = email2.lower()
    return lower_case
