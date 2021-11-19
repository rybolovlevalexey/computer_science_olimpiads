n = int(input())
sp1 = sorted(map(int, input().split()))
sp2 = sorted(map(int, input().split()))
answer = 0
for i in range(n):
    answer += abs(sp1[i] - sp2[i])
print(answer)
