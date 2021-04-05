class Kwadrat:
    def __init__(self, x):
        self.x = x
        self.ob = 4*x

    def __str__(self):
        return "Bok = {} Obwód = {}".format(self.x, self.ob)

    def __add__(self, other):
        return Kwadrat(self.x+other.ob)


test1 = Kwadrat(5)
print(test1)
test2 = Kwadrat(10)
print(test2)

test = test1+test2
print(test)
