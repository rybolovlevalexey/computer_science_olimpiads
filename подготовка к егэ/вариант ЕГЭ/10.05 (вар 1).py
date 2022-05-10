for osn in range(2, 10):
    st = ''
    num = 50
    while num > 0:
        st += str(num % osn)
        num //= osn
    if len(st) == 3:
        print(osn)
        break