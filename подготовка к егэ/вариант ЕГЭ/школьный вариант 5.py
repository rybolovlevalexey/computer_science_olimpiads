file = open('zadanie_24.txt', 'r')
st = file.read().strip()
dl = 1
mxdl = 0

for i in range(1, len(st)):
    if st[i] != st[i - 1]:
        dl += 1
    else:
        if dl > mxdl:
            mxdl = dl
        dl = 1

if dl > mxdl:
    mxdl = dl
print(mxdl)