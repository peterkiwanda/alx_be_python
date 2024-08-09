# Define the conversion factor
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def celsius_to_fahrenheit(celsius_temp):
    return celsius_temp * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

# Example usage
temperature_celsius = 25
temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)
print(f"{temperature_celsius}°C is equal to {temperature_fahrenheit}°F")
