file = open('27-A (2).txt', 'r')
sp = list(sorted(map(int, file.read().strip().split('\n'))))
del sp[0]
d = dict()
for elem in sp[:20]:
    d[elem] = elem % 3
print(d)