def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b


def calculate(num1, operator, num2):
    if operator == "+":
        return add(num1, num2)
    elif operator == "-":
        return subtract(num1, num2)
    elif operator == "*":
        return multiply(num1, num2)
    elif operator == "/":
        return divide(num1, num2)
    else:
        return "Invalid operator"


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def show_menu():
    print("\n--- Simple Calculator ---")
    print("1. Perform Calculation")
    print("2. Clear")
    print("3. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1/2/3): ")

        if choice == "1":
            num1 = get_number("Enter first number: ")
            operator = input("Enter operator (+, -, *, /): ")
            num2 = get_number("Enter second number: ")

            result = calculate(num1, operator, num2)
            print("Result:", result)

        elif choice == "2":
            print("Calculator cleared.")

        elif choice == "3":
            print("Exiting calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
