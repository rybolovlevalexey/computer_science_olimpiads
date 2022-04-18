file = open('24data/k7data/k7b-2.txt')
st = file.read().strip()
letters = {0: 'D', 1: 'B', 2: 'A', 3: 'C'}
num = 0
dl = 0
mxdl = 0
for elem in st:
    if elem == letters[num] and dl == 0:
        num = 0
    if elem == letters[num]:
        dl += 1
        num = (num + 1) % 4
    else:
        if dl > mxdl:
            mxdl = dl
        dl = 0
print(mxdl, dl)
print(st.count('DBAC' * 23))