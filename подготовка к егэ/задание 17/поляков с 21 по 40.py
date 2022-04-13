sp = list()
for i in range(2461, 9719 + 1):
    if 3 <= i % 100 // 10 <= 7 and str(i)[-3] not in ['1', '9']:
        sp.append(i)
print(len(sp), max(sp))