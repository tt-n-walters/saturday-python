
class PowersOf:
    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        self.base = 0
        return self
    
    def __next__(self):
        if self.base == 100:
            raise StopIteration
        self.base += 1
        return self.base ** self.n



squares = PowersOf(2)
cubes = PowersOf(3)
a = PowersOf(71)

for n in a:
    print(n)


# print("\n".join(map(str, [n ** 71 for n in range(100)])))

# The lovely explanation

# def join(list, seperator):
#     output_string = ""
#     for item in list:
#         output_string += item + seperator
#     return output_string

# ns = []
# for n in range(100):
#     ns.append(n ** 71)

# ns_string = map(str, ns)

# ns_string = []
# for n in ns:
#     ns_string.append(str(n))

# # ns = [n ** 71 for n in range(100)]
