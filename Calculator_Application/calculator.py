
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
def arithmetic_mean(numbers):
    return statistics.mean(numbers)

def harmonic_mean(numbers):
    return statistics.harmonic_mean(numbers)

def calculator():
    # Define Calculator Values
    a = 2
    b = 7
    c = 20

    # Test Addition
    result = add(a, b)
    print(f"Addition: {result}") # {a} + {b}

    # Test Subtraction
    result = sub(a, b)
    print(f"Subtraction: {result}") # {a} - {b}

    # Test Multiplication
    result = mul(a, b)
    print(f"Multiplication: {result}") # {a} * {b}

    # Test Arithmetic Mean
    result = arithmetic_mean([a, b, c])
    print(f"Arithmetic Mean: {result}") # ({a} + {b} + {c}) / {len([a, b, c])}

    # Test Harmonic Mean
    result = harmonic_mean([a, b, c])
    print(f"Harmonic Mean: {result}") # {len([a, b, c])} / ({1/a} + {1/b} + {1/c})

calculator()
