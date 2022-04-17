file = open('24data/k7data/k7-5.txt')
st = file.read().strip()
mdlin = None
dlina = 0
print(st)
for i in range(len(st)):
    if st[i] == 'C':
        dlina += 1
    else:
        if dlina != 0:
            if mdlin is None or mdlin < dlina:
                mdlin = dlina
            dlina = 0
print(dlina, mdlin)
