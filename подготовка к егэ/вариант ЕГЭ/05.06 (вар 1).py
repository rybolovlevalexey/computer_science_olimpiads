file = open('26 (2).txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
n = sp[0]
del sp[0]
nechet = list(filter(lambda x: x % 2 == 1, sp))
cnt = 0
mxsr = 0

for i in range(len(nechet) - 1):
    for j in range(i + 1, len(nechet)):
        if (nechet[i] + nechet[j]) % 2 == 0 and (nechet[i] + nechet[j]) // 2 in sp:
            cnt += 1
            if (nechet[i] + nechet[j]) // 2 > mxsr:
                mxsr = (nechet[i] + nechet[j]) // 2
print(cnt, mxsr)