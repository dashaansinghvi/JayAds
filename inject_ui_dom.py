import os

dom_injection = """
  <!-- UI Interactions DOM -->
  <div class="custom-cursor-dot" id="cursor-dot"></div>
  <div class="custom-cursor-halo" id="cursor-halo"></div>
  <div class="page-transition-overlay" id="page-transition"></div>
  <script src="ui_interactions.js"></script>
</body>"""

def inject_dom(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "ui_interactions.js" not in content:
        content = content.replace("</body>", dom_injection)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

inject_dom('build_index.py')
inject_dom('build_pages.py')
