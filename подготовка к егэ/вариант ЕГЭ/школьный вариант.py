file = open('zadanie_26.txt', 'r')
sp = file.read().strip().split('\n')
s, n = map(int, sp[0].split())
del sp[0]
sp = sorted(map(int, sp))
cnt = 0
summa = 0

for i in range(len(sp)):
    elem = sp[i]
    if summa + elem > s:
        break
    else:
        summa += elem
    cnt += 1
print(sp[i])
print(cnt, summa)

mxsm = summa - sp[i]
for j in range(i, len(sp)):
    if sp[j] + mxsm <= s and sp[j + 1] + mxsm > s:
        print(sp[j])
        break
print(mxsm + sp[j])
