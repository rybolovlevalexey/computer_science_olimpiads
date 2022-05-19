cnt = 0
file = open('zadanie_26.txt', 'r')
sp = file.read().strip().split('\n')
n, m = map(int, sp[0].split())
del sp[0]
sp = list(sorted(map(int, sp)))
summa = 0
for elem in sp:
    if 310 <= elem <= 320:
        summa += elem
        cnt += 1
lstind = 0

for i in range(len(sp)):
    elem = sp[i]
    if not 310 <= elem <= 320 and summa + elem <= m:
        summa += elem
        cnt += 1
        lstind = i
print(summa, lstind, m, sp[lstind])
summa -= sp[lstind]
for elem in sp[::-1]:
    if elem + summa <= m:
        summa += elem
        print(elem)
        break
print(cnt, summa)