st = input()
sp = list(map(int, st.split()))
if len(set(sp)) == 1:
    print('Шулер')
else:
    flag = True
    sp = sorted(sp)
    mn = set(sp)
    for elem in mn:
        if sp.count(elem) == 4:
            print('Каре')
            flag = False
    if len(mn) == 2 and flag:
        if sp.count(list(mn)[0]) == 3 and sp.count(list(mn)[1]) == 2 or sp.count(list(mn)[0]) == 2 and sp.count(list(mn)[1]) == 3:
            print('Фулл Хаус')
            flag = False
    if len(mn) == 5 and flag:
        prsp = [sp[1] - sp[0], sp[2] - sp[1], sp[3] - sp[2], sp[4] - sp[3]]
        if len(set(prsp)) == 1 and list(set(prsp))[0] == 1:
            print('Стрит')
            flag = False
    if len(mn) == 3 and flag:
        for elem in mn:
            if sp.count(elem) == 3:
                print('Сет')
                flag = False
    if len(mn) == 3 and flag:
        if sp.count(list(mn)[0]) == 2 and sp.count(list(mn)[1]) == 2 or sp.count(list(mn)[0]) == 2 and sp.count(list(mn)[2]) == 2 or sp.count(list(mn)[2]) == 2 and sp.count(list(mn)[1]) == 2:
            print('Две пары')
            flag = False
    if flag:
        for elem in mn:
            if sp.count(elem) == 2:
                print('Пара')
                flag = False
    if flag:
        print('Старшая карта')