first = set(input().split())
second = set(input().split())
third = set(input().split())
print(*sorted(map(int, (third - first) & (third - second))))