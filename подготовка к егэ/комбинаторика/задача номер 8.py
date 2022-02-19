from itertools import permutations
sp = set(permutations('ШУРУМБУРУМ'))
soglas = ['Ш', 'Р', 'М', 'Б']
ans = set()
print(len(sp))
for elem in sp:
    elem = ''.join(elem)
    flag = True
    for j in range(len(elem) - 2):
        if elem[j] in soglas and elem[j + 1] in soglas and elem[j + 2] in soglas:
            flag = False
            break
    if flag:
        ans.add(elem)
print(len(ans))
