#PRINTING IN PYTHON_____________________________________
# sep = separator
# end = lf / crlf or any other symbol do you want

print(12, 34, 2021, sep="/", end="\n[")
print(56, 78, sep="***", end="]\n")

# STRINGS IN PYTHON____________________________________

# Single quotes
single_quote = 'This is a string using single quotes.'

# Double quotes
double_quote = "This is a string using double quotes."

print(single_quote)
print(double_quote)

# Creating a string
my_string = "Hello, World!"

# Accessing characters in a string
print(my_string[0])  # Output: H

# Slicing a string
print(my_string[7:12])  # Output: World

# Concatenating strings
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name + "!"  # Output: Hello, Alice!

# String methods
print(my_string.lower())  # Output: hello, world!
print(my_string.upper())  # Output: HELLO, WORLD!
print(my_string.replace("Hello", "Hi"))  # Output: Hi, World!

# INT AND FLOAT IN PYTHON____________________________________
# Integer
my_int = 10

# Float
my_float = 3.14

print(my_int)  # Output: 10
print(my_float)  # Output: 3.14

# BOOLEAN IN PYTHON____________________________________
# Boolean
my_bool = True

print(my_bool)  # Output: True

# Comparisons
x = 5
y = 10

print(x < y)  # Output: True
print(x > y)  # Output: False
print(x == y)  # Output: False

# Logical operators
a = True
b = False

print(a and b)  # Output: False
print(a or b)  # Output: True
print(not a)  # Output: False

# COERCION IN PYTHON____________________________________
# Coercion is the process of converting one data type to another.
# Python provides several built-in functions for performing type coercion.

# Example 1: Coercing a float to an integer
my_float = 3.14
my_int = int(my_float)
print(my_int)  # Output: 3

# Example 2: Coercing an integer to a float
my_int = 10
my_float = float(my_int)
print(my_float)  # Output: 10.0

# Example 3: Coercing a string to an integer
my_string = "123"
my_int = int(my_string)
print(my_int)  # Output: 123

# Example 4: Coercing a string to a float
my_string = "3.14"
my_float = float(my_string)
print(my_float)  # Output: 3.14

# Example 5: Coercing a boolean to an integer
my_bool = True
my_int = int(my_bool)
print(my_int)  # Output: 1

# Example 6: Coercing an integer to a boolean
my_int = 0
my_bool = bool(my_int)
print(my_bool)  # Output: False