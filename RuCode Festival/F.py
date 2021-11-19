n = N = int(input())
ans = list()
cnt = 0
ans.append(n)

while n > 1:
    cnt += 1
    if (n - 1) % 4 == 0 and (n - 1) // 4 < n // 4 - 1:
        n -= 1
        ans.append(n)
        n //= 4
        cnt += 1
    elif (n - 1) % 5 == 0 and (n - 1) // 5 < n // 5 - 1:
        n -= 1
        ans.append(n)
        n //= 5
        cnt += 1
    elif n % 4 == 0:
        n //= 4
    elif n % 5 == 0:
        n //= 5
    else:
        n -= 1
    ans.append(n)

ans = ans[::-1]
print(cnt)
print(*ans)
