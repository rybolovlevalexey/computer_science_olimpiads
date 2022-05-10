file = open('28140.txt', 'r')
sp = file.read().strip().split('\n')
s, n = map(int, sp[0].split())
del sp[0]
sp = sorted(list(map(int, sp)))
summa = 0
cnt = 0
indfl = 0

for i in range(n):
    if summa + sp[i] <= s:
        cnt += 1
        summa += sp[i]
        indfl = i
    else:
        break
print(cnt)
summa -= sp[indfl]
for i in range(n - 1):
    if sp[i] + summa <= s and sp[i + 1] + summa > s:
        print(sp[i])
