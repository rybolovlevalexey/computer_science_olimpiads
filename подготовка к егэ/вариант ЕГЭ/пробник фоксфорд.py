n = 1
sp = sorted(['З', 'A', 'Ч', 'Ю', 'Я'])
for i1 in sp:
    for i2 in sp:
        for i3 in sp:
            for i4 in sp:
                st = i1 + i2 + i3 + i4
                if i1 == 'Я':
                    print(n)
                    breakpoint()
                n += 1
