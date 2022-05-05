n, k, m = map(int, input().split())
words = list(input().split())
cost = list(map(int, input().split()))
dict_words = dict()

for i in range(k):
    x, *sp = map(int, input().split())
    if len(sp) == 1:
        dict_words[words[sp[0] - 1]] = cost[sp[0] - 1]
    else:
        mncs = None
        for j in sp:
            if mncs is None or mncs > cost[j - 1]:
                mncs = cost[j - 1]
        for j in sp:
            if mncs < cost[j - 1]:
                dict_words[words[j - 1]] = mncs
            else:
                dict_words[words[j - 1]] = cost[j - 1]

st = list(input().split())
ans = 0
for elem in st:
    ans += dict_words[elem]
print(ans)
