# Conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

FREEZING_POINT_FAHRENHEIT = 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def celsius_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    :param fahrenheit: Temperature in Fahrenheit
    :return: Temperature in Celsius
    """
    return (fahrenheit - 32) * 5 / 9

def convert_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    :param celsius: Temperature in Celsius
    :return: Temperature in Fahrenheit
    """
    return celsius * 9 / 5 + 32

def main():
    """
    Main function to handle user interaction.
    """
    try:
        # Prompt user for input
        temp_input = input("Enter the temperature (e.g., 32F or 100C): ").strip()
        
        # Determine if the input is in Fahrenheit or Celsius
        if temp_input[-1].upper() == 'F':
            fahrenheit = float(temp_input[:-1])
            celsius = convert_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
        elif temp_input[-1].upper() == 'C':
            celsius = float(temp_input[:-1])
            fahrenheit = convert_to_fahrenheit(celsius)
            print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
        else:
            raise ValueError("Invalid temperature. Please enter a numeric value followed by 'C' or 'F'.")
    
    except ValueError as ve:
        print(ve)

if __name__ == "__main__":
    main()
