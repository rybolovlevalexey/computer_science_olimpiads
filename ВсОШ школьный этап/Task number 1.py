k = int(input())  # номер купе
ans = list()
for i in range(4):
    ans.append(k * 4 - i)
for i in range(2):
    ans.append(44 + 2 * (11 - k) + i + 1)
print(*sorted(ans), sep='\n')
