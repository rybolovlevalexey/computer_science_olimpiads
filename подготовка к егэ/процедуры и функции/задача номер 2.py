def F(n):
    print("x")
    if n>0:
        print("x")
        G(n-1)
def G(n):
    print("x")
    if n>1:
        print("x")
        F(n-2)
F(8)