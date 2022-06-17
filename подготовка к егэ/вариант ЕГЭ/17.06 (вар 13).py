file = open('28141.txt', 'r')
sp = file.read().strip().split('\n')
s, n = map(int, sp[0].split())
del sp[0]
sp = sorted(map(int, sp))
summa = 0
cnt = 0
lastelem = 0
for elem in sp:
    if summa + elem <= s:
        summa += elem
        lastelem = elem
        cnt += 1
summa -= lastelem
for elem in sp[::-1]:
    if elem + summa <= s:
        print(elem)
        break
