cnt = 0
for num in range(10**6, 10**7):
    if sum(map(int, list(str(num)))) <= 47:
        cnt += 1
print(cnt)