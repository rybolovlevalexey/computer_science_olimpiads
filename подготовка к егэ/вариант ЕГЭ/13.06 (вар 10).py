print('x y z w res')
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            for w in [True, False]:
                res = x and not y and (not z or w)
                if res:
                    print(int(x), int(y), int(z), int(w), int(res))
