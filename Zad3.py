class Kwadrat:
    def __init__(self, x):
        self.x = x

    def __ge__(self, other):
        return self.x >= other.x

    def __gt__(self, other):
        return self.x > other.x

    def __le__(self, other):
        return self.x <= other.x

    def __lt__(self, other):
        return self.x < other.x


kwadrat1 = Kwadrat(5)
kwadrat2 = Kwadrat(8)
kwadrat3 = Kwadrat(3)
kwadrat4 = Kwadrat(9)

print(kwadrat1 > kwadrat4)
print(kwadrat2 >= kwadrat4)
print(kwadrat4 < kwadrat3)
print(kwadrat2 <= kwadrat4)
