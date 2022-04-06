ans = 0
flag = False
for elem in range(1098, 13765 + 1):
    if elem % 2 == 0 and elem % 7 != 0 and elem % 11 != 0 and elem % 13 != 0 and elem % 23 != 0:
        ans += 1
        if not flag:
            flag = True
            print(elem)
print(ans)