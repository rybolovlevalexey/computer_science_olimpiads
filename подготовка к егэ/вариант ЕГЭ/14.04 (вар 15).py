print('x y z w res')
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            for w in [True, False]:
                res = not ((not z or w) and (not x == y)) + (x and z)
                if not res:
                    print(int(x), int(y), int(z), int(w), int(res))