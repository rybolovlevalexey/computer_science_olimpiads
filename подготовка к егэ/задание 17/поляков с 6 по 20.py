ans = 0
flag = True
for num in range(1200, 11200 + 1):
    if num % 5 == 0 and num % 7 != 0 and num % 13 != 0 and num % 17 != 0 and num % 19 != 0:
        ans += 1
        if flag:
            flag = False
            print(num)
print(ans)