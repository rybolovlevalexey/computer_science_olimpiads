n, k = map(int, input().split())
food = list(map(int, input().split()))
food_types = len(set(food))
answer = list()  # тип блюда, количество съеденных блюд
for i in range(food_types):
    j = -1
    for num_iter in range(food.count(i + 1)):
        if j == -1:
            j = food.index(i + 1)
        else:
            j = food[j + 1:].index(i + 1)
        cnt = 0
        while j < n:
            if food[j] == i + 1:
                cnt += 1
                j += (k + 1)
            else:
                j += 1
        j = -1
        if cnt > 0:
            if len(answer) == 0 or answer[1] < cnt:
                answer = [i + 1, cnt]
print(*answer)