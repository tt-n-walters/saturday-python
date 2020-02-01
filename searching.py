
def main():
    with open("data_nums_1000000.txt", "r") as file:
        numbers = list(map(int, file.read().splitlines()))

    linear_result = linear_search(numbers, 6666666)
    print("Position found: {}".format(linear_result))
    print("Number at position {} was {}".format(linear_result, numbers[linear_result]))

    binary_result = binary_search(numbers, 6666666)
    print("Position found: {}".format(binary_result))
    print("Number at position {} was {}".format(binary_result, sorted(numbers)[binary_result]))



    def some_function(number):
        if numbers == 6666666:
            return "Yay well done"

    some_function(sorted(numbers)[binary_result])
    some_function(6666666)
    

def linear_search(data, needle):
    for index, num in enumerate(data):
        if num == needle:
            # Return the position of the item
            return index


def binary_search(data, needle, comparison=None):
    sorted_data = sorted(data, key=comparison)
    left_index = 0
    right_index = len(sorted_data)

    while True:
        middle_index = int((right_index - left_index) / 2 + left_index)
        # print("Looking at {} between {} and {}".format(middle_index, left_index, right_index))

        num = sorted_data[middle_index]
        # If using a non-standard comparison function
        if not comparison == None:
            num = comparison(num)
        if num > needle:
            right_index = middle_index
        elif num < needle:
            left_index = middle_index
        else:
            return middle_index


