spisok = ['B', 'C', 'D', 'F']
file = open('24data/k7data/k7a-6.txt')
st = file.read().strip()
mxdl = 0
dl = 0
for i in range(len(st)):
    if st[i] in spisok:
        dl += 1
    else:
        if dl != 0 and mxdl < dl:
            mxdl = dl
        dl = 0
print(mxdl, dl)