def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Test the function
input_string = "hello"
print("Reverse of '{}' is '{}'".format(input_string, reverse_string(input_string)))


