for num in range(1000):
    x = num
    a = 0
    b = 0
    while x > 0:
        a = a + 1
        b = b + x % 100
        x = x // 100
    if a == 2 and b == 13:
        print(num)
        break