for num in range(100000, 1, -1):
    x = num
    a = 0
    b = 1
    while x > 0:
        a += 1
        b = b + (x % 100)
        x = x // 10
    if a == 4 and b == 153:
        print(num)
        break
