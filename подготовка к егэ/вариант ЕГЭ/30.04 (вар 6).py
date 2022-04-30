file = open('18.txt', 'r')
sp = [float(i) for i in file.read().strip().split('\n')]
mxsm = 0

for i in range(len(sp) - 1):
    sm = 0
    ind = i
    sm += sp[ind]
    while True:
        if ind + 1 == len(sp):
            break
        if abs(sp[ind] - sp[ind + 1]) <= 10:
            ind += 1
            sm += sp[ind]
        else:
            break
    if sm > mxsm:
        mxsm = sm
print(mxsm, sm)