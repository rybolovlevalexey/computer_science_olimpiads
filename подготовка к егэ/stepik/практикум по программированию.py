first = set(input().split())
second = set(input().split())
third = set(input().split())
al = first | second | third
ans = list()
for elem in al:
    cnt = 0
    if elem in first:
        cnt += 1
    if elem in second:
        cnt += 1
    if elem in third:
        cnt += 1
    if cnt <= 2:
        ans.append(elem)
print(*sorted(map(int, ans)))