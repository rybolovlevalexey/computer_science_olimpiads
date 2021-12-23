file = open('17_4.txt', 'r')
sp = list(map(int, file.read().strip().split('\n')))
maximum = 0
counter = 0
for i in range(len(sp) - 2):
    if sp[i] < sp[i + 1] and sp[i + 1] < sp[i + 2]:
        counter += 1
    if sp[i] + sp[i + 1] + sp[i + 2] > maximum:
        maximum = sp[i] + sp[i + 1] + sp[i + 2]
print(counter, maximum)