file = open('Zadanie-260361.txt', 'r')
sp = file.read().strip().split('\n')
s, n = map(int, sp[0].split())
del sp[0]
sp = list(sorted(map(int, sp)))
sp = list(filter(lambda x: x % 3 == 0, sp))
sp = sp[10:]
s1 = 0
i = 0
m = 0
while True:
    if s1 + sp[i] + sp[i + 1] > s:
        break
    s1 += sp[i]
    i += 1
    m += 1
print(len(sp), i)
for j in range(i, len(sp)):
    if s1 + sp[j] > s:
        print(sp[j - 1])
        break
print(s1, m)