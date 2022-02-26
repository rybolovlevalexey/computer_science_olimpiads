i = 10000000
while True:
    n = i
    s1 = sum(list(filter(lambda x: x % 2 == 1, map(int, list(str(n))))))
    s2 = sum([int(str(n)[i]) for i in range(len(str(n))) if i % 2 == 1])
    r1 = abs(s1 - s2)
    if r1 == 29:
        print(i)
        break
    i += 1
    if i % 100000 == 0:
        print(i)
