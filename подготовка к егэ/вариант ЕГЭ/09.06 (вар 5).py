print('x y z res')
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            res = (not x or y) and (not y or z)
            if res:
                print(int(x), int(y), int(z), int(res))
