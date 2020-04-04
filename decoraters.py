
def how_are_you_decorator(func):
    def wrapper():
        func()
        print("How are you?")
    
    return wrapper


def say_hello():
    print("Hello!")

from random import random
random = how_are_you_decorator(random)
print(random())

# say_hello = how_are_you_decorator(say_hello)
# say_hello()


from time import perf_counter


def timer_decorator(func):                          # Define out decorator
    print("Running timer_decorator with ")
    input(func)
    def wrapper(*args):                             # Define the higher-order wrapper function
        input("Running wrapper")
        start_time = perf_counter()                 # It accepts *args, meaning anfunc amount of arguments
        input("Measuring start time")
        print(func)
        output = func(*args)                        # Run the first-class function, save the returned value to a variable
        print("Run original function")
        input(func)
        end_time = perf_counter()
        input("Measured endtime")
        print(f"Function took {end_time - start_time}s")
        input(f"Returning output {output}")
        return output
    print(wrapper)
    input("Returning wrapper")
    return wrapper


from random import random
# random = timer_decorator(random)

@timer_decorator                # Pie syntax
def quick_function():
    input("Running quick function")
    random()
    input("Finished running random")


# @timer_decorator
# def slow_function(n):
#     for _ in range(n):
#         random()
#     return random()

input("Running quick function once decorated")
print(quick_function)
quick_function()
# final = slow_function(10000000)
# print(final)