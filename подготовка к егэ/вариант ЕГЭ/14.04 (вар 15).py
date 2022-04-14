file = open('17 (2).txt', 'r')
sp = file.read().strip().split('\n')
sp = list(map(int, sp))
ans = 0
max_sum = 0
for i in range(len(sp) - 1):
    i1 = sp[i]
    i2 = sp[i + 1]
    if (i1 % 5 == 0 or i2 % 5 == 0) and (i1 + i2) % 7 == 0:
        ans += 1
        if i1 + i2 > max_sum:
            max_sum = i1 + i2
print(ans, max_sum)
