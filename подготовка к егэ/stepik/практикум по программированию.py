s = input()
dic = dict()
for elem in s.split():
    if elem in dic:
        dic[elem] += 1
    else:
        dic[elem] = 1
print(sorted([key for key in dic.keys() if max(dic.values()) == dic[key]])[0])