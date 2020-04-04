
# Decorator that checks arguments are natural numbers before proceeding.

def requires_natural(func):
    def wrapper(*args):
        for n in args:
            if not type(n) == int and n < 0):
                raise AttributeError(f"{n} is not a natural number.")    
        func(*args)
    
    return wrapper
