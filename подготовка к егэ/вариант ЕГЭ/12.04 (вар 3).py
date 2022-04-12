print('x y z res')
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            res = (not x and not y) or (z == x)
            if not res:
                print(int(x), int(y), int(z), int(res))
