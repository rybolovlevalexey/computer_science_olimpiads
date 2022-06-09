ans = set()
for i1 in ['+2', '*3']:
    for i2 in ['+2', '*3']:
        for i3 in ['+2', '*3']:
            num = eval(str(eval(str(eval('2'+i1))+i2))+i3)
            ans.add(num)
print(ans)
print(len(ans))