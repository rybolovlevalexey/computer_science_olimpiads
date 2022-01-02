file = open('Zimnii_EGE_27_B.txt', 'r')
sp = file.read().strip().split('\n')
del sp[0]
s1 = 0
min_delta = -1
cnt = 0
for elem in sp:
    j1, j2 = map(int, elem.split())
    s1 += max(j1, j2)
    if (min_delta == -1 or abs(j1 - j2) < min_delta) and abs(j1 - j2) != 0:
        min_delta = abs(j1 - j2)
    if abs(j1 - j2) == min_delta:
        cnt += 1
s2 = 0
flag = True
for elem in sp:
    j1, j2 = map(int, elem.split())
    if abs(j1 - j2) != min_delta or not flag:
        s2 += max(j1, j2)
    else:
        flag = False
        s2 += min(j1, j2)
print(s2)