file = open('27-B_2.txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
n = sp[0]
del sp[0]
m = 0
m14 = 0
m2 = 0
m7 = 0
for elem in sp:
    if m % 14 != 0 and elem > m:
        m = elem
    if elem % 2 == 0 and elem > m2:
        m2 = elem
    if elem % 7 == 0 and elem > m7:
        m7 = elem
    if elem % 14 == 0 and elem > m14:
        m14 = elem
print(m, m2, m7, m14)
ans = [m * m2, m * m7, m * m14, m2 * m7, m2 * m14, m7 * m14]
print(ans)
print(max(ans) % 14)
