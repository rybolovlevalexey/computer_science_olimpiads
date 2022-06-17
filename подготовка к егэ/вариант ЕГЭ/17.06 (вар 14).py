print('x y z w res')
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            for w in [True, False]:
                res = (not x or y or not z or not w) and (not w or z or y)
                if not res:
                    print(int(x), int(y), int(z), int(w), int(res))