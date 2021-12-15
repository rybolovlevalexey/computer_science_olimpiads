count = 0
for r in range(1, 1000):
    flag = True
    for a in range(1, 1000):
        for x in range(1, 1000):
            if x & 54 != 0 and x & 45 != 0 or x & a == 0 or x & r == 0:
                pass
            else:
                flag = False
                break
        if not flag:
            break
    if flag:
        print(r)
        count += 1
print()
print(count)