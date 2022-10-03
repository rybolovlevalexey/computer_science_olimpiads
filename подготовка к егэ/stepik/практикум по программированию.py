n = int(input())
sp = list()
for i in range(n):
    line = list()
    flag = False
    for j in range(n):
        if i < n // 2:
            if i == j:
                flag = True
                line.append(1)
            elif i == n - j - 1:
                flag = False
                line.append(1)
            else:
                if flag:
                    line.append(1)
                else:
                    line.append(0)
        else:
            if i == j:
                flag = False
                line.append(1)
            elif i == n - j - 1:
                flag = True
                line.append(1)
            else:
                if flag:
                    line.append(1)
                else:
                    line.append(0)
    sp.append(line)
for elem in sp:
    print(*elem, sep="  ")
