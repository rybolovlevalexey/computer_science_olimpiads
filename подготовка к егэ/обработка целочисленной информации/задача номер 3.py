file = open('17_6.txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
counter = 0
for i in range(len(sp) - 3):
    suka = sp[i] + sp[i + 1] + sp[i + 2] + sp[i + 3]
    if sp[i] % 2 == sp[i + 1] % 2 == sp[i + 2] % 2 == sp[i + 3] % 2 == 1:
        if '888' in str(suka):
            counter += 1
print(counter)