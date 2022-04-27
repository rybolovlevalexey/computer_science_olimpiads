file = open('zadanie_24.txt', 'r')
st = file.read().strip()
dl = 0
mxdl = 0
for i in range(len(st)):
    if st[i] == 'C':
        dl += 1
    else:
        if mxdl < dl:
            mxdl = dl
        dl = 0
print(mxdl, dl)