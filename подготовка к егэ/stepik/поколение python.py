ans = 0  # количество счастливых билетов
cnt = int(input())  # количество билетов
for i in range(cnt):
    num = int(input())  # текущий билет
    first = sum(map(int, list(str(num)[:3])))  # сумма первых трёх цифр
    second = sum(map(int, list(str(num)[3:])))  # сумма вторых трёх цифр
    if first == second:
        ans += 1
print(ans)  # вывод количества счастливых билетов
