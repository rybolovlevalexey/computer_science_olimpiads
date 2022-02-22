st = input()
dl = 0
max_dl = None
for i in st:
    if i == 'C':
        dl += 1
    else:
        if max_dl is None or max_dl < dl:
            max_dl = dl
        dl = 0
print(max_dl)
