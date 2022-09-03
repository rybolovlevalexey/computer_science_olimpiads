n = int(input())
sp = list(map(int, input().split()))
x = int(input())
cnt = 0
for elem in sp:
    if elem == x:
        cnt += 1
print(cnt)