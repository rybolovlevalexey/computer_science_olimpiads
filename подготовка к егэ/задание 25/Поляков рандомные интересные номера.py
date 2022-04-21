def is_prost(x):
    for d in range(2, x // 2 + 1):
        if x % d == 0:
            return False
    return True


cnt = 0
for num in range(2, 20000):
    if is_prost(num):
        cnt += 1
print(cnt)