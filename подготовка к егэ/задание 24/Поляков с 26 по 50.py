file = open('24data/k7data/k7b-1.txt')
st = file.read().strip()
letters = {0: 'E', 1:'A', 2:'B'}
num = 0  # 0-E, 1-A, 2-B
dl = 0
mxdl = 0
for elem in st:
    if elem == letters[num]:
        dl += 1
    else:
        if dl > mxdl:
            mxdl = dl
        dl = 0
    num = (num + 1) % 3
print(mxdl, dl)