def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error. Division by zero."
    return x / y

def modulus(x, y):
    return x % y

def get_number(message):
    while True:
        user_input = input(message)
        try:
            number = float(user_input)
            return number
        except ValueError:
            print("Invalid input. Kindly, enter a numeric value.")

def get_choice():
    while True:
        choice = input("Enter your choice (1/2/3/4/5): ")
        if choice in ["1", "2", "3", "4", "5"]:
            return choice
        else:
            print("Invalid choice. Please select a valid operation.")



print("Select an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")

choice = get_choice()

num1 = get_number("Type your first number: ")
num2 = get_number("Type your second number: ")

if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    result = divide(num1, num2)
    if result == "Error. Division by zero.":
        print(result)
    else:
        print(f"{num1} / {num2} = {result:.2f}")
elif choice == '5':
    print(f"{num1} % {num2} = {modulus(num1, num2)}")

