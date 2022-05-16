file = open('zadanie_24.txt', 'r')
st = file.read().strip()
dl = 1
mxdl = 0
ans = 0

for i in range(1, len(st)):
    if st[i - 1] == st[i]:
        dl += 1
    else:
        if dl > mxdl:
            mxdl = dl
            ans = st[i - 1]
        dl = 1
print(mxdl, ans)
if dl > mxdl:
    mxdl = dl
    ans = st[-1]
print(mxdl, ans)
print(st.count('LLLLL'))