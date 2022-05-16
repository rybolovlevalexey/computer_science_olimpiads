deyst = {1: 1, 2: 5}
results = set()

for i1 in [1, 2, 3]:
    for i2 in [1, 2, 3]:
        for i3 in [1, 2, 3]:
            for i4 in [1, 2, 3]:
                for i5 in [1, 2, 3]:
                    for i6 in [1, 2, 3]:
                        for i7 in [1, 2, 3]:
                            num = 1
                            if i1 in [1, 2]:
                                num += deyst[i1]
                            else:
                                num *= 3
                            if i2 in [1, 2]:
                                num += deyst[i2]
                            else:
                                num *= 3
                            if i3 in [1, 2]:
                                num += deyst[i3]
                            else:
                                num *= 3
                            if i4 in [1, 2]:
                                num += deyst[i4]
                            else:
                                num *= 3
                            if i5 in [1, 2]:
                                num += deyst[i5]
                            else:
                                num *= 3
                            if i6 in [1, 2]:
                                num += deyst[i6]
                            else:
                                num *= 3
                            if i7 in [1, 2]:
                                num += deyst[i7]
                            else:
                                num *= 3
                            results.add(num)
print(len(results))
print(results)