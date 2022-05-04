print('x y z res')
for x in (True, False):
    for y in (True, False):
        for z in (True, False):
            res = (x or not z) and (y or z)
            print(int(x), int(y), int(z), int(res))
