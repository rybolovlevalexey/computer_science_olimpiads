cnt = 1
sp = sorted(['м', 'у', 'х', 'а'])
for i1 in sp:
    for i2 in sp:
        for i3 in sp:
            for i4 in sp:
                st = i1 + i2 + i3 + i4
                if st == 'хухх':
                    print(cnt)
                cnt += 1
