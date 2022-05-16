results = set()

for i1 in [1, 2, 3]:
    for i2 in [1, 2, 3]:
        for i3 in [1, 2, 3]:
            for i4 in [1, 2, 3]:
                for i5 in [1, 2, 3]:
                    for i6 in [1, 2, 3]:
                        num = 1
                        if i1 in [1, 2]:
                            num += i1
                        else:
                            num *= 2
                        if i2 in [1, 2]:
                            num += i2
                        else:
                            num *= 2
                        if i3 in [1, 2]:
                            num += i3
                        else:
                            num *= 2
                        if i4 in [1, 2]:
                            num += i4
                        else:
                            num *= 2
                        if i5 in [1, 2]:
                            num += i5
                        else:
                            num *= 2
                        if i6 in [1, 2]:
                            num += i6
                        else:
                            num *= 2

                        results.add(num)
print(len(results))
print(results)
cnt = 0
for elem in results:
    if 34 <= elem <= 59:
        cnt += 1
print(cnt)