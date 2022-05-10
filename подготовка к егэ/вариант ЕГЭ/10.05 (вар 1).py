file = open('24 (2).txt', 'r')
sp = file.read().strip().split('\n')

cntg = None
ansst = ''
for i in range(len(sp)):
    elem = sp[i]
    if cntg is None or cntg > elem.count('G'):
        cntg = elem.count('G')
        ansst = elem
print(cntg)

dletters = dict()
for let in ansst:
    if let in dletters:
        dletters[let] += 1
    else:
        dletters[let] = 1
print(dletters)
mxcn = 0
ans = ''
for key in sorted(dletters.keys())[::-1]:
    if dletters[key] > mxcn:
        mxcn = dletters[key]
        ans = key
print(mxcn)
print(ans)
