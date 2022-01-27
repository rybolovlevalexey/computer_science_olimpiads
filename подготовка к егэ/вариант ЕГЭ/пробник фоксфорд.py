file = open('Zadanie-260232.txt', 'r')
sp = file.read().strip().split('\n')
sp = list(map(int, sp))
cnt = 0
maximum = None
for i in range(len(sp) - 1):
    i1 = sp[i]
    i2 = sp[i + 1]
    if (i1 + i2) % 3 == 0 and (i1 + i2) % 6 != 0:
        cnt += 1
        if maximum is None or (i1 + i2) > maximum:
            maximum = i1 + i2
print(cnt, maximum)