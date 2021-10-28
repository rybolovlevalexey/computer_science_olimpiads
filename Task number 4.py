n = int(input())  # количество высот
k = int(input())  # длина отрезка, k + 1 = количество высот
ans_sp = list()  # стартовая позиция, дельта энергии
sp = list()
for i in range(n):
    elem = int(input())
    sp.append(elem)

for start in range(n - k):
    delta = 0
    otr = sp[start: start + k + 1]
    for i in range(1, k + 1):
        i1 = otr[i - 1]
        i2 = otr[i]
        if i1 < i2:
            delta -= abs(i1 - i2)
        else:
            delta += abs(i1 - i2)
    if len(ans_sp) == 0 or ans_sp[1] < delta:
        ans_sp = [start, delta]
print(ans_sp[0] + 1)
