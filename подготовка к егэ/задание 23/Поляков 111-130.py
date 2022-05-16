deyst = {1: '+1', 2: '+5', 3: '*3'}
results = set()

for i1 in [1, 2, 3]:
    for i2 in [1, 2, 3]:
        for i3 in [1, 2, 3]:
            for i4 in [1, 2, 3]:
                for i5 in [1, 2, 3]:
                    for i6 in [1, 2, 3]:
                        for i7 in [1, 2, 3]:
                            for i8 in [1, 2, 3]:
                                num = eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval(str(eval('1' + deyst[i1])) + deyst[i2])) + deyst[i3])) + deyst[i4])) + deyst[i5])) + deyst[i6])) + deyst[i7])) + deyst[i8])
                                results.add(num)
print(len(results))
print(results)
cnt = 0
for elem in results:
    if 1000 <= elem <= 1024:
        cnt += 1
        print(elem)
print(cnt)