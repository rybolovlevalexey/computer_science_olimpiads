file = open('24 (9).txt', 'r')
sp = file.read().strip().split('\n')
ansn = None
ansst = ''
for elem in sp:
    if ansn is None or ansn < elem.count('N'):
        ansn = elem.count('N')
        ansst = elem
d = dict()
for let in ansst:
    if let in d:
        d[let] += 1
    else:
        d[let] = 1
ans = list()
for key in d.keys():
    if d[key] == max(d.values()):
        ans.append(key)
print(ans)