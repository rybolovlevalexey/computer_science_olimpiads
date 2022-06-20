file = open('EGE-inf-26-file7(4).txt', 'r')
sp = file.read().strip().split('\n')
s, n = map(int, sp[0].split())
del sp[0]
sp = list(sorted(map(int, sp)))
summa = 0
cnt = 0
lastelem = 0
for elem in sp:
    if summa + elem <= s:
        summa += elem
        cnt += 1
        lastelem = elem
summa -= lastelem
print(cnt)
for elem in sp[::-1]:
    if elem + summa <= s:
        summa += elem
        print(elem)
        break
print(summa, s)