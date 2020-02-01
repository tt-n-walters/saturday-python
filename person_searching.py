from collections import namedtuple
from pprint import pprint
from searching import binary_search

processors = [
    str,
    str,
    float,
    int,
    str
]

def process_data(processors, data):
    for processor, item in zip(processors, data):
        yield processor(item)



def main():
    with open("datasets/data_person_100000.csv", "r", encoding="utf-8") as file:
        people_strings = file.read().splitlines()

    Person = namedtuple("Person", people_strings[0])

    people = []
    for p in people_strings[1:20]:
        person_data = p.split(",")
        processed = process_data(processors, person_data)
        people.append(Person(*processed))
        
    def simple_comparison(person):
        return person
    
    def first_name_comparison(person):
        return person.first

    # result = binary_search(people, "Bob", first_name_comparison)
    # print(sorted(people, key=first_name_comparison)[result])


    def age_comparison(person):
        return person.age
    # result = binary_search(people, 88.8, age_comparison)
    # print(sorted(people, key=age_comparison)[result])

    age_sorted = sorted(people, key=age_comparison)
    first_sorted = sorted(people, key=first_name_comparison)
    
    # pprint(people)
    pprint(first_sorted)



main()
