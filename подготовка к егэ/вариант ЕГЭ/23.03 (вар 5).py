def is_prost(x):
    for d in range(2, x // 2 + 2):
        if x % d == 0:
            return False
    return True


cnt = 1
for num in range(2422000, 2422080 + 1):
    if is_prost(num):
        print(cnt, num)
        cnt += 1
