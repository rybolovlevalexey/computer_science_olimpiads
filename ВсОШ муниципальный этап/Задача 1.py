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
    if len(sp) == 1:
        answer += 1
        sp = []
    elif len(sp) == 2:
        first = sp[0]
        second = sp[1]
        if first + second <= e:
            answer += 1
        else:
            answer += 2
        sp = []
    elif len(sp) == 3:
        first = max(sp)
        third = min(sp)
        second = sum(sp) - first - third
        if first + second <= e and first + third <= e:
            answer += 1
        elif first + second >= e and second + third <= e:
            answer += 2
        elif first + second >= e and second + third >= e:
            answer += 3
    elif len(sp) == 4:
        sp = sorted(sp)[::-1]
        first, second, third, fourth = sp
        if first + second <= e and first + third <= e and first + fourth <= e:
            answer += 1
        elif first + second >= e and first + third <= e and first + fourth <= e:
            answer += 2
        elif first + second >= e and first + third >= e and first + fourth <= e:
            answer += 1
            if second + third <= e:
                answer += 1
            else:
                answer += 2
        else:
            answer += 1
            if second + third <= e and second + fourth <= e:
                answer += 1
            elif second + third >= e and (second + fourth <= e or third + fourth <= e):
                answer += 2
            else:
                answer += 3
    print(answer)