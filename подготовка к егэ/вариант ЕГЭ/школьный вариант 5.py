print('x y z result')
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            res = (not(x) or z) and (not(y) or x)
            if (int(x) + int(y) + int(z) == 1 and int(res) == 0) or (int(x) + int(y) + int(z) == 2 and int(res == 1)):
                print(int(x), int(y), int(z), int(res))
