ans = 0
flag = True
for num in range(200, 9120 + 1):
    if num % 8 == 0 and num % 7 != 0 and num % 11 != 0 and num % 17 != 0 and num % 19 != 0:
        ans += 1
        if flag:
            flag = False
            print(num)
print(ans)