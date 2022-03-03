flag = True
for s in range(1, 80):
    st1 = [[6, s + 3], [6 + 3, s], [6 * 2, s], [6, s * 2]]
    for elem in st1:
        if sum(elem) >= 86:
            flag = False
    if not flag:
        break
    st2 = list()
    for elem in st1:
        el = elem[::]
        el[0] += 3
        st2.append(el)
        el = elem[::]
        el[1] += 3
        st2.append(el)
        el = elem[::]
        el[0] *= 2
        st2.append(el)
        el = elem[::]
        el[1] *= 2
        st2.append(el)
    for elem in st1:
        if sum(elem) >= 86:
            flag = False
    if not flag:
        break
    for elem in st2:
        a, b = elem
        if a + b + 3 >= 86 or a * 2 + b >= 86 or a + b * 2 >= 86:
            print(s)
            break
