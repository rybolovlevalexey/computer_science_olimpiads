n, m = map(int, input().split())
num = 1
flag = True
for i in range(n):
    line = list()
    for j in range(m):
        if flag:
            line.append(num)
        else:
            line = [num] + line
        num += 1
    if flag:
        flag = False
    else:
        flag = True
    for elem in line:
        print(str(elem).ljust(3), end='')
    print()
