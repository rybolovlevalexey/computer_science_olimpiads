sp = ['е', 'г', 'э']
glas = ['е', 'э']
cnt = 0
for i1 in glas:
    for i2 in sp:
        for i3 in sp:
            for i4 in sp:
                for i5 in sp:
                    cnt += 1
print(cnt)