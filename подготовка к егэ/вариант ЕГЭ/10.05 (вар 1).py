def is_prost(y):
    for z in range(2, int(y**0.5)+1):
        if y % z == 0:
            return False
    return True


delit = 0
for num in range(35000000, 40000000 + 1):
    x = num
    while x % 2 == 0:
        x //= 2
    for d in range(3, int(x**0.5) + 1, 2):
        if x % d == 0 and d**4 == x:
            delit = d
            print(num)
            break
        elif x % d == 0 and d**4 != x:
            break
    if num % 100000 == 0:
        print(f'{num} - продолжаем выполнение')
    if delit != 0:
        break