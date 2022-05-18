file = open('27-48b (1).txt', 'r')
sp = file.read().strip().split('\n')
n = int(sp[0])
del sp[0]
chet = {1: 0, 0: 0}
summa = 0
i = 0
mndelta = None
flag = False
for elem in sp:
    a, b = map(int, elem.split())
    if (mndelta is None or abs(a - b) < mndelta) and a % 2 != b % 2:
        mndelta = abs(a - b)
print(mndelta)

for elem in sp:
    a, b = map(int, elem.split())
    if not flag and mndelta == abs(a - b):
        summa += min(a, b)
        if min(a, b) % 2 == 0:
            chet[0] += 1
        else:
            chet[1] += 1
        flag = True
    else:
        summa += max(a, b)
        if max(a, b) % 2 == 0:
            chet[0] += 1
        else:
            chet[1] += 1

print(summa, summa % 2)
print(chet)
print(mndelta)