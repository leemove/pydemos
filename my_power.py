def my_power(num, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * num
    return s
print(my_power(10))