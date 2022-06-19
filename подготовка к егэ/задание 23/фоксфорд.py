file = open('Zadanie_24_text_dlia_KR_4.txt', 'r')
st = file.read().strip()
dl = 1
mxdl = 0
s = st[0]
for i in range(len(st) - 1):
    if st[i] != st[i + 1]:
        dl += 1
        s += st[i + 1]
    else:
        if dl > mxdl:
            mxdl = dl
            anst = s
        s = st[i + 1]
        dl = 1
print(mxdl)
print(dl)
print(len(anst), anst)
print(st[st.index(anst) - 1 : st.index(anst) + len(anst) + 2])