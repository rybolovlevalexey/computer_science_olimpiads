m = int(input())
n = int(input())
math = set()
inf = set()
for i in range(m):
    math.add(input())
for i in range(n):
    inf.add(input())
print(len(math - inf))