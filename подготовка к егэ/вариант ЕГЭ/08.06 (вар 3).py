print('x y z res')
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            res = (x == z) or (not(x) or (y and z))
            if not res:
                print(int(x), int(y), int(z), int(res))
