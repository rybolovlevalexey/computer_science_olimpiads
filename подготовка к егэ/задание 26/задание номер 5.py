file = open('Zadanie_26_tablisa.txt', 'r')
sp = file.read().strip().split('\n')
s, n = map(int, sp[0].split())
del sp[0]
sp = list(sorted(map(int, sp)))
summa = 0
counter = 0
for i in range(len(sp) - 1):
    elem = sp[i]
    flag = False
    if summa + elem + sp[i + 1] > s:
        flag = True
        maximum = 0
        counter += 1
        for j in range(i, len(sp)):
            if summa + sp[j] <= s:
                maximum = sp[j]
                print(maximum)
            else:
                summa += maximum
                break
    if flag:
        break
    summa += elem
    counter += 1
print(summa, s)
print(counter, maximum)