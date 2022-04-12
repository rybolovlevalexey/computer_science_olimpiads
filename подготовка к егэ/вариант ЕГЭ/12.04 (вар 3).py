file = open('24.txt', 'r')
st = file.read().strip()
all_indexes = list()
max_dlina = 0
for i in range(len(st)):
    if st[i] == 'D':
        all_indexes.append(i)
for i1 in range(len(all_indexes) - 2):
    i2 = i1 + 2
    dlina = all_indexes[i2] - all_indexes[i1] - 1
    if dlina > max_dlina:
        max_dlina = dlina
print(max_dlina)