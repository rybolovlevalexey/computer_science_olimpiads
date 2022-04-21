def is_prost(x):
    for d in range(2, x // 2 + 1):
        if x % d == 0:
            return False
    return True


cnt = 1
for num in range(3, 200000, 2):
    if is_prost(num):
        cnt += 1
print(cnt)