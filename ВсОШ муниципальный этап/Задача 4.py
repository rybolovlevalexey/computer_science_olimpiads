n = int(input())  # количество поселений
po = input().split()  # вместимость поселений
posel = dict()
for i in range(len(po)):
    posel[i] = int(po[i])
m = int(input())  # количество рейсов
for _ in range(m):
    rashod = 0
    x, k = map(int, input().split())  # номер поселения, количество колонистов на посадку
    x -= 1
    while k > 0:
        can_take = posel[x]
        if can_take == 0:
            x += 1
            rashod += k
        elif can_take < k:
            posel[x] = 0
            k -= can_take
            x += 1
            rashod += k
        elif can_take >= k:
            posel[x] -= k
            k = 0
            break
        if x == n:
            x = 0
    print(rashod)
