
def a():
    yield 1
    yield 2
    return 3
    yield 4
    yield 5
k = a()
k2 = a()
print(next(k))
print(next(k))
print(next(k))



