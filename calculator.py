# calculator.py

def add(a, b):
    """Return the sum of two numbers."""
    result = a + b
    return result


def subtract(a, b):
    """Return the difference of two numbers."""
    result = a - b
    return result


def multiply(a, b):
    """Return the product of two numbers."""
    result = a * b
    return result


def divide(a, b):
    """Return the quotient of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    result = a / b
    return result


def power(a, b):
    """Return a raised to the power of b."""
    result = a ** b
    return result
