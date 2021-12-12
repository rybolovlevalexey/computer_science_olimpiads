t = int(input())
answers = dict()
for i in range(t):
    n = int(input())
    sp = map(int, input().split())
    k = 1
    flag = True  # был полит или первый за ход то True, иначе False
    for elem in sp:
        if elem == 0 and not flag:
            k = -1
            break
        elif elem == 0 and flag:
            flag = False
        elif elem == 1 and (not flag or k == 1):
            k += 1
            flag = True
        elif elem == 1 and flag and k != 1:
            k += 5
    print(k)
