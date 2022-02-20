st = input()
dlina = 0
max_dlina = None
for i in range(len(st) - 1):
    if st[i] != st[i + 1]:
        dlina += 1
    else:
        if max_dlina is None or max_dlina < dlina:
            max_dlina = dlina
        dlina = 0
print(max_dlina)
