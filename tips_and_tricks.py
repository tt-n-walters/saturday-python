
#__#        Tip & Trick  no 1               Parallel Iteration
# We want to iterate over more than one list at a time

x_coords = [45, 92, 20, 71, 53]
y_coords = [24, 21, 68, 47, 19]
z_coords = [67, 43, 19, 32, 10]


# for i in range(len(x_coords)):
#     print(x_coords[i], y_coords[i])


# for i in range(len(x_coords)):
#     x = x_coords[i]
#     y = y_coords[i]
#     print(x, y)



for x, y, z in zip(x_coords, y_coords, z_coords):
    print(x, y, z)





# Desired output:
"""
45 24
92 21
20 68
71 47
53 19

"""




# Example 2

monthly_profit = [52300, 48800, 57100, 41100, 62800]
monthly_costs = [48900, 46000, 54900, 45200, 59600]


for profit, cost in zip(monthly_profit, monthly_costs):
    print(f"Net profit: {profit - cost}")







# Desired output:
"""
Net profit: 3400
Net profit: 2800
Net profit: 2200
Net profit: -4100
Net profit: 3200

"""



#_#


#__#        Tip & Trick  no 2               
# We want to loop through some data, and have access to the items and indexes at the same time

column_names = ["First name", "Last name", "Date of birth", "Address", "Gender"]



# for i in range(len(column_names)):
#     item = column_names[i]
#     print(....)

# i = 0
# for column in column_names:
#     print(f"Column {i + 1} is '{column}'")
#     i += 1


for i, column in enumerate(column_names):
    print(f"Column {i + 1} is '{column}'")



enumerated_data = enumerate(column_names)
column_names
list(enumerated_data)



# Desired output:
"""
Column 1 is 'First name'
Column 2 is 'Last name'
Column 3 is 'Date of birth'
Column 4 is 'Address'
Column 5 is 'Gender'

"""

#_#


#__#        Tip & Trick  no 3               In-place variable swap
# We want to swap two variables

a, b = "python is amazing", 3.141592



# tmp = a
# a = b
# b = tmp

a, b = b, a


print(f"a = {a}")
print(f"b = {b}")





# Desired output:
"""
a = 3.141592
b = python is amazing

"""




#_#


#__#        Tip & Trick  no 4 & 5  
# We want to inspect an object, module, class, etc...

import random
from pprint import pprint


print(dir(dict))
# for a, b in zip(dir(random)[::2], dir(random)[1::2]):
#     print(f"{a}\t\t\t\t{b}")


















#_#


#__#        Tip & Trick  no 6                           Python standard datastructures
# We want to categorise a sentance of words

from pprint import pprint
from collections import defaultdict

sentence = "A cranky old lady shoots lemons with her high-powered machinegun while wearing crocks."

words = sorted(map(lambda word: word.strip("."), sentence.split(" ")))
results = defaultdict([])

for word in words:
    first = word[0].lower()
    results[first].append(word)

pprint(results)





# Desired output: dictionary of lists
"""
{
    "a": ["A"],
    "c": ["cranky", "crocks"],
    "h": ["high-powered"],
    "l": ["lady", "lemons"],
    etc...
}

"""







# We want to count the occurences of each letter in a sentence.
from collections import defaultdict
from pprint import pprint
sentence = "A cranky old lady shoots lemons with her high-powered machinegun while wearing crocks."


results = defaultdict(int)
filtered_chars = " -."

for letter in sentence:
    print(letter)
    if not letter in filtered_chars:
        results[letter] += 1


pprint(results)








# Desired output: dictionary with counts of words
"""
{
    "a": 4,
    "c": 4,
    "d": 3,
    "e": 7,
    "g": 3,
    etc...
}

"""




















#_#


#__#        Tip & Trick  no 7               List Initialisation
# We want to initialise a list with a number of starting values













# Desired output:
"""
a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

"""




#_#


#__#        Tip & Trick  no 8   
# We want to access items in a dictionary, but there is a chance the items don't exist in the dictionary

hair_colours = {
    "arthur": "ginger",
    "bill": "ginger",
    "charlie": "ginger",
    "dobby": "bald",
    "errol": "feathers",
    "fred": "ginger",
    "george": "ginger",
    "harry": "black"
}

print(hair_colours["fred"])
print(hair_colours.get("ron", None))












#_#


#__#        Tip & Trick  no 9   
# Making comparisons more concise


# Check if a value is within a range, example greater than 4 and less than 18
age = 15















# Check if a value is equal to discrete set of values

















#_#


#__#        Tip & Trick  no 10      
# We want to check if a series of conditions are NOT true


# Example, find the prime numbers between 2 and 30













# Desired output
"""
2 is a prime number.
3 is a prime number.
5 is a prime number.
7 is a prime number.
11 is a prime number.
13 is a prime number.
17 is a prime number.
19 is a prime number.
23 is a prime number.
29 is a prime number.

"""








#_#