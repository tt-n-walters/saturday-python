from random import randint

# data = []
# for i in range(100000):
#     data.append(randint(0, 100))

data = [randint(0, 100) for _ in range(30)]
# data = [1, 2, 3, 4, 5]

def bubble(data):
    num_of_operations = 0
    num_of_swaps = 0
    for i in range(len(data)):
        previous_swaps = num_of_swaps
        for j in range(len(data) - i - 1):
            num_of_operations += 1
            first = data[j]
            second = data[j + 1]
            # print("Comparing {} and {}".format(first, second))

            if first > second:
                num_of_swaps += 1
                # print("Swapping {} and {}".format(first, second))
                data[j] = second
                data[j + 1] = first
        
        if previous_swaps == num_of_swaps:
            break
    
    print("Looped: {} times".format(num_of_operations))
    print("Swapped: {} times".format(num_of_swaps))


# An algorithm is a repeatable series of steps.



def shuffle_sort(data):
    while not sorted(data) == data:
        data.shuffle()
    return data





def miracle_sort(data):
    while not sorted(data) == data:
        time.sleep(10)
    return data



# The __name__ of a python file is only ever "__main__" when the file is run
# directly.
# Otherwise it's filled with all other kind of nonsense

if __name__ == "__main__":
    print("Running bubble sort.")
    bubble()
