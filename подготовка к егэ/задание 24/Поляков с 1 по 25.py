file = open('24data/k7data/k7-25.txt')
st = file.read().strip()
mxdl = 0
dl = 0
for i in range(len(st)):
    if st[i] == 'C':
        dl += 1
    else:
        if dl != 0:
            if mxdl < dl:
                mxdl = dl
        dl = 0
print(mxdl, dl)