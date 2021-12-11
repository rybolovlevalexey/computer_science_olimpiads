print('x y z w res')
for x in [False, True]:
    for y in [False, True]:
        for z in [False, True]:
            for w in [False, True]:
                res = (x and z) or ((not w or x) == (not z or y))
                if not res:
                    print(int(x), int(y), int(z), int(w), int(res))
