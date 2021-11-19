cnt = int(input())
count = 0
maximum = -1
index_maximum = -1
max_dict = dict()

for i in range(cnt):
    req = input()
    if req.startswith("push"):
        money = int(req.split()[1])
        count += 1
        if money > maximum:
            maximum = money
            index_maximum = count
    elif req.startswith("max"):
        print(maximum)
    else:
        pass