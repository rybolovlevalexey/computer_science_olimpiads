file = open('26 (4).txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
n = sp[0]
del sp[0]
cnt = 0
mxsr = 0
chet = list(filter(lambda x: x % 2 == 0, sp))
for i in range(len(chet) - 1):
    for j in range(i + 1, len(chet)):
        if (chet[i] + chet[j]) % 2 == 0 and (chet[i] + chet[j]) // 2 in sp:
            cnt += 1
            if mxsr < (chet[i] + chet[j]) // 2:
                mxsr = (chet[i] + chet[j]) // 2
print(cnt, mxsr)