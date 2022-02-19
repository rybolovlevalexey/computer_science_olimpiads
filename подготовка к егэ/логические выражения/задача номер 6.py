print('x y z w result')
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            for w in [True, False]:
                res = (x and z) or ((not w or x) == (not z or y))
                if not res:
                    print(int(x), int(y), int(z), int(w), int(res))
