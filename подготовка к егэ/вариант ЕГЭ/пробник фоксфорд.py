def is_prost(num):
    if num % 2 == 0:
        return False
    for d in range(3, int(num**0.5), 2):
        if num % d == 0:
            return False
    return True


for elem in range(4542345, 4542419 + 1):
    if is_prost(elem):
        print(elem)
