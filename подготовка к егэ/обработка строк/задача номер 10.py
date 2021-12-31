file = open('24-s1 (1).txt', 'r')
sp = file.read().strip().split('\n')
ans_count = 0
for elem in sp:
    if elem.count('K') > elem.count('U'):
        ans_count += 1
print(ans_count)