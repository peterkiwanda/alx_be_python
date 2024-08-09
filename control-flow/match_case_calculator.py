# match_case_calculator.py

def main():
    try:
        # Prompt the user to enter two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Prompt the user to choose an operation
        operation = input("Choose the operation (+, -, *, /): ")

        # Perform the calculation using match case
        match operation:
            case '+':
                result = num1 + num2
            case '-':
                result = num1 - num2
            case '*':
                result = num1 * num2
            case '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    return
                result = num1 / num2
            case _:
                print("Error: Invalid operation. Please choose +, -, *, or /.")
                return

        # Output the result
        print(f"The result is {result}")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
