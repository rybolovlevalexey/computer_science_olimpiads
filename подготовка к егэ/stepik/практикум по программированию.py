letters = {'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v',
           'м': 'm', 'ч': 'ch', 'г': 'g', 'н': 'n', 'ш': 'sh',
           'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*', 'ё': 'jo', 'р': 'r',
           'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'",
           'з': 'z', 'т': 't', 'э': 'je', 'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j',
           'ф': 'f', 'я': 'ya'}

file = open('cyrillic.txt', encoding='utf-8')
file1 = open('transliteration.txt', 'w', encoding='utf-8')
st = file.read().strip()
ans_sp = list()
for line in st.split('\n'):
    ans = ''
    for elem in line.strip():
        if elem.lower() in letters:
            if elem == elem.upper():
                app = letters[elem.lower()]
                ans += app[0].upper() + app[1:]
            else:
                ans += letters[elem]
        else:
            ans += elem
    ans_sp.append(ans)
file1.write('\n'.join(ans_sp))