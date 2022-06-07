file = open('26 (3).txt', 'r')
sp = file.read().strip().split('\n')
s, n = map(int, sp[0].split())  # грузоподъёмность, количество
del sp[0]
sp = list(sorted(map(int, sp)))
cnt = 0
summa = 0
lastelem = 0
for elem in sp:
    if elem + summa <= s:
        summa += elem
        cnt += 1
    if elem + summa > s:
        lastelem = elem
        break
summa -= lastelem
print(summa)
ans = 0
for i in range(len(sp) - 1):
    if summa + sp[i] <= s:
        ans = sp[i]
print(cnt, summa)
print(ans)
print(sp[-1])
print(summa + ans, s - summa - ans)