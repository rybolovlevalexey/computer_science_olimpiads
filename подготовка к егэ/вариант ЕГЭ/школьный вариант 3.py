def is_prost(x):
    for d in range(2, x // 2 + 1):
        if x % d == 0:
            return False
    return True


for num in range(152346, 957812 + 1):
    if int(num ** 0.25) == num ** 0.25 and is_prost(int(num**0.25)):
        print(num, int((num ** 0.25)**3))
