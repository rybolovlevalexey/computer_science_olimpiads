file = open('27986_B.txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
m = 0
m7 = 0
for elem in sp:
    if elem % 7 == 0 and elem > m7:
        m7 = elem
    if elem % 7 != 0 and elem > m:
        m = elem
print(m * m7)