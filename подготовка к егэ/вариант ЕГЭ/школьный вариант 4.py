sp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
num = 1
for i1 in sp:
    for i2 in sp:
        for i3 in sp:
            for i4 in sp:
                st = i1 + i2 + i3 + i4
                if st == 'ddfa':
                    print(num)
                    break
                num += 1
