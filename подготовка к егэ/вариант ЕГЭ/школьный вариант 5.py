file = open('zadanie_24.txt', 'r')
st = file.read().strip()
dl = 1
ans = ''
s = st[0]
mxdl = 0

for i in range(1, len(st)):
    if st[i] != st[i - 1]:
        dl += 1
        s += st[i]
    else:
        if dl > mxdl:
            mxdl = dl
            ans = s
        dl = 1
        s = st[i]

if dl > mxdl:
    mxdl = dl
print(mxdl)
print(ans)
print(st.count(ans))
print(st.index(ans))
ind = st.index(ans)
print(st[ind: ind + 85])