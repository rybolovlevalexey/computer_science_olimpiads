m = int(input())
ans = set()
for i in range(m):
    n = int(input())
    lesson = set()
    for j in range(n):
        lesson.add(input())
    if i == 0:
        ans = lesson
    else:
        ans = ans & lesson
print(*sorted(ans), sep='\n')