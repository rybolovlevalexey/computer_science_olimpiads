print('x y z res')
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            for w in [True, False]:
                res = (x == y) or (z == (y or w))
                if not res:
                    print(int(x), int(y), int(z), int(w), int(res))
