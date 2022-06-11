file = open('Безымянный.txt', 'r')
sp = file.read().strip().split('\n')
numbers = list()
for line in sp:
    line = map(float, line.split())
    for num in line:
        numbers.append(num)
sr = round(sum(numbers) / len(numbers), 1)
mn = min(numbers) * 2
cnt = 0
for num in numbers:
    if mn < num < sr:
        cnt += 1
print(cnt)
