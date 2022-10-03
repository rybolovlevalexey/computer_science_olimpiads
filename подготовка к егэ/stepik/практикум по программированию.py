sp = list()
for i in range(8):
    line = ["." for j in range(8)]
    sp.append(line)
st = input()
letters = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, }
x = letters[st[0]] - 1
y = 8 - int(st[1])
sp[y][x] = "N"
for i in [-1, -2, 1, 2]:
    for j in [-1, -2, 1, 2]:
        if abs(i) != abs(j):
            if 0 <= x + i <= 7 and 0 <= y + j <= 7:
                sp[y + j][x + i] = "*"
for elem in sp:
    print(*elem)