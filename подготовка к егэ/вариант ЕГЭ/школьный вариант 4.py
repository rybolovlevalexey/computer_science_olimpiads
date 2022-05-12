sp = [0] * 51
sp[50] = 1
for i in range(49, 29, -1):
    if i + 3 <= 50:
        sp[i] = sp[i + 3] + sp[i + 2]
    elif i + 2 <= 50:
        sp[i] = sp[i + 2]
    else:
        sp[i] = 0

    if i * 2 + 1 <= 50:
        sp[i] += sp[i * 2 + 1]
        if sp[i * 2 + 1] != 0:
            print('i am here')
    if i * 2 <= 50:
        sp[i] += sp[i * 2]
        if sp[i * 2] != 0:
            print('i am here')
print(sp)
print(sp[30])
for i in range(50, 30, -1):
    sp[i] = 0
print(sp)
for i in range(29, 17, -1):
    if i == 23:
        continue
    if i + 3 <= 50:
        sp[i] = sp[i + 3] + sp[i + 2]
    elif i + 2 <= 50:
        sp[i] = sp[i + 2]
    else:
        sp[i] = 0

    if i * 2 + 1 <= 50:
        sp[i] += sp[i * 2 + 1]
        if sp[i * 2 + 1] != 0:
            print('i am here')
    if i * 2 <= 50:
        sp[i] += sp[i * 2]
        if sp[i * 2] != 0:
            print('i am here')

print(sp)
print(sp[18])
