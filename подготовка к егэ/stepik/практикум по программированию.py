n = int(input())
numbers = dict()
for i in range(n):
    number, name = input().split()
    name = name.lower()
    if name in numbers:
        numbers[name.lower()] += [number]
    else:
        numbers[name.lower()] = [number]
for i in range(int(input())):
    print(*numbers.get(input().lower(), 'абонент не найден'.split()))