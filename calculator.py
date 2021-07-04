
# Calculator App

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

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

calculator()
