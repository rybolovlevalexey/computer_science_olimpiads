from itertools import permutations
sp = set(permutations('кукуруза'))
ans = set()
for elem in sp:
    elem = ''.join(elem)
    if elem.count('уу') == 0 and elem.count('ау') == 0 and elem.count('уа') == 0:
        ans.add(elem)
print(len(ans))
