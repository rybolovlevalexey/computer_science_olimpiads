print('x y z w res')
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            for w in [True, False]:
                res = (y and x) == (not y or w) or not z
                sp = [int(x), int(y), int(z), int(w)]
                if not res and sum(sp) <= 2:
                    print(int(x), int(y), int(z), int(w), int(res))
