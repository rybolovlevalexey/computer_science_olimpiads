n = int(input())
sp = list()
for i in range(n):
    sp.append(input())
sp = sorted(sp)
gem = dict()
for elem in sp:
    s = 0
    for j in elem.upper():
        s += ord(j) - ord("A")
    gem[elem] = s
for value in set(sorted(gem.values())):
    for key in gem:
        if gem[key] == value:
            print(key)
