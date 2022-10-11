from itertools import permutations

num = 53617824
sp = sorted(map(lambda x: ''.join(x), sorted(permutations(str(num)))))
cnt = 0
for elem in sp:
    if elem == str(num):
        cnt += 1
    if 1 <= cnt <= 10:
        print(elem)
        cnt += 1