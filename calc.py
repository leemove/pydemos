def calc(*numbers):
  sum = 0
  for num in numbers:
    sum += num**2
  return sum

print(calc(1,2,3))
print(calc(*(1,2,3)))