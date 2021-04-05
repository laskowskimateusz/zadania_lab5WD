class Point:
    counter = []

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def update(self, n=1):
        self.counter.append(n)


p1 = Point()
print(p1.counter)
p1.update()
print(p1.counter)

p2 = Point(4, 3)
print(p2.counter)
p2.update()
print(p2.counter)

Point.counter = []
print(p1.counter)
