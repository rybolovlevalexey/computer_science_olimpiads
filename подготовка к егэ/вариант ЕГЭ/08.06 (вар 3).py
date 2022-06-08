file = open('24 (5).txt', 'r')
st = file.read().strip().split('E')
mxdl = 0
for elem in st:
    if elem.count('A') >= 3 and len(elem) > mxdl:
        mxdl = len(elem)
print(mxdl)