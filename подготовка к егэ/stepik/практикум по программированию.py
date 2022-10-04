n = int(input())
start = 0
plus = True
for i in range(n):
    num = start
    for j in range(n):
        print(num, end=' ')
        if num == 0 and not plus:
            plus = True
        if plus:
            num += 1
        else:
            num -= 1
    plus = False
    start += 1
    print()
