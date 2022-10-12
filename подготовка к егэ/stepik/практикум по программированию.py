st1 = input()
st2 = input()
if len(st1) == len(st2):
    letters = dict()
    for i in range(len(st1)):
        if st1[i] in letters:
            letters[i] += 1
        else:
            letters[i] = 1
        if st2[i] in letters:
            letters[i] -= 1
        else:
            letters[i] = -1
    flag = True
    for value in letters.values():
        if value != 0:
            flag = False
    if flag:
        print('YES')
    else:
        print('NO')
else:
    print('NO')