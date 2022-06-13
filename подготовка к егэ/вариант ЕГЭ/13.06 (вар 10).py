file = open('27991_B.txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
mxsm = 0
del sp[0]
ans = list()
chet = sorted(filter(lambda x: x % 2 == 0, sp))[::-1]
nechet = sorted(filter(lambda x: x % 2 != 0, sp))[::-1]
if chet[0] % 17 == 0:
    ans.append(chet[0] + chet[1])
else:
    chet17 = list(filter(lambda x: x % 17 == 0, chet))
    if len(chet17) > 0:
        ans.append(max(chet17) + chet[0])
if nechet[0] % 17 == 0:
    ans.append(nechet[0] + nechet[1])
else:
    nechet17 = list(filter(lambda x: x % 17 == 0, nechet))
    if len(nechet17) > 0:
        ans.append(max(nechet17) + nechet[0])
print(max(ans))
