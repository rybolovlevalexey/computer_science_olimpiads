print('x y z w res')
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            for w in [True, False]:
                res = not w != x or z and not x or y and w and z
                if res == False:
                    print(int(x), int(y), int(z), int(w), int(res))
