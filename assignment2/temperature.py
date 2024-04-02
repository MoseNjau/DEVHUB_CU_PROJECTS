def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Test the functions
celsius_value = 30
print("{} Celsius in Fahrenheit is {}".format(celsius_value, celsius_to_fahrenheit(celsius_value)))

fahrenheit_value = 98
print("{} Fahrenheit in Celsius is {}".format(fahrenheit_value, fahrenheit_to_celsius(fahrenheit_value)))
