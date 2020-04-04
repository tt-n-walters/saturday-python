from operator import add, sub, mul, pow, truediv


operations = {
    "add": add,
    "subtract": sub,
    "multiply": mul,
    "divide": truediv,
    "to the power of": pow
}

def join_list(list):
    return " ".join(list)

processors = [ int, join_list, int ]

# Accepts the name of a mathematical operation, and finds the appropriate
# mathematical function.
def match_operation(operation):
    return operations[operation]


# Applies a mathematical function
def calculate(a, b, operation):
    return operation(a, b)


def parse_string(string):
    a, *operation, b = string.split(" ")
    return a, b, operation


# Applies a list of processors to a list of inputs
def process_string(*inputs):
    return [func(item) for item, func in zip(inputs, processors)]


def process_file(filename):
    with open(filename, "r") as file:
        lines = file.read().splitlines()

        results = []
        for calc in lines:
            a, b, operation = parse_string(calc)
            a, operation, b = process_string(a, operation, b)
            operation = match_operation(operation)
            results.append(calculate(a, b, operation))

        print(f"Total is: {sum(results)}")


if __name__ == "__main__":
    process_file("inputs_3.txt")
