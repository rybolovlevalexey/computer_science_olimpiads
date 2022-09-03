n = int(input())
sp = list(map(int, input().split()))
mx = max(sp)
print(max(filter(lambda x: x != mx, sp)))