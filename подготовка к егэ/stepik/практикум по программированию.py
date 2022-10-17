n = int(input())
mxdl = None
dl = 0
for i in range(n):
    num = int(input())
    if num == 1:
        dl += 1
        if mxdl is None or dl > mxdl:
            mxdl = dl
    else:
        dl = 0
if mxdl is None:
    mxdl = 0
print(mxdl)