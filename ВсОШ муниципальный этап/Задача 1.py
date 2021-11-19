a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
sp = [a, b, c, d]
if a == b == c == d == e:
    print(4)
else:
    answer = 0
    if e in sp:
        answer += sp.count(e)
        while e in sp:
            sp.remove(e)
    print(sp, answer)