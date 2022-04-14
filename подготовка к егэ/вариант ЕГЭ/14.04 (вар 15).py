sp = set()
i1 = '*2+1'
num = eval('1' + i1)
print(num)
for i1 in ['*2', '*2+1']:
    for i2 in ['*2', '*2+1']:
        for i3 in ['*2', '*2+1']:
            for i4 in ['*2', '*2+1']:
                for i5 in ['*2', '*2+1']:
                    for i6 in ['*2', '*2+1']:
                        for i7 in ['*2', '*2+1']:
                            for i8 in ['*2', '*2+1']:
                                for i9 in ['*2', '*2+1']:
                                    for i10 in ['*2', '*2+1']:
                                        num = eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval('1' + i1)) + i2)) + i3)) + i4)) + i5)) + i6)) + i7)) + i8)) + i9)) + i10)
                                        sp.add(num)
print(sp)
print(len(sp))