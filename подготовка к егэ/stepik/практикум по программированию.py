st = input().split()
n = int(input())
ans_d = dict()
for i in range(n):
    ans_d[i] = list()
for i in range(len(st)):
    ans_d[i % n].append(st[i])
print(list(value for value in ans_d.values()))