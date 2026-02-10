# Simple Calculator Project

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


while True:
    print("\n--- Simple Calculator ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Clear")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '6':
        print("Exiting calculator. Thank you!")
        break

    if choice == '5':
        print("Calculator cleared.")
        continue

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result =", add(num1, num2))
            elif choice == '2':
                print("Result =", subtract(num1, num2))
            elif choice == '3':
                print("Result =", multiply(num1, num2))
            elif choice == '4':
                print("Result =", divide(num1, num2))

        except ValueError:
            print("Invalid input! Please enter numbers only.")
    else:
        print("Invalid choice! Please select 1 to 6.")
