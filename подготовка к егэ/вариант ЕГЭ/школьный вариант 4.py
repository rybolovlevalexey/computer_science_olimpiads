file = open('zadanie_17.txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
cnt = 0
summa = 0

for elem in sp:
    cntdelit = 0
    for d in [7, 13, 17, 19]:
        if elem % d == 0:
            cntdelit += 1
    if cntdelit == 2:
        cnt += 1
        summa += sum(map(int, list(str(elem))))
print(cnt, summa)
