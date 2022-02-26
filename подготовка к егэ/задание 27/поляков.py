file = open('27data/1/27-1a.txt', 'r')
sp = file.read().strip().split('\n')
n = int(sp[0])
del sp[0]
s = 0
ind = None
delta = None
for i in range(n):
    elem = list(map(int, sp[i].split()))
    s += min(elem)
    if abs(elem[1] - elem[0]) % 3 != 0 and (delta is None or delta > abs(elem[1] - elem[0])):
        delta = abs(elem[1] - elem[0])
        ind = i
    sp[i] = elem
print(delta, ind)
ans = 0
for i in range(n):
    if i == ind:
        ans += max(sp[i])
    else:
        ans += min(sp[i])
print(ans, ans % 3)