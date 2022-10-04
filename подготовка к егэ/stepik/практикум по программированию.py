n = int(input())
sp = list()
flag = True
for i in range(n):
    line = list(map(int, input().split()))
    sp.append(line)
    if list(sorted(set(line))) != list(i+1 for i in range(n)):
        flag = False
for j in range(n):
    line = set()
    for i in range(n):
        line.add(sp[i][j])
    if list(sorted(line)) != list(i+1 for i in range(n)):
        flag = False
print("YES" if flag else "NO")