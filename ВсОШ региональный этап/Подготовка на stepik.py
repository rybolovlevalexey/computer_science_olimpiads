fib = {0: 0, 1: 1}
def func(x):
    if x == 0 or x == 1:
        return x
    elif x >= 2 and x in fib:
        return fib[x]
    else:
        res = func(x - 1) + func(x + 2)
        fib[x] = res
        return res

def fib_mod(n, m):
    mch = func(m)
    nch = func(n)



def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()