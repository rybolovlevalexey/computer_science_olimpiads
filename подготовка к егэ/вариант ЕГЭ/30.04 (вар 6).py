print('x y z res')
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            res = not z and x or x and y
            print(int(x), int(y), int(z), int(res))