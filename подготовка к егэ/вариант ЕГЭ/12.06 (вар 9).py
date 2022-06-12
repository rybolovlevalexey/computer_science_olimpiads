file = open('26 (7).txt', 'r')
sp = file.read().strip().split('\n')
s, n = map(int, sp[0].split())
del sp[0]
sp = list(sorted(map(int, sp)))
summa = 0
cnt = 0
lstelem = 0
for elem in sp:
    if summa + elem <= s:
        summa += elem
        cnt += 1
        lstelem = elem
    else:
        break
summa -= lstelem
for elem in sp[::-1]:
    if elem + summa <= s:
        print(elem)
        break