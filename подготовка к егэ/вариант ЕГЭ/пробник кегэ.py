file = open('24 (10).txt', 'r')
st = file.read().strip()
dl = 1
mxdl = 0
ansst = ''
s = st[0]
for i in range(1, len(st)):
    if int(s[-1]) <= int(st[i]):
        dl += 1
        s += st[i]
    else:
        if dl > mxdl:
            mxdl = dl
            ansst = s
        dl = 1
        s = st[i]
print(mxdl, ansst)
print(dl, s)
print(st[st.index(ansst) - 1: st.index(ansst) + 49 + 1])