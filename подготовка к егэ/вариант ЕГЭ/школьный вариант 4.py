print('a b c res')
for a in [True, False]:
    for b in [True, False]:
        for c in [True, False]:
            res = not a or (b and not c)
            print(int(a), int(b), int(c), int(res))
