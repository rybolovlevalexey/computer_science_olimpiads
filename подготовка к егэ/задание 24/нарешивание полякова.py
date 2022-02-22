st = input()
print(st.count('BAFEBAFEBAFEBAFEBAFEBAFEBAFEBAF'))
print(len('BAFEBAFEBAFEBAFEBAFEBAFEBAFEBAF'))
dl = 0
max_dl = -1
let = {0: 'B', 1: 'A', 2: 'F', 3: 'E'}
letter = 0  # B-0; A-1; F-2; E-3
for i in range(len(st)):
    if st[i] == let[letter]:
        dl += 1
        if max_dl < dl:
            max_dl = dl
    else:
        if max_dl < dl:
            max_dl = dl
        dl = 0
    letter = (letter + 1) % 4
print(max_dl)
print(dl)