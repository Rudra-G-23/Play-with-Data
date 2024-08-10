# SHOW MENU
menu = {
    1: {"name": "Pizza", "price": 50},
    2: {"name": "Pasta", "price": 30},
    3: {"name": "Burger", "price": 40},
    4: {"name": "Coffe", "price": 20},
    5: {"name": "Salad", "price": 0}
}

# MENU FORMAT
def display_menu():
    print("YOUR PYTHON RESTURANT ")
    print("-----------------------")
    print("\tOUR MENU")
    print("-----------------------")
    for key, value in menu.items():
        print("press {} for {} price is {}".format(key, value["name"], value["price"]))

    print("\nIn our healthy resturant salad is 'FREE of cost'")

# ORDER ITEMS
def order_item():
    display_menu()
    total_bill = 0
    your_items = []

    while True:
        choices = int(input('\nEnter 1 to 5 for what you want for eat :'))

        if choices in menu:
            item = menu[choices]
            print("Your order item is {}".format(item["name"]))
            total_bill += item["price"]
            your_items.append(item["name"])
            print("Check out our other items ")

            ask = input('\nDo you want anthing (y/n) :')
            
            if ask.lower() != 'y':    
                break          
        else:
            print("Invalid choice. Please choose a number between 1 and 5.")

    print(f"\nYour ordered items are {', '.join(your_items)}")
    print(f"You need to pay :{total_bill}")
    
# CALL FUNCTION
order_item()

# TIME -> 7:50AM Saturday, 10 August 2024 (IST)
