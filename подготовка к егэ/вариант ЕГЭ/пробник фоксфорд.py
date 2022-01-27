file = open('Zadanie-260283.txt', 'r')
st = file.readline().strip()
sp = list()
for i in range(len(st)):
    if st[i] == 'F':
        sp.append(i)
i1 = 0
i2 = sp[3]
ans = None
for i in range(len(sp) - 4):
    i1 = sp[i]
    i2 = sp[i + 4]
    lenght = i2 - i1 - 1
    if ans is None or lenght > ans:
        ans = lenght
print(ans)