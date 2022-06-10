for num in range(1000):
    q = 0
    n = num
    for i in range(1, n):
        if n % i == 0:
            q = i
    if q == 17:
        print(num)