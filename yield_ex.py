def gen(n):
    for i in range(n):
        yield i


g = gen(3)
print(g.__next__())
print(g.__next__())
print(g.__next__())

h = "Hello"
ier = iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())
