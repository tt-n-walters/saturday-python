from collections import namedtuple


def main():
    with open("data_person_100000.csv", "r", encoding="utf-8") as file:
        people_strings = file.read().splitlines()

    Person = namedtuple("Person", people_strings[0])

    people = []
    for p in people_strings[1:]:
        person_data = p.split(",")
        people.append(Person(*person_data))

    print(people[0:5])


def weird_function(function_to_run):
    function_to_run()


weird_function(main)
