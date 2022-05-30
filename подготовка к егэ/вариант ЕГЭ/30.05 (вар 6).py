print('x y z w result')
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            for w in [True, False]:
                res = (((x and not y) or (not w or z)) == (z == x))
                x, y, z, w = int(x), int(y), int(z), int(w)
                s = sum([x, y, z, w])
                if res and s != 4 and s != 0 and s != 1 and x != z:
                    print(x, y, z, w, int(res))
