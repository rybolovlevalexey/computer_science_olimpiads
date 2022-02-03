import json

file = open('muggle_repellent.json', 'r')
output_file = open('muggle_magic.csv', 'w')
output_file.write('name,size,danger,magic,additional\n')
sp = json.load(file)
additional = dict()
name_dict = dict()
i = 0
while i < len(sp):
    elem = sp[i]
    name_dict[elem.get('creature')] = [str(elem.get('size')), str(elem.get('danger')),
                                       str(elem.get('magic'))]
    addi = 100 - elem.get('size') * elem.get('magic') // elem.get('danger')
    if addi < 0:
        addi = 0
    additional[elem.get('creature')] = addi
    i += 1
answer_dict = dict()
for key, value in additional.items():
    if value in answer_dict:
        answer_dict[value] += [key]
    else:
        answer_dict[value] = [key]
for number in sorted(answer_dict.keys(), reverse=True):
    for name in sorted(answer_dict[number]):
        st = name + ',' + ','.join(name_dict[name]) + ',' + str(number) + '\n'
        output_file.write(st)
output_file.close()
