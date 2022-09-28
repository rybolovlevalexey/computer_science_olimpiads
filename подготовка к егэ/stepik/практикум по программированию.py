st = input().split()
ans = list()
sp = list()
for elem in st:
    if len(sp) == 0:
        sp.append(elem)
    else:
        if sp[-1] == elem:
            sp.append(elem)
        else:
            ans.append(sp)
            sp = [elem]
ans.append(sp)
print(ans)