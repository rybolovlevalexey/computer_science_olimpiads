print('x y z w result')
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            for w in [True, False]:
                res = (((x and y) or (y and z)) == ((not x or w) and (not w or z)))
                numbers = [int(x), int(y), int(z), int(w)]
                if res and not x:
                    print(int(x), int(y), int(z), int(w), int(res))