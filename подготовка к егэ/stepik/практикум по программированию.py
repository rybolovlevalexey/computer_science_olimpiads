n, m = map(int, input().split())
num = 1
sp = list()
for i in range(n):
    line = list("*" for j in range(m))
    sp.append(line)
for j in range(m):
    for i in range(n):
        sp[i][j] = num
        num += 1
for elem in sp:
    for el in elem:
        print(str(el) + " " * (3 - len(str(el))), end="")
    print()