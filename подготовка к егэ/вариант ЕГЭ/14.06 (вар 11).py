for num in range(1000, 10000):
    a, b, c, d = map(int, list(str(num)))
    s1 = a + b
    s2 = c + d
    ans = ''.join(map(str, sorted([s1, s2])))
    if ans == '117':
        print(num)