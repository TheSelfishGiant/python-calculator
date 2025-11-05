# Simple Calculator Program in Python

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

def power(x, y):
    return x ** y

def modulus(x, y):
    try:
        return x % y
    except ZeroDivisionError:
        return "Error: Cannot modulus by zero."

def calculator():
    print("\n===== Simple Calculator =====")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (**)")
    print("6. Modulus (%)")
    print("7. Exit")

    while True:
        choice = input("\nEnter your choice (1–7): ")

        if choice == '7':
            print("Exiting calculator. Goodbye!")
            break

        if choice not in ('1', '2', '3', '4', '5', '6'):
            print("Invalid input! Please enter a number between 1 and 7.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        if choice == '1':
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            print(f"Result: {num1} ** {num2} = {power(num1, num2)}")
        elif choice == '6':
            print(f"Result: {num1} % {num2} = {modulus(num1, num2)}")

        # Ask user if they want to continue
        next_calc = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if next_calc not in ('yes', 'y'):
            print("Thank you for using the calculator!")
            break

if __name__ == "__main__":
    calculator()
