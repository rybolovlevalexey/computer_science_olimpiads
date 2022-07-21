n = int(input())
num = 1
cnt = 0
ans = list()
while n > 0:
    ans.append(num)
    cnt += 1
    if cnt == num:
        cnt = 0
        num += 1
    n -= 1
print(*ans)
