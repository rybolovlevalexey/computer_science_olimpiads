file = open('28132.txt', 'r')
sp = file.read().strip().split('\n')
s, n = map(int, sp[0].split())
del sp[0]
sp = list(sorted(map(int, sp)))
summa = 0
cnt = 0
lastelem = -1
for elem in sp:
    if summa + elem <= s:
        summa += elem
        cnt += 1
        lastelem = elem
    else:
        #lastelem = elem
        break
print(cnt)

print(lastelem)
