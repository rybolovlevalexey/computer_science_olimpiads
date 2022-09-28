n = int(input())
ans = dict()
for i in range(n):
    st = input()
    ans[i] = st
for i in range(n - 1, -1, -1):
    print(ans[i])