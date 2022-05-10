for num in range(100000, 0, -1):
    s = num
    s = s // 10
    n = 1
    while s < 51:
        s += 5
        n = n * 2
    if n == 64:
        print(num)
        break
