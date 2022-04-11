numbers = list()
max_sum = 0
cnt = 0
for _ in range(10000):
    numbers.append(int(input()))
print('ok')
for i in range(10000):
    for j in range(i + 1, 10000):
        if numbers[i] * numbers[j] % 34 != 0:
            cnt += 1
            if numbers[i] + numbers[j] > max_sum:
                max_sum = numbers[i] + numbers[j]
print(cnt, max_sum)
