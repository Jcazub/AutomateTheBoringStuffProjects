import sys

def spam(divideby):
    try:
        return 42 / divideby
    except ZeroDivisionError:
        print("Division by Zero")
        sys.exit('User divided by zero')


spam(42)
spam(100)
spam(0)
spam(84)