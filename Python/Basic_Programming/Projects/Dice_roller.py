def print_dice(number):
    if number == 1:
        print("""
    |---------|
    |         |
    |    O    |
    |         |
    |---------|
        """)
    elif number == 2:
        print("""
    |---------|
    | O       |
    |         |
    |       O |
    |---------|
        """)
    elif number == 3:
        print("""
    |---------|
    | O       |
    |    O    |
    |       O |
    |---------|
        """)
    elif number == 4:
        print("""
    |---------|
    | O     O |
    |         |
    | O     O |
    |---------|
        """)
    elif number == 5:
        print("""
    |---------|
    | O     O |
    |    O    |
    | O     O |
    |---------|
        """)
    elif number == 6:
        print("""
    |---------|
    | O     O |
    | O     O |
    | O     O |
    |---------|
        """)

store = []
while input('Do you want to play Dice (y/n):').lower() == 'y':
    import random
    print_dice(random.randint(1, 6))
    store.append(random.randint(1, 6))
    
print("\nYou chose not to roll the dice.")
print("\nThe numbers you rolled were: ", store)

# TIME -> 7:37 am Wednesday, 14 August 2024 (IST)