a = int(input())  # цена пирожка с брусникой
b = int(input())  # цена пирожка с черникой
c = int(input())  # цена пирожка с вишней
n = int(input())  # количество дней
pirogok = int(input())  # 1 - брусникой, 2 - черникой, 3 - вишней

ans_sum = (n // 3) * (a + b + c)
n %= 3
while n > 0:
    if pirogok == 1:
        ans_sum += a
        pirogok += 1
    elif pirogok == 2:
        ans_sum += b
        pirogok += 1
    else:
        ans_sum += c
        pirogok = 1
    n -= 1
print(ans_sum)