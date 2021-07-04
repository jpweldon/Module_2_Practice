
# Calculator App (Monolithic Version)

# Import Functions
from calculations.add import add # from calculations folder add module import add function
from calculations.sub import sub # from calculations folder sub module import sub function
from calculations.mul import mul # from calculations folder mul module import mul function
from calculations.mean.arithmetic import arithmetic_mean # from calculations folder mean subfolder arithmetic module import arithmetic_mean function
from calculations.mean.harmonic import harmonic_mean # from calculations folder mean subfolder harmonic module import harmonic_mean function

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
