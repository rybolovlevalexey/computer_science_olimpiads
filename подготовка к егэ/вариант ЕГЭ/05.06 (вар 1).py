file = open('27_B.txt', 'r')
sp = file.read().strip().split('\n')
n = int(sp[0])
del sp[0]
for i in range(n):
    elem = sp[i]
    sp[i] = list(map(int, elem.split()))
summa = 0
delta = None

for elem in sp:
    a, b, c = elem
    summa += max(elem)
    if len(set(elem)) == 1 or len(set(elem)) == 2:
        continue
    rd1 = abs(a - b)
    rd2 = abs(a - c)
    rd3 = abs(b - c)
    rd = list(filter(lambda x: x % 109 != 0 and x != 0, [abs(a - b), abs(a - c), abs(b - c)]))
    if len(rd) > 0 and (delta is None or delta > min(rd)):
        delta = min(rd)

print(summa)
print(summa % 109)
print(delta)
ans = summa + delta
print(ans)
print(ans % 109)