
class Polynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def __repr__(self):
        return "Polynomial({}x^2 + {}x + {})".format(self.a, self.b, self.c)
    

    def __add__(self, other):
        return Polynomial(self.a + other.a, self.b + other.b, self.c + other.c)
    

    def __len__(self):
        return 2 if self.a > 0 else 1 if self.b > 0 else 0
    

    def __getitem__(self, name):
        if name == 0:
            return self.c
        if name == 1:
            return self.b
        if name == 2:
            return self.a


poly1 = Polynomial(1, 5, 9) #    x^2 + 5x + 9
poly2 = Polynomial(2, 4, 0) #    2x^2 + 4x
print(poly1[2])
print(poly2[1])

poly3 = poly1 + poly2
print(poly3)

poly4 = Polynomial(0, 2, 3)
print(len(poly4))
