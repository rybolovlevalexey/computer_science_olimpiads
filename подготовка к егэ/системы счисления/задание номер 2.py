def five(x):
    st = ''
    while x > 0:
        st += str(x % 5)
        x //= 5
    return st


num = 125**10 + 25**2
for x in range(1, 1000):
    res = five(num - x)
    if res.count('4') == 27:
        print(x)
        break
