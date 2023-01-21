from touchtouch import touch
file=r'f:\caminho\nao\existe\bu.txt'
touch(file)

with open(file
,
mode='w', encoding='utf-8') as f:
    f.write('bababa')
