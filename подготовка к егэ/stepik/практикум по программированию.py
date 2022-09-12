school = dict()
for _ in range(int(input())):
    family = input()
    name = input()
    clas = input()
    bdate = input()
    if clas in school:
        school[clas] += [family + " " + name + " " + bdate]
    else:
        school[clas] = [family + " " + name + " " + bdate]
for key in sorted(school.keys()):
    oneclass = school[key]
    for i in range(len(oneclass) - 1):
        for j in range(i, len(oneclass) - 1):
            if oneclass[j] > oneclass[j + 1]:
                oneclass[j], oneclass[j + 1] = oneclass[j + 1], oneclass[j]
    for elem in oneclass:
        print(key + " " + elem)