file = open('17_7.txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
cnt = 0
chet = list(filter(lambda x: x % 2 == 0, sp))
nechet = list(filter(lambda x: x % 2 != 0, sp))
src = sum(chet) / len(chet)
srn = sum(nechet) / len(nechet)
mxsm = 0
for i in range(len(sp) - 1):
    s = sp[i] + sp[i + 1]
    if src <= s <= srn:
        cnt += 1
        if s > mxsm:
            mxsm = s
print(cnt, mxsm)