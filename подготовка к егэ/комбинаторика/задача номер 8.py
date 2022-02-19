from itertools import permutations
sp = set(permutations('ВЫИГРЫВАТЬ'))
glas = ['Ы', 'И', 'А']
ans = set()
print(len(sp))
for elem in sp:
    elem = ''.join(elem)
    flag = True
    for j in range(len(elem) - 1):
        if elem[j] in glas and elem[j + 1] in glas:
            flag = False
            break
    if elem[0] != 'Ь' and flag:
        ans.add(elem)
print(len(ans))
