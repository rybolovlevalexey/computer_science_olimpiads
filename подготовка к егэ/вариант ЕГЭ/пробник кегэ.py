file = open('26 (9).txt', 'r')
sp = file.read().strip().split('\n')
s, n = map(int, sp[0].split())
del sp[0]
percnt = 0
cntB = 0
afiles = list()
bfiles = list()
for i in range(n):
    num, type = sp[i].split()
    if type == 'A':
        afiles.append(int(num))
    else:
        bfiles.append(int(num))
afiles = sorted(afiles)[::-1]
bfiles = sorted(bfiles)
while len(afiles) > 0:
    summa = 0
    i = 0
    while i < len(afiles):
        elem = afiles[i]
        if elem + summa <= s:
            summa += elem
            del afiles[i]
        else:
            i += 1
    percnt += 1
    i = 0
    while i < len(bfiles):
        elem = bfiles[i]
        if elem + summa <= s:
            summa += elem
            cntB += 1
            del bfiles[i]
        else:
            i += 1
print(percnt, cntB)