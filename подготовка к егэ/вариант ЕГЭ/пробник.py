n = 1
glas = ['е', 'а']
sp = sorted(['ф', 'е', 'в', 'р', 'а', 'л', 'ь'])
for i1 in sp:
    for i2 in sp:
        for i3 in sp:
            for i4 in sp:
                for i5 in sp:
                    for i6 in sp:
                        if i1 not in glas and i2 not in glas and i3 not in glas and i4 not in glas and i5 not in glas and i6 not in glas:
                            print(n)
                            x = 1/0
                        n += 1
