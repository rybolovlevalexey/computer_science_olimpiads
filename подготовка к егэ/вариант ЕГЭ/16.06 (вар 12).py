for num in range(11, 101, 2):
    x = num
    res = int(str(x % 4) + str(x % 3) + str(x % 2))
    if res == 301:
        print(num)
        break