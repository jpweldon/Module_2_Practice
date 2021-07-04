
# Calculator App (Monolithic Version)

import statistics # Importing the statistics package

# Define an Addition Function
def add(num1, num2):
    return num1 + num2

# Define a Subtraction Function
def sub(num1, num2):
    return num1 - num2

# Define a Multiplication Function
def mul(num1, num2):
    return num1 * num2

# Define a Mean Function
def mean(numbers):
    return statistics.mean(numbers)

def calculator():
    # Define Calculator Values
    a = 2
    b = 7
    c = 20

    # Test Addition
    result = add(a, b)
    print(f"Addition: {a} + {b} = {result}")

    # Test Subtraction
    result = sub(a, b)
    print(f"Subtraction: {a} - {b} = {result}")

    # Test Multiplication
    result = mul(a, b)
    print(f"Multiplication: {a} * {b} = {result}")

    # Test Mean
    result = mean([a, b, c])
    print(f"Mean: ({a} + {b} + {c}) / {len([a, b, c])} = {result: .3f}")

calculator()
