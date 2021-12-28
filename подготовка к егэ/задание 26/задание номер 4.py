file = open('26_2(1).txt', 'r')
sp = file.read().strip().split('\n')
n = int(sp[0])
del sp[0]
maximum = 0
summa = 0
for elem in sp:
    elem = int(elem)
    if elem > 50:
        if elem > maximum:
            maximum = elem
        elem = elem * 0.85
        if elem != int(elem):
            elem = int(elem) + 1
        else:
            elem = int(elem)
    summa += elem
print(summa)
print(maximum)