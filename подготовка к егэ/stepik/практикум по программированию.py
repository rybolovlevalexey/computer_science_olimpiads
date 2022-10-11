m = int(input())
n = int(input())
words = dict()
for i in range(n + m):
    st = input()
    if st in words:
        words[st] += 1
    else:
        words[st] = 1
print(len(list(filter(lambda x: words[x] == 1, words.keys()))))