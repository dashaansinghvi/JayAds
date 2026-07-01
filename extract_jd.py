import re

path = r'C:\Users\ADMIN\.gemini\antigravity-ide\brain\2ec4cb10-5ff0-4b55-bf3d-dc54d7454239\.system_generated\steps\912\content.md'
content = open(path, encoding='utf-8', errors='ignore').read()

phones = re.findall(r'[\d]{10}', content)
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)
# Look for address snippets
addr_matches = [m for m in re.findall(r'.{0,60}Anna Nagar.{0,120}', content)]

print('--- PHONES ---')
for p in set(phones):
    if p.startswith('9') or p.startswith('8') or p.startswith('7') or p.startswith('6'):
        print(p)

print('--- EMAILS ---')
for e in set(emails):
    if 'jd' not in e.lower() and 'justdial' not in e.lower():
        print(e)

print('--- ADDRESSES ---')
for a in addr_matches[:10]:
    print(a.replace('\n', ' ').strip())
