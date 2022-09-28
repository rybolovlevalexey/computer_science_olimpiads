n = int(input())
sp = list()
mx = 0
flag = True
left = list()
rigth = list()
up = list()
down = list()
for i in range(n):
    line = list(map(int, input().split()))
    sp.append(line)
for i in range(n):
    sp[i][i] = 0
    sp[i][n - i - 1] = 0
for i in range(n):
    if i <= n // 2:
        left.extend(sp[i][:i+1])
        rigth.extend(sp[i][n-i-1:])
        up.extend(sp[i][i: n-i])
    else:
        left.extend(sp[i][:n-i])
        rigth.extend(sp[i][i:])
        start = sp[i].index(0)
        down.extend(sp[i][start:sp[i].index(0, start + 1) + 1])
print(f"Верхняя четверть: {sum(up)}")
print(f"Правая четверть: {sum(rigth)}")
print(f"Нижняя четверть: {sum(down)}")
print(f"Левая четверть: {sum(left)}")