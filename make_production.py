import os

replacements = {
    # General identity
    "premium digital marketing agency": "premium digital media production house",
    "Performance ads, social commerce, brand strategy &amp; web growth": "Commercial ad films, branded documentaries, post-production &amp; visual effects",
    "Data-driven performance ads, social commerce, brand strategy &amp; web growth": "Commercial ad films, branded documentaries, post-production &amp; visual effects",
    "performance marketing": "media production",
    "Your Elite In-House Growth &amp; Marketing Team": "Your Elite In-House Media Production Team",
    "Data-driven performance campaigns, social commerce, and full-stack brand growth.": "High-end commercial films, branded documentaries, and full-stack post-production.",
    "integrated marketing and ": "integrated production and ",
    "Data-Driven Work.<br />Measurable Results.": "Cinematic Work.<br />World-Class Production.",
    "combine elite creative strategy with ruthless media buying.": "combine elite cinematic creative with flawless post-production.",
    "Performance Ads & Paid Media": "Commercial Ad Films & Video Production",
    "in-house growth department. Continuous campaign management, media buying, and CRO.": "in-house production department. Continuous asset creation, editing, and VFX.",
    "discuss your marketing goals": "discuss your production goals",
    "dedicated, elite marketing": "dedicated, elite production",
    "Full-Stack Marketing": "Full-Stack Production",
    '<span class="badge-tag">PERFORMANCE</span>': '<span class="badge-tag">CINEMATIC</span>',
    "Our rapid campaign workflow ensures": "Our rapid production workflow ensures",
    "across paid media, brand strategy, and growth marketing.": "across ad films, branded documentaries, and social content.",
    "entire creative strategy and performance marketing department": "entire production studio and post-production house",
    "<h3>Marketing</h3>": "<h3>Production</h3>",
    "massive performance ad campaign, a full digital rebrand, or an SEO overhaul": "massive commercial ad campaign, a branded documentary, or social video assets",
    
    # build_pages.py specifics
    "Growth & Marketing": "Video & Production",
    "Digital Marketing Strategy": "Commercial Ad Films",
    "Data-driven growth plans": "High-end broadcast commercials",
    "Organic Growth (SEO)": "Branded Documentaries",
    "Long-term search visibility": "Compelling narrative storytelling",
    "Paid Ads &amp; Performance Marketing": "Commercial Ad Films & Video Production",
    "Paid Ads & Performance Marketing": "Commercial Ad Films & Video Production",
    "Marketing Consulting": "Production Consulting",
    "marketing timeline": "production timeline",
    "marketing and digital growth team": "production and post-production team",
    "We produce highly targeted performance marketing campaigns, optimized Google Ads, and data-driven Meta ads that demand attention. Utilizing deep analytics and continuous A/B testing, we bring scalable growth to your brand.": "We produce broadcast-quality ad commercials, YouTube brand films, and motion graphics that demand attention. Utilizing industry-standard camera packages and custom soundtracks, we bring high-end aesthetics to your brand.",
    "<li> Full Campaign Strategy &amp; Setup</li>": "<li> Full Pre-Production (Scripting, Storyboarding, Casting)</li>",
    "<li> Audience Targeting &amp; Segmentation</li>": "<li> High-end Camera Operators &amp; Direction</li>",
    "<li> Conversion Rate Optimization (CRO)</li>": "<li> Premium Post-Production (Color Grading, Sound Design, VFX)</li>",
    "<li> Multi-platform Execution (Meta, Google, LinkedIn)</li>": "<li> Multi-format Exports (16:9 Cinema, 9:16 Social, 4:5 Feeds)</li>",
    "Social Commerce &amp; Performance Ads": "Social Video & Short-Form Content",
    "Get Performance Creative": "Get Video Assets",
    "Web &amp; Organic Growth (SEO)": "Post-Production & VFX",
    "Full technical SEO audits and website speed optimizations": "Advanced Color Grading (DaVinci Resolve)",
    "Book SEO Growth Audit": "Book Post-Production",
    '<span class="badge-tag">GROWTH</span>': '<span class="badge-tag">VFX</span>',
    "While ads stop running when budgets dry up, organic SEO traffic builds over years.": "We turn raw footage into cinematic masterpieces with industry-standard coloring and visual effects.",
    "Let's Talk<br />Growth.": "Let's Talk<br />Production.",
    
    # build_index.py specifics
    "Your Dedicated <span class=\"accent word-reveal\">Digital</span><br />\n        Marketing &amp;<br />\n        Growth Partner.": "Your Dedicated <span class=\"accent word-reveal\">Media</span><br />\n        Production &amp;<br />\n        Content Partner.",
    "Strategic execution. Measurable growth.<br />\n        Data-driven campaigns designed to scale your brand.": "Cinematic execution. Flawless post-production.<br />\n        World-class video assets designed to elevate your brand.",
    '<div class="float-card-title">Traffic Increased</div>': '<div class="float-card-title">Final Render Complete</div>',
    '<div class="float-card-sub">Organic Search Optimization</div>': '<div class="float-card-sub">4K Delivery • Approved</div>',
    
    # Marquee
    "SEO Growth": "Post-Production",
    "Digital Marketing": "Commercial Films",
    "Paid Advertising": "Motion Graphics",
    "Market Research": "Sound Design",
    
    # Portfolio tags
    "Performance Media": "Commercial Film",
    "SEO • Local Search": "Editing • VFX",
    "SEO Growth": "Branded Content",
}

def apply_replacements(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old_str, new_str in replacements.items():
        content = content.replace(old_str, new_str)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

apply_replacements('build_index.py')
apply_replacements('build_pages.py')
