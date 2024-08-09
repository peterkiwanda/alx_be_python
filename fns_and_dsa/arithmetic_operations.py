# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic operations based on the provided operation.

    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (str): The arithmetic operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
    float or str: The result of the arithmetic operation, or an error message if the operation is invalid
                  or if division by zero is attempted.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."

