from pprint import pprint

st = st1 = "алексей"
sp = list()
sp.append(st1)
for i in range(len(st) - 1):
    st1 = st1[1:] + st1[0]
    sp.append(st1)
sp = sorted(sp)
bwt = "".join(tuple(elem[-1] for elem in sp))
pos = list(i for i in range(len(sp)) if sp[i] == st)[0]
print(bwt)
ans = list()
for i in range(len(st)):
    line = list()
    for j in range(len(st)):
        if j + 1 == len(st):
            line.append(bwt[i])
        else:
            line.append("*")
    ans.append(line)
ans = sorted(ans)
for k in range(len(st) - 1):
    for i in range(len(st)):  # проход по строкам
        ans[i][len(st) - 2 - k] = bwt[i]
    ans = sorted(ans)
print(''.join(ans[pos]))