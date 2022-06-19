file = open('127992(3).txt', 'r')
st = file.read().strip()
cnt = 0
for i in range(len(st) - 3):
    i1 = st[i]
    i2 = st[i + 1]
    i3 = st[i + 2]
    i4 = st[i + 3]
    mn = {i1, i2, i3, i4}
    if len(mn) == 4:
        cnt += 1
print(cnt)