print('x y z w res')
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            for w in [True, False]:
                res = not w or (x or not z) and (not x or not y or z) and not w or (x or not z) and (not x or not y or z)
                if not res:
                    print(int(x), int(y), int(z), int(w), int(res))