print('x y z w result')
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            for w in [True, False]:
                res = (x == (w or y)) or ((not w or z) and (not y or w))
                if not res:
                    print(int(x), int(y), int(z), int(w), int(res))