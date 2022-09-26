import itertools
def primes():
    def is_prost(x):
        for d in range(2, x // 2 + 1):
            if x % d == 0:
                return False
        return True
    num = 2
    while True:
        if is_prost(num) or num == 2 or num == 3:
            yield num
        num += 1

print(list(itertools.takewhile(lambda x : x <= 40, primes())))