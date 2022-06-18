file = open('27data/52/27-52b.txt', 'r')
sp = file.read().strip().split('\n')
n = int(sp[0])
del sp[0]
sp = sorted(map(int, sp))[::-1]
mx1 = sorted(filter(lambda x: x % 3 == 1, sp))[::-1][:3]
mx2 = sorted(filter(lambda x: x % 3 == 2, sp))[::-1][:3]
mx = sorted(filter(lambda x: x % 3 == 0, sp))[::-1][:3]
ans = list()
ans.append(max(mx1) + max(mx2) + max(mx))
ans.append(sum(mx1))
ans.append(sum(mx))
ans.append(sum(mx2))
print(ans)
print(max(ans))
print(max(ans) % 3)