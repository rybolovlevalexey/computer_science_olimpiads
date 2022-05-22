print('x y z w result')
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            for w in [True, False]:
                result = (((x and w) or (w and z)) == ((not z or y) and (not y or x)))
                if result and y and not z:
                    print(int(x), int(y), int(z), int(w), int(result))