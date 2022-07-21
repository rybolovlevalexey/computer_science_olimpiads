first = input()
second = input()
fird = dict()
secd = dict()
for elem in first:
    if elem in fird:
        fird[elem] += 1
    else:
        fird[elem] = 1
for elem in second:
    if elem in secd:
        secd[elem] += 1
    else:
        secd[elem] = 1
if len(fird) == len(secd):
    for key in fird:
        if fird[key] != secd[key]:
            print(key)
else:
    for key, value in secd.items():
        if value == 1 and key not in fird:
            print(key)