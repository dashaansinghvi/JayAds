import re

def purge_growth_buzzwords(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements to strip "Growth" and "Growth Planner" buzzwords
    replacements = {
        "Growth Partner": "Marketing Agency",
        "Growth &amp; Marketing": "Digital Marketing",
        "Marketing &amp;<br />\n        Growth Partner.": "Marketing<br />\n        Agency.",
        "growth plans": "marketing strategies",
        "Organic Growth (SEO)": "Search Engine Optimization (SEO)",
        "marketing and digital growth team": "digital marketing team",
        "Growth Services": "Marketing Services",
        "growth marketing": "digital marketing",
        "SEO Growth": "SEO Services",
        "SEO Growth Audit": "SEO Audit",
        "scalable growth": "scalable results",
        "Let's Talk<br />Growth.": "Let's Talk<br />Marketing.",
        "full-stack brand growth": "full-stack digital marketing",
        "growth department": "marketing department",
        "marketing goals": "marketing goals",
        "Growth & Marketing": "Digital Marketing",
        "Growth Consulting": "Marketing Consulting",
        "In-House Growth": "In-House Marketing",
        "full digital rebrand, or an SEO overhaul": "full digital rebrand, or an SEO campaign",
        '<span class="badge-tag">GROWTH</span>': '<span class="badge-tag">MARKETING</span>',
        "Measurable growth": "Measurable results",
    }

    for old_str, new_str in replacements.items():
        content = content.replace(old_str, new_str)
        
    # Case insensitive regex replace for lingering "growth" not caught above
    # We have to be careful not to replace it inside CSS classes or IDs if possible, but let's do a targeted replace.
    content = content.replace(">Growth<", ">Marketing<")
    content = content.replace(" Growth ", " Marketing ")
    content = content.replace(" growth ", " marketing ")
    content = content.replace("growth.", "marketing.")
    content = content.replace("Growth.", "Marketing.")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

purge_growth_buzzwords('build_index.py')
purge_growth_buzzwords('build_pages.py')
