# Converts temperature between Fahrenheit to Celsius.

# To create a python converter for celsius and fahrenheit, you first have to find out which formula to use.


# Fahrenheit to Celsius formula:
# (°F - 32) x 5/9 = °C or in plain english, First subtract 32, then multiply by 5, then divide by 9.


# Celsius to Fahrenheit formula:
# (°C × 9/5) + 32 = °F or in plain English, Multiple by 9, then divide by 5, then add 32.



# Convert Fahrenheit to Celsius

#!/usr/bin/env python
Fahrenheit = int(input("Enter a temperature in Fahrenheit: "))

Celsius = (Fahrenheit - 32) * 5.0//9.0

print("Temperature:", Fahrenheit, "Fahrenheit = ", Celsius, " C")



# Convert Celsius to Fahrenheit

#!/usr/bin/env python
Celsius = int(input("Enter a temperature in Celsius: "))

Fahrenheit = 9.0//5.0 * Celsius + 32

print("Temperature:", Celsius, "Celsius = ", Fahrenheit, " F")
