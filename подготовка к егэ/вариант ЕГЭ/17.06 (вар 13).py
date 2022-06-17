for num in range(100, 1000):
    a, b, c = map(int, list(str(num)))
    s1 = a + b
    s2 = b + c
    res = ''.join(list(map(str, sorted([s1, s2])[::-1])))
    if res == '1412':
        print(num)
        break