for n in range(2, 50):
    cnt = 0
    num1 = num2 = 338
    while num1 > 0:
        cnt += 1
        num1 //= n
    if num2 % n == 2 and cnt == 3:
        print(n)
