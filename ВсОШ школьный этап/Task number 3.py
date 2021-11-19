n = int(input())  # количество чисел
x = int(input())  # искомое число

colvo_before = x - 1

while colvo_before > 0:
    if colvo_before % 2 == 0:
        print(2)
        colvo_before //= 2
        if n % 2 == 0:
            n //= 2
        else:
            n //= 2
            n += 1
    else:
        print(1)
        if colvo_before == 1:
            colvo_before = 0
        else:
            colvo_before //= 2
        n //= 2

while n > 1:
    print(2)
    if n % 2 == 0:
        n //= 2
    else:
        n //= 2
        n += 1
