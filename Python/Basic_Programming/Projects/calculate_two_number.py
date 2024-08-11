# SHOW DISPLAY
def show_disply():
    print("\nWelcome to the python basic calculator")
    print("""
        Press 1 for  Addition
        Press 2 for Substration
        Press 3 for Multiplication
        Press 4 for Divison
        
        """)
    
# TAKE NUMBER
def take_number_from_user():
    oper = int(input("Enter from 1 to 4 for operation :"))
    if oper <= 4:
        num1 = float(input("Enter your first number :"))
        num2 = float(input("Enter your second number :"))
        return oper, num1, num2
    else:
        print("\nInvalid Operation")
        return None, None, None

# OPERATION
def operation(oper, num1, num2):
    if oper == 1:
        print("Addition is activated.")
        print("{} + {} = {}".format(num1, num2, num1 + num2)) 
    elif oper == 2:
        print("Substration is activated.")
        print("{} - {} = {}".format(num1, num2, num1 - num2))
    elif oper == 3:
        print("Multiplication is activated.")
        print("{} * {} = {}".format(num1, num2, num1 * num2))
    elif oper == 4:
        if num2 !=0:
            print("Division is activated.")
            print("{} / {} = {}".format(num1, num2, num1 / num2))
        else:
            print("Error! Division by zero is not allowed.")
    else:
        print('Give valid operation.')

# MAIN LOOP 
def calculate():
    while True:
        show_disply()
        oper, num1, num2 = take_number_from_user()
        operation(oper, num1, num2)
        if oper is not None:
            cont = input("Do you want to continue? (yes/no): ")
            if cont.lower() != "yes":
                break
            else:
                print("Thank you for using ... Have Fun")

# CALL 
calculate()

# TIME -> 07:12AM Sunday, 11 August 2024 (IST)