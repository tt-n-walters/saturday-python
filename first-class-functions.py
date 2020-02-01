
# def main():
#     print("Things are happening.")

# main

# if main == "a thing":
#     print("Yes!")
# else:
#     print("No")



def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def person_does_something(name, something):
    def func(text):
        return name + " does " + something(text)
    
    return func


nico_shouts = person_does_something("nico", shout)
nico_whispers = person_does_something("nico", whisper)

unai_shouts = person_does_something("unai", shout)

print(nico_shouts("I am teaching python"))
print(unai_shouts("And I'm learning!"))


print(nico_whispers("THIS TEXT IS VERY LOUD ISNT IT"))


nico_broke = person_does_something("nico", 42)
nico_broke("Does this work?")
