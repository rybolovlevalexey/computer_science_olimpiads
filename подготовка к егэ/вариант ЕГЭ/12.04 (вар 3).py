x = int(input())
q = 6
l = 0
while x >= q:
    l += 1
    x = x - q
M = x
if M < l:
    M = l
    l = x
print(l)
print(M)