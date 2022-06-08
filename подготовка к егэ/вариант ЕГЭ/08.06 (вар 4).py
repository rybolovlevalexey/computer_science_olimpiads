#12345?7?8
for i1 in range(0, 10):
    for i2 in range(0, 10):
        st = '12345' + str(i1) + '7' + str(i2) + '8'
        num = int(st)
        if num < 10**9 and num % 23 == 0:
            print(num, num // 23)