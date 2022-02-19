from itertools import permutations
sp = set(permutations('ШУРУМБУРУМ'))
soglas = ['Ш', 'Р', 'М', 'Б']
glas = ['У']
ans = set()
print(len(sp))
for elem in sp:
    elem = ''.join(elem)
    flag1 = True
    for j in range(len(elem) - 2):
        if elem[j] in soglas and elem[j + 1] in soglas and elem[j + 2] in soglas:
            flag1 = False
            break
    flag2 = True
    for j in range(len(elem) - 1):
        if elem[j] in glas and elem[j + 1] in glas:
            flag2 = False
            break
    if flag1 and flag2:
        ans.add(elem)
print(len(ans))
