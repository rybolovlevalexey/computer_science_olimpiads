n = int(input())
info = dict()
for i in range(n):
    name, thing, cnt = input().split()
    cnt = int(cnt)
    if name not in info:
        info[name] = {thing: cnt}
    else:
        if thing in info[name]:
            info[name][thing] += cnt
        else:
            info[name][thing] = cnt
for name in sorted(info.keys()):
    print(name + ':')
    for key in sorted(info[name].keys()):
        print(key, info[name][key])
