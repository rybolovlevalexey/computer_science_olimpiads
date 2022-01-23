def seven(x):
    st = ''
    while x > 0:
        st += str(x % 7)
        x //= 7
    return st[::-1]


num = 343**8 + 49**2
for x in range(10000, 1, -1):
    res = seven(num - x)
    if res.count('0') == 21:
        print(x)
        break
