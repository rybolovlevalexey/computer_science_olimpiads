from functools import lru_cache

@lru_cache()
def f(n):
    if n > 2:
        return f(n - 1) + g(n - 2)
    return n + 1
@lru_cache()
def g(n):
    if n > 2:
        return g(n - 1) + f(n - 2)
    return n


print(g(77))