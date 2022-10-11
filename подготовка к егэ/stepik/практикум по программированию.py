first = set(input())
second = set(input())
print('YES' if len(first & second) == len(second) else 'NO')