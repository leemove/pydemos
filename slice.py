L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# print(L[2:])

L = list(range(10))
# print(L[:-1])

def forin(l):
  for item in l:
    print(item)
# forin(L)
L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = [word.lower() for word in L1 if isinstance(word, str)]
print(L2)