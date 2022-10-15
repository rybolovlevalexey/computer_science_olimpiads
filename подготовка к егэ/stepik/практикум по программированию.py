def read_csv():
    file = open('data.csv')
    ans = list()
    keys = file.readline().strip().split(',')
    for line in file.readlines():
        line = line.strip().split(',')
        dline = dict()
        for i in range(len(keys)):
            dline[keys[i]] = line[i]
        ans.append(dline)
    return ans