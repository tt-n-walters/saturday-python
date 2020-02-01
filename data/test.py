from sys import getsizeof

# Generators provide data one item at a time

def naive_function():
    pies = []

    for _ in range(100000000):
        pies.append("3.141592")
    
    return pies


def lazy_function():
    for _ in range(100000000):
        yield "3.141592"


pies = lazy_function()
converted = map(float, pies)

print("Size: {}".format(getsizeof(converted)))
print("Sum: {}".format(sum(converted)))
