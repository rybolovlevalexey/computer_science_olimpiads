st = input().split()
n = int(st[0])
del st[0]
sp = list(map(int, st))
num = min(sp)
for i in range(len(sp)):
    if sp[i] == max(sp):
        sp[i] = num
print(*sp)