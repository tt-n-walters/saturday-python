
def add(amount):
    def func(value):
        return value + amount
    
    return func



adds_5 = add(5)
adds_10 = add(10)
adds_1000 = add(1000)

print(adds_5(60))
print(adds_5(15))
print(adds_5(995))

print(adds_1000(60))
print(adds_1000(15))
print(adds_1000(995))