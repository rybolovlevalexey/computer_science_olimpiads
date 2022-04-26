file = open('24.txt', 'r')
st = file.read().strip()
indexes = list()
for i in range(len(st)):
    if st[i] == 'A':
        indexes.append(i)
mxdl = 0
for i in range(len(indexes) - 2):
    if indexes[i + 2] - indexes[i] - 1 > mxdl:
        mxdl = indexes[i + 2] - indexes[i] - 1
print(mxdl)