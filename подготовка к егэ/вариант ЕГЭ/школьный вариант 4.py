file = open('zadanie_27B.txt', 'r')
sp = file.read().strip().split('\n')
n = int(sp[0])
del sp[0]
i = 0
while i < n:
    sp[i] = list(map(int, sp[i].split(' ')))
    i += 1
summa = 0
for elem in sp:
    summa += min(elem)
print(summa, summa % 13)