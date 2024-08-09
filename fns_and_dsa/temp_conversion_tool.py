# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_OFFSET = 32

def convert_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius using the global conversion factor.
    
    Parameters:
    fahrenheit (float): The temperature in Fahrenheit.
    
    Returns:
    float: The temperature converted to Celsius.
    """
    # Convert to Celsius
    return (fahrenheit - FAHRENHEIT_TO_CELSIUS_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit using the global conversion factor.
    
    Parameters:
    celsius (float): The temperature in Celsius.
    
    Returns:
    float: The temperature converted to Fahrenheit.
    """
    # Convert to Fahrenheit
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_TO_CELSIUS_OFFSET

def main():
    try:
        # Get user input
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == 'C':
            
