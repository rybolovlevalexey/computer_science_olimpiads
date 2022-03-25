for elem in range(0, 10000):
    x = elem
    r = 0
    while x > 0:
        d = x % 10
        r = 10 * r + d
        x = x // 10
    if len(str(r)) == 2 and int(str(r)[0]) + int(str(r)[1]) == 16:
        print(elem)
