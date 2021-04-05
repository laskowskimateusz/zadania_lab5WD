class Parzyste:
    def __init__(self, data):
        self.data = data
        self.index = -2

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration
        self.index = self.index + 2
        return self.data[self.index]


test = Parzyste("Data")
print(test)
for _ in range(0, len(test.data), 2):
    print(next(test))
test2 = Parzyste("Fotel")
print(test2)
for _ in range(0, len(test2.data), 2):
    print(next(test2))
