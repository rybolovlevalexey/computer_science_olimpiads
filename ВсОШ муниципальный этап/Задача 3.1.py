n, k = map(int, input().split())
food = tuple(map(int, input().split()))
dict_types = dict()
answer = []  # тип блюда, количество съеденных блюд

for i in range(n):
    elem = food[i]
    if elem in dict_types:
        dict_types[elem] += [i]
    else:
        dict_types[elem] = [i]
for key, value in dict_types.items():
    dop_sp = list()
    cnt = 0
    dop_delta = 0
    for i in range(len(value) - 1):
        res = abs(value[i] - value[i + 1])
        dop_sp += [res]
        if res + dop_delta > k:
            cnt += 1
            dop_delta = 0
        else:
            dop_delta = res
    if answer == [] or answer[1] < cnt + 1:
        answer = [key, cnt + 1]
print(*answer)