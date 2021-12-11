print('x y z w')
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            for w in [True, False]:
                res = ((not x or y) == (not y or not w)) or (not z and w)
                if not res and not x == y == z == w:
                    print(int(x), int(y), int(z), int(w), int(res))
