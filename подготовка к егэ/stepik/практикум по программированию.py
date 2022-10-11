first = set(input().split())
second = set(input().split())
third = set(input().split())
print(*sorted(map(int, first & second - third))[::-1])