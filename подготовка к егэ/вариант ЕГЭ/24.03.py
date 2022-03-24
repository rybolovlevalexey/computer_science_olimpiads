print('x y z w result')
for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            for w in [True, False]:
                result = not(w) and z and (not(y) or x)
                if result:
                    print(int(x), int(y), int(z), int(w), int(result))
