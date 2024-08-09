# multiplication_table.py

def main():
    try:
        # Prompt the user to enter a number
        number = int(input("Enter a number to see its multiplication table: "))

        # Generate and print the multiplication table
        print(f"Multiplication table for {number}:")
        for i in range(1, 11):  # Loop from 1 to 10
            product = number * i
            print(f"{number} * {i} = {product}")

    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == "__main__":
    main()

