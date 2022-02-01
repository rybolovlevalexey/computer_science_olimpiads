file = open('Zadanie-260370B.txt', 'r')
sp = file.read().strip().split('\n')
dlina = int(sp[0])
del sp[0]
s = 0
cnt = 0
for i in range(dlina):
    i1, i2, i3 = map(int, sp[i].split())
    i1, i2, i3 = min(i1, i2, i3), sum([i1, i2, i3]) - max(i1, i2, i3) - min(i1, i2, i3), max(i1, i2, i3)
    if i3 - i2 == 1 and cnt < 2:
        cnt += 1
        s += i2
    else:
        s += i3
print(s)