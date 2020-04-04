
from time import perf_counter


def timer_decorator(func):                          # Define out decorator
    
    def wrapper(*args):                             # Define the higher-order wrapper function
        start_time = perf_counter()                 # It accepts *args, meaning any amount of arguments
        output = func(*args)                        # Run the first-class function, save the returned value to a variable
        end_time = perf_counter()
        # print(f"Function took {end_time - start_time}s")
        difference = end_time - start_time
        return output, difference
    
    return wrapper
