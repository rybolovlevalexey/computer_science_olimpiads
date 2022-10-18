import random
sp = set()
for i in range(5):
    for j in range(5):
        if i == 2 and j == 2:
            print('  0', end='')
        else:
            num = str(random.randint(1, 75))
            while num not in sp:
                num = str(random.randint(1, 75))
            sp.add(num)
            print(' ' * (3 - len(num)) + num, end='')
    print()
