sp = list()
for _ in range(10000):
    sp.append(int(input()))
print('ok')
cnt = 0
max_sum = 0
for i in range(10000):
    for j in range(i + 1, 10000):
        if sp[i] * sp[j] % 10 == 0:
            cnt += 1
            if sp[i] + sp[j] > max_sum:
                max_sum = sp[i] + sp[j]
print(cnt, max_sum)
