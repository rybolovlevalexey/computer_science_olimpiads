file = open('17_5.txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
counter = 0
maximum = 0
for i in range(len(sp) - 3):
    suka = sp[i] + sp[i + 1] + sp[i + 2] + sp[i + 3]
    if suka == maximum:
        counter += 1
    elif suka > maximum:
        maximum = suka
        counter = 1
print(maximum, counter)