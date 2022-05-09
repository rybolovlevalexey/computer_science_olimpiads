file = open('273802.txt', 'r')
st = file.read().strip()

dl = 1
mxdl = 0
for i in range(len(st) - 1):
    if st[i] != st[i + 1]:
        dl += 1
    else:
        if dl > mxdl:
            mxdl = dl
        dl = 1
print(mxdl, dl)
