file = open('26 (10)(2).txt', 'r')
sp = file.read().strip().split('\n')
n, m = map(int, sp[0].split())
del sp[0]
sp = sorted(list(map(int, sp)))
summa = 0
cnt = 0
mxelem = 0
for elem in sp[::-1]:
    if 200 <= elem <= 220:
        summa += elem
        cnt += 1
        if elem > mxelem:
            mxelem = elem
for elem in sp:
    if elem + summa <= m and not 200 <= elem <= 220:
        cnt += 1
        summa += elem
        if elem > mxelem:
            mxelem = elem
summa -= mxelem
for elem in sp[::-1]:
    if summa + elem <= m:
        print(elem)
        print(summa, m)
        break