cnt = 0
first = ['x', 'y', 'z']
second = ['a', 'b', 'c', 'd']
for i1 in first:
    for i2 in first:
        for i3 in second:
            for i4 in second:
                cnt += 1
print(cnt)
