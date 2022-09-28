n = int(input())
if n == 1:
    print(input())
else:
    sp = list()
    for i in range(n):
        line = input().split()
        sp.append(line)
    for i in range(n // 2):
        up = sp[i][:]
        down = sp[n - i - 1][:]
        left = list()
        rigth = list()
        for j in range(i, n - i):
            left.append(sp[j][i])
            rigth.append(sp[j][n - i - 1])
        for j in range(len(left)):
            sp[i][j + i] = left[len(left) - j - 1]
            sp[n - i - 1][j + i] = rigth[len(rigth) - j - 1]
        if i + 1 == n // 2 and n % 2 == 0:
            break
        for j in range(1, len(up) - 1):
            sp[i + j][n - i - 1] = up[j]
        for j in range(1, len(down) - 1):
            sp[n - j - 1][i] = down[len(down) - j - 1]
    for elem in sp:
        print(*elem, sep=' ')