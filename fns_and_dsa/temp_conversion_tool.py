# Define conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def fahrenheit_to_celsius(fahrenheit_temp):
    return (fahrenheit_temp - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def celsius_to_fahrenheit(celsius_temp):
    return celsius_temp * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

# Example usage
temperature_fahrenheit = 77
temperature_celsius = fahrenheit_to_celsius(temperature_fahrenheit)
print(f"{temperature_fahrenheit}°F is equal to {temperature_celsius:.2f}°C")

temperature_celsius = 25
temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)
print(f"{temperature_celsius}°C is equal to {temperature_fahrenheit:.2f}°F")
