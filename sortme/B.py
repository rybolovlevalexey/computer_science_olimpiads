n, m = map(int, input().split())
rebra = set()
svyazi = dict()
for i in range(m):
    k1, k2 = map(int, input().split())
    rebra.add(k1)
    rebra.add(k2)
    svyazi[k1] = k2
    svyazi[k2] = k1
flag = True
for i in range(len(rebra)):
    if i == len(rebra) - 1:
        break