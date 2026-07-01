import os

def fix_typo(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix the typo in the hero headline
    content = content.replace("Marketing &amp;<br />\n        Marketing Agency.", "Marketing<br />\n        Agency.")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

fix_typo('build_index.py')
