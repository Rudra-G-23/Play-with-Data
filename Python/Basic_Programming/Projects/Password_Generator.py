print("\n-------Welcome to the Python World !--------")

import random
import string

letters = int(input("How many letters would you like: "))
numbers = int(input("How many numbers would you like: "))
symbols = int(input("How many symbols would you like: "))
punctuation = ['@', '&', '*', '-', '_']

password = [random.choice(string.ascii_letters) for _ in range(letters)] + \
           [random.choice(string.digits) for _ in range(numbers)] + \
           [random.choice('@&*-_') for _ in range(symbols)]

random.shuffle(password)

print("\nYour Password is:", ''.join(password))


# TIME -> 11:42 pm Tuesday, 13 August 2024 (IST)