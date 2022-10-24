athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
n = int(input())
answer = {4: sorted(athletes, key=lambda x: x[-1]), 3: sorted(athletes, key=lambda x: x[-2]),
          2: sorted(athletes, key=lambda x: x[1]), 1: sorted(athletes, key=lambda x: x[0])}
for elem in answer[n]:
    print(*elem)
