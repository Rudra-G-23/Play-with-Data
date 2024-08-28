import os
import time

car = [
    "  ______",
    " /|_||_\\`.__",
    "(   _    _ _\\",
    "=`-(_)--(_)-'"
]

def your_age():
    age = int(input("Enter your age :"))
    return age

def check_age():
    age = your_age() 
    if age <= 18:
        print("\nyou are Teenager. Your write code for the car")
        for _ in car:
            print(_)            
    elif age > 18:
        move_car()
        

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_car(position):
    for line in car:
        print(" " * position + line)

def move_car():
    for position in range(50):       
        clear_console()
        print_car(position)
        time.sleep(0.1)
        
    print('Made by Rudra.Lets Drive our Automate Car.')

while True:
    inp = input('Do you want to Drive car :')
    if inp.lower() == 'y' :
        check_age()
    else:
        print('Invalid output ')

# TIME -> 07:42am Wednesday, 28 August 2024 (IST)