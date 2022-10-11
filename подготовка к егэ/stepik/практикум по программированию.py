n = int(input())
ans = set()
for i in range(n):
    if i == 0:
        ans = set(input())
    else:
        ans = ans & set(input())
print(*sorted(map(int, ans)) if len(ans) > 0 else '')