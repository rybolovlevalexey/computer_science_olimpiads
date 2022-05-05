file = open('zadanie_26.txt', 'r')
sp = file.read().strip().split('\n')
s, n = map(int, sp[0].split())
del sp[0]
sp = list(sorted(map(int, sp)))[::-1]
print(sum(sp))
summa = 0
cnt = 0
last_ind = 0
mn = None
for i in range(len(sp)):
    if summa + sp[i] > s:
        break
    else:
        summa += sp[i]
        last_ind = i
        cnt += 1
        if mn is None or mn > sp[i]:
            mn = sp[i]
sp = sp[::-1]
for j in range(0, len(sp)):
    if sp[j] + summa <= s and sp[j + 1] + summa > s:
        print(sp[j])
        break

print(cnt + 1)
