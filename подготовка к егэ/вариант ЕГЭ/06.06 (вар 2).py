file = open('24 (4).txt', 'r')
sp = file.read().strip().split('\n')
cnt = None
ansst = ''
for elem in sp:
    if cnt is None or elem.count('N') < cnt:
        cnt = elem.count('N')
        ansst = elem
d = dict()
for let in ansst:
    if let in d:
        d[let] += 1
    else:
        d[let] = 1
print(d)
print(max(d.values()))
ansd = dict()
for key, value in d.items():
    if value == max(d.values()):
        ansd[key] = value
print(ansd)
print(sorted(ansd.keys())[-1])