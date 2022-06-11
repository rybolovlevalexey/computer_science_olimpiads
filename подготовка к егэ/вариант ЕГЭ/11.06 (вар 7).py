file = open('27-B_2.txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
n = sp[0]
del sp[0]
mx = 0
i1 = 0
for i in range(len(sp)):
    if sp[i] % 14 != 0 and mx < sp[i]:
        mx = sp[i]
        i1 = i
m2 = 0
i2 = 0
for i in range(len(sp)):
    if sp[i] % 2 == 0 and m2 < sp[i] and i != i1:
        m2 = sp[i]
        i2 = i
m7 = 0
i3 = 0
for i in range(len(sp)):
    if sp[i] % 7 == 0 and m7 < sp[i] and i != i1 and i != i2:
        m7 = sp[i]
        i3 = i
m14 = 0
i4 = 0
for i in range(len(sp)):
    if sp[i] % 14 == 0 and m14 < sp[i] and i != i1 and i != i2 and i != i3:
        m14 = sp[i]
        i4 = i

print(i1, i2, i3, i4)
print(mx, m2, m7, m14)
ans = [mx * m14, m2 * m7, m2 * m14, m7 * m14]
print(max(ans))