file = open('Zimnii_EGE_27_A.txt', 'r')
sp = file.read().strip().split('\n')
for i in range(len(sp)):
    sp[i] = list(map(int, sp[i].split()))
summa = 0
for elem in sp:
    summa += max(elem)
print(summa)
flag = False
delts = []
for i in range(len(sp)):
    elem = sp[i]
    if (max(elem) - min(elem)) % 4 != 0:
        flag = True
        delts.append([(max(elem) - min(elem)), i])

print(delts)
index = min(delts, key=lambda x: x[0])[1]
new_sum = 0
for j in range(len(sp)):
    if j == index:
        new_sum += min(sp[j])
    else:
        new_sum += max(sp[j])
print(new_sum)