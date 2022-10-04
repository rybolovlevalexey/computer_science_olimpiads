st = input()
d = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
x = d[st[0]]
y = 8 - int(st[1])
sp = list(['.'] * 8 for i in range(8))
sp[y][x] = 'Q'
for i in range(8):
    if i != y:
        sp[i][x] = '*'
    if i != x:
        sp[y][i] = '*'

for i in range(1, 8):
    if 0 <= x - i <= 7 and 0 <= y - i <= 7:
        sp[y - i][x - i] = '*'
    if 0 <= x + i <= 7 and 0 <= y + i <= 7:
        sp[y + i][x + i] = '*'
    if 0 <= x + i <= 7 and 0 <= y - i <= 7:
        sp[y - i][x + i] = '*'
    if 0 <= x - i <= 7 and 0 <= y + i <= 7:
        sp[y + i][x - i] = '*'
for elem in sp:
    print(*elem)