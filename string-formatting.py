from datetime import datetime
from random import randint


name = "Nico"
age = randint(18, 30)
birthday = 27
birthmonth = 4


# Expected output:
#  My name is Nico, I am XX years old, and I was born on the XX/XX/XX

birthyear = (datetime.now().year - age) % 100
print("My name is " + name + ", and I am " + str(age) + " years old, and I was born on the " + str(birthday) + "/" + str(birthmonth) + "/" + str(birthyear))

print("My name is %s, and I am %d years old, and I was born on the %02d/%02d/%02d" % (name, age, birthday, birthmonth, birthyear))

print("My name is {}, and I am {} years old, and I was born on the {:02}/{:02}/{:02}".format(name, age, birthday, birthmonth, birthyear))

print(f"My name is {name}, and I am {age} years old, and I was born on the {birthday:02}/{birthmonth:02}/{birthyear:02}")