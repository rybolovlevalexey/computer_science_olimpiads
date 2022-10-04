n, m = map(int, input().split())
sp1 = list()
sp2 = list()
for i in range(n):
    line = list(map(int, input().split()))
    sp1.append(line)
input()
for i in range(n):
    j = 0
    for elem in map(int, input().split()):
        print(elem + sp1[i][j], end=" ")
        j += 1
    print()