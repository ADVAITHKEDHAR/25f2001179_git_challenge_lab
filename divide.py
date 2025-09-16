# divide.py
def divide(a, b):
    """Return a / b or explain division by zero."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: division by zero"
