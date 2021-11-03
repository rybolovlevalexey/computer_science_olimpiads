st = input()
output = ""
for elem in st:
    if elem == "," or elem == ";":
        print('"' + output + '"')
        output = ""
    else:
        output += elem
print('"' + output + '"')