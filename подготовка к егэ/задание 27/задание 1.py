file = open('27_B.txt', 'r')
sp = file.read().strip().split('\n')
n = int(sp[0])
del sp[0]
max_sum = 0
min_sum = 0
min_delta = -1
count = 0
for elem in sp:
    first, second = map(int, elem.split())
    delta = abs(first - second)
    if delta == min_delta:
        count += 1
    if (min_delta == -1 or min_delta > delta) and delta != 0 and delta % 2 == 1 and delta > 3:
        min_delta = delta
        count = 1
print(count)
flag = True
for elem in sp:
    first, second = map(int, elem.split())
    delta = abs(first - second)
    if first > second and delta != min_delta:
        max_sum += first
        min_sum += second
    elif first < second and delta != min_delta:
        max_sum += second
        min_sum += first
    elif first > second and delta == min_delta:
        max_sum += first
        min_sum += first
        flag = False
    elif first < second and delta == min_delta:
        max_sum += first
        min_sum += first
        flag = False
print(max_sum - min_sum)
print(min_delta)