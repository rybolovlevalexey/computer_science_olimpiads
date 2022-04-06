ans = 0
flag = False
for elem in range(1325, 15367 + 1):
    if elem % 13 == 0 and elem % 7 != 0 and elem % 17 != 0 and elem % 19 != 0 and elem % 23 != 0:
        ans += 1
        if not flag:
            flag = True
            print(elem)
print(ans)