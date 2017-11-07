def gn ():
  n = 0
  while n < 999:
    n = n + 1
    yield n

# g = gn()
# print(next(g))
# print(next(g))
# print(next(g))

def triangles ():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]

# g = triangles()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))