for num in range(-1000, 1000):
    x = num
    a = 0
    b = 1
    while x > 0:
        a = a + 1
        b = b * (x % 10)
        x = x // 10
    if a == 2 and b == 15:
        print(num)
        break