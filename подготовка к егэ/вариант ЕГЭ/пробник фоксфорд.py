file = open('Zadanie-273949.txt', 'r')
sp = file.read().strip().split('\n')
s, n = map(int, sp[0].split())
del sp[0]
sp = sorted(list(filter(lambda x: x % 2 == 0, map(int, sp))))
summa = 0
cnt = 0
lstfl = 0
for i in range(len(sp)):
    if sp[i] + summa > s:
        break
    summa += sp[i]
    cnt += 1
    lstfl = sp[i]
print(s, summa, cnt, lstfl)
summa -= lstfl
for i in range(len(sp)):
    if sp[i] + summa <= s and sp[i + 1] + summa > s:
        print(sp[i], sp[i] + summa)
        break