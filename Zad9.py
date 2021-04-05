def parzyste(data):
    for index in range(0, len(data), 2):
        yield data[index]


gen = parzyste("Feliks")
print(next(gen))
print("Marek")
print(next(gen))
