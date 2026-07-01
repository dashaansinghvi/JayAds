import os

def build_clone_script():
    # Load the exact HTML of theintermentalist.com
    html_path = r'C:\Users\ADMIN\.gemini\antigravity-ide\brain\2ec4cb10-5ff0-4b55-bf3d-dc54d7454239\intermentalist.html'
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replacements for JayAds B2B Production House
    replacements = {
        # Meta & Header
        "The InterMentalist - South India's top influencer marketing agency": "JayAds - B2B White-Label Production & Editing Partner",
        "South India's top influencer marketing agency": "The silent execution engine for agencies. We provide white-label production, editing, and shooting.",
        "influencer marketing, south india influencers, south influencers, tamil nadu influencers, telugu influencers": "white label production, b2b video editing, camera crew, agency partner",
        'href="original/theintermentalist.com/images/favicon.ico"': 'href="favicon.ico"',
        "The InterMentalist": "JayAds",
        'src="original_files/InterMentalist_logo_png-01.webp"': 'src="" style="display:none;"', # Hide their logo
        
        # Link JS and CSS correctly
        'href="index.css"': 'href="styles.css"',
        'src="index.js"': 'src="ui_interactions.js"',

        # Hero Section
        'alt="Shivashish Tarkas — Founder, The InterMentalist"': 'alt="JayAds Production Team"',
        'src="original_files/Founder_Photo_nobg.webp"': 'src="https://images.unsplash.com/photo-1601506521937-0121a7fc2a6b?q=80&w=1024&auto=format&fit=crop" style="border-radius: 12px; filter: grayscale(100%);"', # High-end camera crew image
        "South India's <span class=\"accent-word\">Finest</span><br>\n                        Influencer Marketing<br>\n                        Network": "The Silent <span class=\"accent-word\">Engine</span><br>\n                        Behind The Best<br>\n                        Campaigns.",
        "Building influence across South India since before “creator economy” became a buzzword.": "We are the dedicated, white-label production & editing crew for agencies and high-profile managers. You handle the client, we handle the execution.",

        # Stats Section
        '<div class="stat-l">Campaigns Done</div>': '<div class="stat-l">Projects Delivered</div>',
        '<div class="stat-l">Agencies Partnered With</div>': '<div class="stat-l">Agencies Partnered With</div>',
        '<div class="stat-l">Contents Created</div>': '<div class="stat-l">Hours of Content</div>',
        '<div class="stat-l">Brands Done</div>': '<div class="stat-l">White-Labeled</div>',

        # About / Journey
        '<span class="t-label fade">About The Agency</span>': '<span class="t-label fade">B2B EXECUTION</span>',
        'You Have US,<br><span\n                                style="color:var(--blue)">You Have South.</span>': 'We Stay Behind The Scenes,<br><span\n                                style="color:var(--blue)">You Take The Credit.</span>',
        
        "Founded in 2015 with nothing but instinct, intent, and ₹3,500, <strong>The\n                                InterMentalist</strong> has grown into one of South India’s most influential forces in\n                            creator economy of south.": "Founded on the premise that executing high-end production is fundamentally different from client management, <strong>JayAds</strong> was built specifically for agencies, PR firms, and talent managers.",
        "Today, the agency stands at the centre of the South Indian entertainment and creator\n                            ecosystem — working with brands that operate at a national and global scale, while\n                            collaborating with almost every significant voice across the region. From superstars and\n                            film personalities to internet-first creators and emerging digital talent, The\n                            InterMentalist has built deep relationships across every layer of influence.": "We know that as an agency, your most valuable asset is your client relationship. Building an in-house shooting and editing team is expensive, volatile, and deeply time-consuming. That is exactly where we step in.",
        "What sets the agency apart is not just access — but <strong>understanding</strong>. A sharp\n                            grasp of regional culture, audience behaviour, internet trends, and storytelling allows the\n                            team to create campaigns that feel native, not manufactured.": "We act as your plug-and-play, invisible production department. From on-ground camera crews and lighting to high-end post-production, VFX, and color grading, we execute the entire project seamlessly under your banner.",
        "From influencer marketing and digital movie promotions to creator strategy, scripting,\n                            production, and campaign analytics, The InterMentalist operates as a <strong>full-scale\n                                strategic partner</strong> built specifically for South India.": "<strong>We never contact your clients directly.</strong> We do not compete with you. We are simply the raw execution engine that allows you to confidently pitch massive campaigns knowing you have a world-class production crew on standby.",
        "Over the years, the agency has quietly shaped how brands enter and win in the South —\n                            creating systems, processes, and scalable models that have redefined influencer-led\n                            marketing in the region.": "Over the years, we have quietly produced the assets behind some of the most visible influencer campaigns and corporate films, completely white-labeled. That is our power.",
        "At its core lies a rare capability: <em>the power to influence the people who influence\n                                culture</em>. That is what makes The InterMentalist the preferred partner for brands,\n                            studios, and agencies looking to build real impact in South India.": "At our core lies a rare capability: <em>the power to execute flawlessly at scale</em>. That is what makes JayAds the preferred production partner for agencies looking to build real impact without the overhead.",

        # About The Founder section - replace with Services
        "The Founder": "Our Capabilities",
        "Shivashish <br> <span style=\"color:var(--blue)\">Tarkas</span>": "Full-Scale <br> <span style=\"color:var(--blue)\">Production</span>",
        "Founder &amp; CEO — The InterMentalist": "On-Ground & Post-Production",
        "At 21, with just ₹3,500 in hand and no roadmap to follow, Shivashish stepped into\n                            entrepreneurship with nothing except conviction.": "<strong>1. On-Ground Shooting</strong><br>We deploy fully equipped camera crews, lighting technicians, and sound engineers to capture high-end footage for your campaigns. Whether it's a studio shoot or a live event, we handle the logistics.",
        "<strong>No funding. No infrastructure. No industry backing. No business education.</strong>\n                            Just a middle-class boy carrying a vision too big for the room he came from.": "<strong>2. Post-Production & Editing</strong><br>Raw footage is nothing without rhythm. Our editing bays process terabytes of data to deliver polished, narrative-driven content optimized for both cinema and social platforms.",
        "In a world where people trusted experience, pedigree, and privilege — he chose belief. While\n                            most doubted him, dismissed him, or laughed at the audacity of his dreams, he kept building\n                            quietly, relentlessly, and without shortcuts.": "<strong>3. VFX & Motion Graphics</strong><br>We elevate standard footage with high-end 2D/3D motion graphics, text tracking, and visual effects to ensure your client's deliverables look exceptionally premium.",
        "What began as a one-man pursuit driven by instinct and obsession has today evolved into one\n                            of South India’s most influential and result-driven marketing forces.": "",
        "But the story was never about money. It was about perspective — about understanding people\n                            before platforms did, and recognising the power of influence before the industry realised\n                            its value.": "",
        "Today, Shivashish stands at the intersection of brands, cinema, creators, and culture —\n                            leading an agency that has helped shape the South Indian creator ecosystem from the ground\n                            up.": "",
        "His journey is proof that you do not need perfect conditions to build something powerful.\n                            Sometimes, all it takes is the <strong>courage to start</strong> before the world gives you\n                            permission.": "",
        
        # Adjust founder image to services image
        'alt="Shivashish Tarkas, Founder of The InterMentalist"': 'alt="JayAds Capabilities"',
        'src="original_files/01.webp"': 'src="https://images.unsplash.com/photo-1574717024453-354056aaddfa?q=80&w=985&auto=format&fit=crop" style="border-radius: 12px; filter: grayscale(100%);"', # Editing bay image
        
        # Portfolio Section
        "Creators <br>We've Shaped": "Campaigns <br>We've Produced",
        "See All Creators": "See All Work",

        # Clients Section
        "Brands <br>That Trust Us": "Agencies <br>That Trust Us",
        "See All Brands": "See All Partners",

        # Contact Section
        "Are you ready to grow?": "Let's build your production pipeline.",
        "Ready to scale your brand with South India’s top influencers? Let’s create campaigns that people actually care about.": "Ready to scale your agency without the overhead of an in-house crew? Let's discuss a partnership.",
        
        # Footer
        "© 2026 The InterMentalist. All rights reserved.": "© 2026 JayAds. All rights reserved.",
        "By Uniquecrew": ""
    }

    for old, new in replacements.items():
        html = html.replace(old, new)

    # Escape triple quotes and backslashes for python script generation
    html = html.replace('\\', '\\\\')
    
    script_content = f'''import os

def build_index():
    html = """{html}"""
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

build_index()
'''
    with open('build_index.py', 'w', encoding='utf-8') as f:
        f.write(script_content)

build_clone_script()
