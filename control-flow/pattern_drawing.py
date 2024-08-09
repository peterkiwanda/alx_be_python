# pattern_drawing.py

def main():
    while True:
        try:
            # Prompt the user to enter a positive integer for the pattern size
            size = int(input("Enter the size of the pattern: "))
            if size <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")
    
    # Draw the pattern using nested loops
    row = 0
    while row < size:
        # Print each row of asterisks
        for col in range(size):
            print("*", end="")
        print()  # Move to the next line after printing a row
        row += 1

if __name__ == "__main__":
    main()

