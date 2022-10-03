n, m = map(int, input().split())
num = 1
for i in range(n):
    for j in range(m):
        print(str(num) + " " * (3 - len(str(num))), end="")
        num += 1
    print()
