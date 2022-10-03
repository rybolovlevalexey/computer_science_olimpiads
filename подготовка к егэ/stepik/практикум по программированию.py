n = int(input())
sp = list()
for i in range(n):
    line = list()
    for j in range(n):
        if i == j or i == n - j - 1:
            line.append(1)
        else:
            line.append(0)
    sp.append(line)
for elem in sp:
    print(*elem, sep="  ")
