import os

# 1. Fix ui_interactions.js by removing the Stagger text logic which breaks inner HTML
def fix_js():
    with open('ui_interactions.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove the text stagger block
    stagger_marker = "// TEXT STAGGER (Stagger reveal for specific headings)"
    if stagger_marker in content:
        content = content[:content.find(stagger_marker)]
        
    with open('ui_interactions.js', 'w', encoding='utf-8') as f:
        f.write(content)

# 2. Fix the HTML generation scripts by removing stagger-reveal class
def remove_stagger_class(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('class="hero-headline stagger-reveal"', 'class="hero-headline"')
    content = content.replace('class="section-heading stagger-reveal"', 'class="section-heading"')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

fix_js()
remove_stagger_class('build_index.py')
remove_stagger_class('build_pages.py')
