file = open('zadanie24_2.txt', 'r')
st = file.read().strip()
max_dlina = 0
dlina = 0
for i in range(len(st)):
    elem = st[i]
    if elem == 'D':
        dlina += 1
    else:
        if dlina > 0 and max_dlina < dlina:
            max_dlina = dlina
        dlina = 0
print(max_dlina)