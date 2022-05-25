ans = 0
sp = ['г', 'е', 'р', 'а', 'с', 'и', 'м']
sogl = ['г', 'р', 'с', 'м']
glas = ['е', 'а', 'и']
for i1 in sp:
    for i2 in sp:
        for i3 in sp:
            for i4 in sp:
                for i5 in sp:
                    for i6 in sp:
                        for i7 in sp:
                            st = i1 + i2 + i3 + i4 + i5 + i6 + i7
                            word = set()
                            word.add(i1)
                            word.add(i2)
                            word.add(i3)
                            word.add(i4)
                            word.add(i5)
                            word.add(i6)
                            word.add(i7)
                            pointword = ''
                            if i1 in glas:
                                pointword += '1'
                            else:
                                pointword += '2'

                            if i2 in glas:
                                pointword += '1'
                            else:
                                pointword += '2'

                            if i3 in glas:
                                pointword += '1'
                            else:
                                pointword += '2'

                            if i4 in glas:
                                pointword += '1'
                            else:
                                pointword += '2'

                            if i5 in glas:
                                pointword += '1'
                            else:
                                pointword += '2'

                            if i6 in glas:
                                pointword += '1'
                            else:
                                pointword += '2'

                            if i7 in glas:
                                pointword += '1'
                            else:
                                pointword += '2'
                            if len(word) == 7 and pointword.count('11') == 0 and pointword.count('22') == 0:
                                ans += 1
print(ans)