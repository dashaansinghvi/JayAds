import re
js = open('ui_interactions.js', encoding='utf-8').read()
html = open('index.html', encoding='utf-8').read()

ids = re.findall(r"getElementById\('([^']+)'\)", js)
classes = re.findall(r"querySelectorAll\('\.([^']+)'\)", js)
classes += re.findall(r"querySelector\('\.([^']+)'\)", js)

missing = []
for i in ids:
    if i not in html:
        missing.append('#' + i)
for c in classes:
    if c not in html:
        missing.append('.' + c)

print('Missing in HTML:', set(missing))
