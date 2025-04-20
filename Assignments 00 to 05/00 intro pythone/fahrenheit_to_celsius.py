# Ask user to enter temperature in Fahrenheit
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert to Celsius
celsius = (fahrenheit - 32) * 5 / 9

# Display the result
print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
