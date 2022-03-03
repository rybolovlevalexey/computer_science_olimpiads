for s in range(1, 58):
    stones = [7, s]
    stones1 = list()
    st1 = [stones[0] + 2, stones[1]]
    st2 = [stones[0], stones[1] + 2]
    st3 = [stones[0] * 2, stones[1]]
    st4 = [stones[0], stones[1] * 2]
    stones1.append(st1)
    stones1.append(st2)
    stones1.append(st3)
    stones1.append(st4)
    for elem in stones1:
        if max(elem) * 2 + min(elem) >= 62:
            print(s)
            break