m = int(input())
n = int(input())
sp = set()
for i in range(m):
    sp.add(input())
for i in range(n):
    town = input()
    if town in sp:
        print('YES')
    else:
        print('NO')