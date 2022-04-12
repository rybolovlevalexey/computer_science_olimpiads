number = 500000
cnt = 0
while cnt < 5:
    flag = False
    for d in range(18, number // 2, 10):
        if number % d == 0:
            flag = True
            break
    if flag:
        print(number, d)
        cnt += 1
    number += 2
