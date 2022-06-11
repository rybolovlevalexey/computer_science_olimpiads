file = open('24_demo (1).txt', 'r')
st = file.read().strip()
ansst = ''
mxdl = 0
dl = 1
s = st[0]
for i in range(1, len(st)):
    if s[-1] == st[i]:
        if dl > mxdl:
            mxdl = dl
            ansst = s
        dl = 1
        s = st[i]
    else:
        s += st[i]
        dl += 1
print(ansst, mxdl)
