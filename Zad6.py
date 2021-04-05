class Wspak:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


test = Wspak("Data")
print(test)
for _ in test.data:
    print(next(test))
test2 = Wspak("Fotel")
print(test2)
for _ in test2.data:
    print(next(test2))
