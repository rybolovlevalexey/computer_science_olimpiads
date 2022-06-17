for num in range(1000, 10000):
    a, b, c, d = map(int, list(str(num)))
    s1 = a * b
    s2 = c * d
    res = ''.join(list(map(str, sorted([s1, s2])[::-1])))
    if res == "124":
        print(num)
        break