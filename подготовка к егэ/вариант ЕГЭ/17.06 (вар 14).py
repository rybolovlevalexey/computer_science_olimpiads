sp = ['a', 'b', 'c', 'd', 'e']
cnt = 0
for i1 in sp[:-1]:
    for i2 in sp:
        for i3 in sp:
            for i4 in sp:
                for i5 in sp[1:]:
                    cnt += 1
print(cnt)