def countchet(spisok):
    res = 0
    for elem in spisok:
        if elem > 0 and elem % 2 == 0:
            res += 1
    return res
answer = 0
file = open('27-A (3).txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
del sp[0]
chetind = list()
for i in range(len(sp)):
    elem = sp[i]
    if elem > 0 and elem % 2 == 0:
        chetind.append(i)
ind1 = 0; ind2 = 29
i1 = chetind[ind1]
i2 = chetind[ind2]
chetcount = 0
while True:
    if ind2 + 1 > len(chetind):
        for start in range(0, i1 + 1):
            for finish in range(i2, chetind[ind2 + 1]):
                srez = sp[start: finish + 1]
                #print(sum(srez))
                if countchet(srez) % 30 != 0:
                    print('fuuuuuuuuuuuuuuuuuuuuuuck')
                if sum(srez) > answer:
                    answer = sum(srez)
    ind2 += 30
    if ind2 >= len(chetind):
        ind1 += 1
        ind2 = ind1 + 29
        if ind2 >= len(chetind):
            break
    i1 = chetind[ind1]
    i2 = chetind[ind2]

print(answer)