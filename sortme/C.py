n = int(input())
if n % 60 == 0:
    ans_money = n // 60 * 440
    ans = ans_money // 440
    print(ans)
else:
    spisok = {1: [], 2: [], 3: []}
    first = (n // 60 + 1) * 440
    spisok[1] = [n // 60 + 1, 0, 0]
    second = (n // 60) * 440
    spisok[2] = [n // 60, 0, 0]
    third = (n // 60) * 440
    spisok[3] = [n // 60, 0, 0]
    n2 = n - (n // 60 * 60)
    if n2 % 10 == 0:
        second += n2 // 10 * 125
        spisok[2][1] = n2 // 10
        spisok[3][1] = n2 // 10
        third += n2 // 10 * 125
    else:
        second += (n2 // 10 + 1) * 125
        spisok[2][1] = n2 // 10 + 1
        third += (n2 // 10) * 125
        spisok[2][1] = n2 // 10
        n3 = n2 - (n2 // 10 * 10)
        third += n3 * 15
        spisok[2][2] = n3
    minimum = min(first, second, third)
    if minimum == first:
        print(spisok[1])
    elif minimum == second:
        print(spisok[2])
    else:
        print(spisok[3])
