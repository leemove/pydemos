from functools import reduce

l = ['adam', 'LISA', 'barT']

def fn(name):
  return name.capitalize()

nl = list(map(fn, l))

# print(nl)


#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
l = [1,2,3,4]

def ji(res, num):
  return res * num

def prod(L):
  return reduce(ji, L)

print(prod(l))