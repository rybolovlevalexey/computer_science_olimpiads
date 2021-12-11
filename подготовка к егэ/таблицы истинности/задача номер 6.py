print('x y z w')
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            for w in [True, False]:
                res = ((not x or y) == (not y or w)) and z and not x
                if res:
                    print(int(x), int(y), int(z), int(w), int(res))
