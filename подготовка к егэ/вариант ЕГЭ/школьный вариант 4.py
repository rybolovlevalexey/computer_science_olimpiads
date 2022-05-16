file = open('zadanie_26.txt', 'r')
sp = file.read().strip().split('\n')
s, n = map(int, sp[0].split())
del sp[0]
sp = list(reversed(sorted(map(int, sp))))
print(sp)
anscnt = 0
mnchis = None
summa = 0

i = 0
while i < n:
    if summa + sp[i] <= s:
        summa += sp[i]
        anscnt += 1
        if mnchis is None or mnchis > sp[i]:
            mnchis = sp[i]
    i += 1
print(anscnt, mnchis)
print(summa)