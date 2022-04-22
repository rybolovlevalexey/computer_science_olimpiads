print('x y z res')
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            res = (not x and y and z) or (not x and not y and z) or (not x and not y and not z)
            if res:
                print(int(x), int(y), int(z), int(res))

