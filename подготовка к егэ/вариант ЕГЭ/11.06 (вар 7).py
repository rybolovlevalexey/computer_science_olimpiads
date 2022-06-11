def convert(x, s):
    r = ''
    while x > 0:
        r += str(x % s)
        if s == 11:
            print(x % s)
        if s == 13:
            print(x % s)
        if s == 19:
            print(x % s)
        x //= s
    if s in [11, 13, 19]:
        print('----------')
    return r[::-1]


for n in range(2, 20):
    res = convert(144, n)
    if res[-1] == '1' and len(res) >= 3:
        print(n, 'answer')
