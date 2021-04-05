def ciag(a1, r):
    while True:
        yield a1
        a1 += r


gen = ciag(1, 5)
ile = 10
for _ in range(0, ile):
    print(next(gen))
