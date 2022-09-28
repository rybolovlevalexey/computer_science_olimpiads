import itertools

st = input()
if len(st) == 0:
    print([[], [st]])
else:
    st = st.split()
    ans = list()
    ans.append([])
    for d in range(1, len(st) + 1):
        line = itertools.permutations(st, d)
        print(list(line))