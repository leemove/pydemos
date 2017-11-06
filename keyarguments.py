def person(name, age, **other):
    print('name:', name, 'age:', age, 'other:', other)

person('Tom', 12, job='catch muouse')

def cat(name, age, *, color):
    print(name,age,color)
cat('Tom', 12, color = 'dark')