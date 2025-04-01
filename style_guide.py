# Naming Conventions
# rigth(using _ to seperate words)
def calculate_area(radius):
    return 3.14 * radius ** 2

# worng
def CalculateArea(Radius):
    return 3.14 * Radius ** 2

# right(use caps letters for class names)
class Car:
    pass

# wrong
class car:
    pass

# right(use UPPER_CASE for constants)
MAX_CONNECTIONS = 100

# worng
maxConnections = 100

# Imports
# right
import os
import sys

# wrong
import os, sys

# right
import os
import sys

import numpy as np

from mymodule import my_function

# worng
import numpy as np
import os
import mymodule
import sys

# Strings

# right(use f-strings)
name = "Alice"
print(f"Hello, {name}!")

# wrong
name = "Alice"
print("Hello, " + name + "!")  # Less readable

# right(use sonsistent quotes)
message = "Hello, world!"
another_message = 'Python is great!'

# wrong
message = "Hello, world!'
another_message = "Python is great!"

# Comments & Docstings
# right
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

# wrong
def add(a, b):
    # This function adds two numbers
    return a + b

# Function Definicions
# right
def multiply(x: int, y: int) -> int:
    return x * y

# wrong
def multiply(x, y):
    return x * y

# right(keep functyion focused)
def get_user_age():
    """Prompt user for age and return it."""
    age = int(input("Enter your age: "))
    return age

# wrong
def get_user_info():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    print(f"Hello {name}, you are {age} years old.")
    return name, age

# Boolean Evalution
# right(use implicit boolean evalution)
if my_list:
    print("List is not empty")

# wrong
if len(my_list) > 0:
    print("List is not empty")

# right(use is not None)
if value is not None:
    print("Value exists")

# wrong
if value != None:
    print("Value exists")

#Exception Handeling
# rigth(use specific exceptions)
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")

# wrong
try:
    result = 10 / 0
except:
    print("An error occurred")  # This can hide unexpected errors

# List Comprehensions
# right
squares = [x**2 for x in range(10) if x % 2 == 0]

# wrong
squares = []
for x in range(10):
    if x % 2 == 0:
        squares.append(x**2)

# File Handeling
# right
with open("file.txt", "r") as f:
    content = f.read()

# wrong
f = open("file.txt", "r")
content = f.read()
f.close()  # Manually closing is risky if an error occurs before this