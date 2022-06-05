num = int(input())
def one(x):
    x = bin(x)[2:] + '0'
    return int(x, 2)
def two(x):
    return x - 1

num = one(num)
num = one(num)
num = two(num)
num = one(num)
num = one(num)
num = two(num)
print(num)