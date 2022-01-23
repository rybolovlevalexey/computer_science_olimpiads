def four(number):
    st = ''
    while number > 0:
        st += str(number % 4)
        number //= 4
    return st


num = 16**8 + 2**8
for x in range(1, 1000):
    res = four(num - x)
    if res.count('3') == 12:
        print(x)
        break
