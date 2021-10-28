n = int(input())
st = input().lower()
answer = 0
for i1 in range(n - 1):
    for i2 in range(i1 + 1, n):
        if ord(st[i1]) < ord(st[i2]):
            answer += 1
print(answer)
