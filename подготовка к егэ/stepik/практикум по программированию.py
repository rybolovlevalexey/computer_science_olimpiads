sp = list(map(int, input().split()))
sp = sorted(sp, key=lambda x: sum(map(int, list(str(x)))))
print(*sp)