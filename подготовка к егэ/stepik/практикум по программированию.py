import random
n = int(input())
m = int(input())
elements = list(i for i in range(2, 10))
for i in range(97, 123):
    let = chr(i)
    if let != 'l' and let.upper() != 'I' and let != 'o':
        elements.append(let)
        elements.append(let.upper())
for i in range(n):
    ans = set()
    ans.add(str(random.choice(list(i for i in range(2, 10)))))
    ans.add(random.choice(list(set(elements).difference(list(i for i in range(2, 10))))).lower())
    ans.add(random.choice(list(set(elements).difference(list(i for i in range(2, 10))))).upper())
    random.shuffle(list(ans))
    ans = set(ans)
    while len(ans) < m:
        ans.add(str(random.choice(elements)))
    print(''.join(ans))
