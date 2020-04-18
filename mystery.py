
# for n in [3, 1, 4, 1, 5, 9, 2]:
#     print(n)

# for c in "Python is great.":
#     print(c)

# for k in { "name": "Bob", "job": "Builder", "age": 42 }:
#     print(k)

# # for l in open("datasets/sentences.txt", "r"):
# #     print(l)

# for x in range(100):
#     print(x)



my_list = ["apple", "banana", "cherry", "durian", "egg", "food"]

# print("Counting while")
# i = 0
# while i < len(my_list):
#     print(my_list[i])
#     i += 1

# print("Valuing while")
# item = my_list[0]
# while my_list.index(item) < len(my_list) - 1:
#     print(item)
#     item = my_list[my_list.index(item) + 1]


# print("Counting for")
# for i in range(len(my_list)):
#     print(my_list[i])

# print("Valuing for")
# for item in my_list:
#     print(item)



my_iterator = iter(something)
while True:
    try:
        print(next(my_iterator))
    except StopIteration:
        break
