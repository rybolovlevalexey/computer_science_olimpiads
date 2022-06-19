file = open('27-B (4).txt', 'r')
sp = file.read().strip().split('\n')
del sp[0]
sp = list(sorted(map(int, sp)))
m1 = sorted(filter(lambda x: x % 3 == 1, sp))[:3]
m2 = sorted(filter(lambda x: x % 3 == 2, sp))[:3]
m = sorted(filter(lambda x: x % 3 == 0, sp))[:3]
ans = list()
ans.append(min(m1) + min(m2) + min(m))
ans.append(sum(m))
ans.append(sum(m1))
ans.append(sum(m2))
print(min(ans), min(ans) % 3)
print(ans)