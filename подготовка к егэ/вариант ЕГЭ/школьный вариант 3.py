file = open('zadanie_24.txt', 'r')
ans = 0
st = file.read().strip()

for i in range(len(st) - 2):
    i1 = st[i]
    i2 = st[i + 1]
    i3 = st[i + 2]
    if i1 in ['B', 'C', 'D'] and i2 in ['B', 'D', 'E'] and i1 != i2 and i3 in ['B', 'C', 'E'] and i2 != i3:
        ans += 1
print(ans)
print(len(st))