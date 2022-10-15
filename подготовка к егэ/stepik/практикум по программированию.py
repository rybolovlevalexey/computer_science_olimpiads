text = map(lambda x: x.strip(), open('lines.txt').readlines())
print(*filter(lambda x: len(x) == len(max(text, key=len)), text), sep='\n')