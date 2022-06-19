file = open('28138.txt', 'r')
sp = file.read().strip().split('\n')
s, n = map(int, sp[0].split())
del sp[0]
sp = list(sorted(map(int, sp)))
summa = 0
cnt = 0
lastelem = 0
for elem in sp:
    if elem + summa <= s:
        summa += elem
        lastelem = elem
        cnt += 1
summa -= lastelem
for elem in sp[::-1]:
    if summa + elem <= s:
        print(elem)
        break
print(summa + elem, s)
