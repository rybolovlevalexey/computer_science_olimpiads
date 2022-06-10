for num in range(1000, 2, -1):
    s = num
    n = s
    s = s // 10
    while s + n < 125:
        s = s + n
        n = n - 5
    if len(str(n)) == 2:
        print(num)
