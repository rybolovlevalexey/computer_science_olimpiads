file = open('26.txt', 'r')
sp = file.read().strip().split('\n')
n = int(sp[0])
del sp[0]
rady = dict()
for elem in sp:
    ryd, place = map(int, elem.split())
    if ryd in rady:
        rady[ryd] += [place]
    else:
        rady[ryd] = [place]

for key in sorted(rady.keys())[::-1]:
    if len(rady[key]) >= 2:
        longryad = sorted(rady[key])
        for i in range(len(longryad) - 1):
            if longryad[i + 1] - longryad[i] - 1 == 2:
                print(key, longryad[i] + 1)