a = int(input())
b = int(input())
ans = 0
while a >= b:
    ans += 1
    a -= b
print(ans)