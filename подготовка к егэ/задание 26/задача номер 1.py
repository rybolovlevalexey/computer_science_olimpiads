file = open('26.txt', 'r')
sp = file.read().strip().split('\n')
n, m = map(int, sp[0].split(' '))
del sp[0]
sp = list(map(int, sp))
sp.sort()
massa = 0
count = 0
for i in range(len(sp) - 1, 0, -1):
    elem = sp[i]
    if massa > m:
        break
    if 200 <= elem <= 220:
        massa += elem
        count += 1
for i in range(len(sp)):
    elem = sp[i]
    if 200 <= elem <= 220:
        continue
    if elem + massa <= m:
        massa += elem
        count += 1
print(massa, count)
massa -= sp[51]
last = -1
for i in range(len(sp)):
    elem = sp[i]
    if massa + elem > m:
        print(last)
        break
    last = elem
print(massa)