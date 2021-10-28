n = int(input())  # количество высот
k = int(input())  # длина отрезка, k + 1 = количество высот
ans_sp = list()  # стартовая позиция, дельта энергии
sp = list()
ans_dict = dict()  # в списке[0] - дельта энергии, [1] - количество холмов

elem0 = int(input())
for i in range(n - 1):
    elem = int(input())
    sp_for_deleting = list()

    for j in ans_dict.keys():
        if ans_dict[j][1] == k:
            if len(ans_sp) == 0 or ans_dict[j][0] > ans_sp[1]:
                ans_sp = [j, ans_dict[j][0]]
            sp_for_deleting.append(j)
        else:
            if elem0 < elem:
                ans_dict[j][0] += (elem0 - elem)
            else:
                ans_dict[j][0] += abs(elem0 - elem)
            ans_dict[j][1] += 1

    for index in sp_for_deleting:
        ans_dict.pop(index)

    if elem0 < elem:
        ans_dict[i] = [(elem0 - elem), 1]
    else:
        ans_dict[i] = [abs(elem0 - elem), 1]

    elem0 = elem

for key, value in ans_dict.items():
    if value[1] == k and value[0] > ans_sp[1]:
        ans_sp = [key, value[0]]
    if value[1] < k:
        break

print(ans_sp[0] + 1)
