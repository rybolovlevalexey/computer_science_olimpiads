file = open('24.txt', 'r')
st = file.read().strip()
indexes = list()
for i in range(len(st) - 3):
    if st[i:i+4] == 'XZZY':
        indexes.append(i)
ans = -1
indexes = indexes[::-1]
for j in range(len(indexes) - 1):
    delta = indexes[j] - indexes[j + 1] - 4
    if delta > ans:
        ans = delta
print(ans)
maximum = -1
for i in range(len(indexes) - 1):
    delta = abs(indexes[i] - indexes[i + 1])
    if delta > maximum:
        maximum = delta
print(maximum)