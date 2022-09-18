num = int(input())
sp = list()
for i in range(1, num // 2 + 1):
    if num % i == 0 and i not in sp and (num // i) not in sp:
        print(f"{num} = {i} * {num // i}")