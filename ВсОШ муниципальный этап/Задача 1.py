a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if a == b == c == d == e:
    print(4)
else:
    cnt = 0
    box_size = [e, e, e]
    boxes = list(reversed([a, b, c, d]))
    while len(boxes) > 0:
        delet_index = list()
        for elem in boxes:
            if box_size == [e, e, e]:
                pass