def is_prost(x):
    for d in range(2, int(x**0.5) + 1):
        if x % d == 0:
            return False
    return True


cnt = 0
mxdelta = 0
ans = 0
for num in range(238941, 315675 + 1):
    for delit in range(2, int(num**0.5) + 1):
        if num % delit == 0 and delit != num // delit and is_prost(delit) and is_prost(num // delit):
            cnt += 1
            i = delit
            j = num // delit
            if abs(i - j) > mxdelta:
                mxdelta = abs(i - j)
                ans = num
print(cnt, ans)
