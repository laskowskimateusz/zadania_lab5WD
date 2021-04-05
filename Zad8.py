class Samogloski:
    samogloski = 'aąeęiouy'

    def __init__(self, data):
        if isinstance(data, str):
            print("True")
        self.data = data
        self.index = -1
        self.lista = [i for j in range(0, len(self.data)) for i in self.samogloski if i == self.data[j]]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration
        self.index += 1
        return self.lista[self.index]


test = Samogloski("Data")
print(test)
for _ in range(0, len(test.lista)):
    print(next(test))

test2 = Samogloski("Fotel")
print(test2)
for _ in range(0, len(test2.lista)):
    print(next(test2))

test3 = Samogloski("Samogloski")
print(test3)
for _ in range(0, len(test3.lista)):
    print(next(test3))
