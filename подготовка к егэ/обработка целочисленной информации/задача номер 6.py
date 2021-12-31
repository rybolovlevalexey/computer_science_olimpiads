count = 0
flag = False
for elem in range(7548, 24658 + 1):
    if elem % 10 != elem % 8 and (elem % 13 == 0 or elem % 15 == 0 or elem % 17 == 0):
        count += 1
        if not flag:
            flag = True
            print(elem)
print(count)