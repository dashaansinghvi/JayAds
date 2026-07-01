import os

def build_single_page():
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>JayAds | B2B White-Label Production Crew</title>
  <meta name="description" content="JayAds is the silent execution engine for agencies. We provide white-label production, editing, and shooting for high-profile clients." />
  
  <link rel="stylesheet" href="styles.css" />
  
  <style>
    /* 
      ====================================================
      INTERMENTALIST-INSPIRED SINGLE PAGE LAYOUT CSS 
      ====================================================
    */
    
    html {
      scroll-behavior: smooth;
    }
    
    /* NAVIGATION OVERRIDES */
    .site-header {
      background: rgba(30, 41, 59, 0.4) !important;
      backdrop-filter: blur(24px) saturate(180%) !important;
      -webkit-backdrop-filter: blur(24px) saturate(180%) !important;
      border-bottom: 1px solid rgba(255, 255, 255, 0.06) !important;
    }
    
    .nav-links {
      display: flex;
      gap: 2rem;
    }
    
    .nav-links a {
      font-size: 0.9rem;
      font-weight: 500;
      letter-spacing: 1px;
      text-transform: uppercase;
      opacity: 0.8;
      transition: opacity 0.3s;
    }
    .nav-links a:hover { opacity: 1; color: var(--accent-gold); }
    
    /* EDITORIAL HERO SECTION */
    #home {
      position: relative;
      min-height: 100vh;
      display: flex;
      align-items: center;
      padding-top: 80px;
      overflow: hidden;
    }
    
    .hero-editorial-wrap {
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 100%;
      max-width: var(--container-max);
      margin: 0 auto;
      padding: 0 var(--section-px);
      position: relative;
      z-index: 10;
    }
    
    .hero-editorial-text {
      flex: 1;
      max-width: 700px;
    }
    
    .hero-editorial-title {
      font-size: clamp(3rem, 7vw, 6rem);
      line-height: 1.05;
      font-weight: 800;
      letter-spacing: -1px;
      margin-bottom: 1.5rem;
      background: linear-gradient(135deg, #ffffff 0%, var(--accent-gold) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }
    
    .hero-editorial-title .accent-word {
      font-style: italic;
      font-weight: 400;
      color: transparent;
      -webkit-text-stroke: 1px var(--accent-gold);
    }
    
    .hero-editorial-sub {
      font-size: 1.25rem;
      line-height: 1.6;
      opacity: 0.8;
      max-width: 500px;
      margin-bottom: 2.5rem;
    }
    
    .hero-editorial-image {
      flex: 1;
      display: flex;
      justify-content: flex-end;
      opacity: 0.8;
    }
    
    .hero-editorial-image img {
      width: 100%;
      max-width: 500px;
      height: auto;
      object-fit: contain;
      filter: grayscale(100%) contrast(1.2);
      border-radius: 12px;
    }
    
    /* DRAMATIC STATS BAR */
    #stats {
      background: #0f1523;
      padding: 4rem 0;
      border-top: 1px solid rgba(255,255,255,0.05);
      border-bottom: 1px solid rgba(255,255,255,0.05);
    }
    
    .stats-grid {
      display: grid;
      grid-template-columns: repeat(4, 1px) /* Wait, 4 columns */;
      grid-template-columns: repeat(4, 1fr);
      gap: 2rem;
      max-width: var(--container-max);
      margin: 0 auto;
      padding: 0 var(--section-px);
      text-align: center;
    }
    
    .stat-number {
      font-size: 3.5rem;
      font-weight: 700;
      color: var(--accent-gold);
      margin-bottom: 0.5rem;
      font-variant-numeric: tabular-nums;
    }
    
    .stat-label {
      font-size: 0.9rem;
      text-transform: uppercase;
      letter-spacing: 2px;
      opacity: 0.6;
    }
    
    /* JOURNEY / ABOUT (Sticky Layout) */
    #about {
      padding: 8rem 0;
      position: relative;
    }
    
    .journey-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 4rem;
      max-width: var(--container-max);
      margin: 0 auto;
      padding: 0 var(--section-px);
    }
    
    .journey-sticky {
      position: sticky;
      top: 150px;
      height: fit-content;
    }
    
    .journey-sticky h2 {
      font-size: 3.5rem;
      line-height: 1.1;
      margin-top: 1rem;
    }
    
    .journey-body p {
      font-size: 1.25rem;
      line-height: 1.8;
      margin-bottom: 1.5rem;
      opacity: 0.8;
    }
    
    /* RESPONSIVE */
    @media(max-width: 900px) {
      .hero-editorial-wrap, .journey-grid { grid-template-columns: 1fr; }
      .stats-grid { grid-template-columns: 1fr 1fr; }
      .hero-editorial-image { justify-content: center; margin-top: 3rem; }
      .nav-links { display: none; } /* Handle mobile menu separately */
    }
  </style>
</head>
<body>

  <!-- UI Interactions DOM -->
  <div class="custom-cursor-dot" id="cursor-dot"></div>
  <div class="custom-cursor-halo" id="cursor-halo"></div>
  <div class="page-transition-overlay" id="page-transition"></div>

  <!-- NAVIGATION -->
  <header class="site-header">
    <div class="header-inner">
      <a href="#home" class="logo">JayAds</a>
      <ul class="nav-links">
        <li><a href="#home">Home</a></li>
        <li><a href="#about">About Us</a></li>
        <li><a href="#services">Capabilities</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <a href="#contact" class="btn-primary" style="padding: 10px 24px;">Book Team</a>
    </div>
  </header>

  <!-- HERO SECTION -->
  <section id="home">
    <div class="hero-editorial-wrap">
      <div class="hero-editorial-text">
        <h1 class="hero-editorial-title">
          The Silent <span class="accent-word">Engine</span><br />
          Behind The Best Campaigns.
        </h1>
        <p class="hero-editorial-sub">
          We are the dedicated, white-label production &amp; editing crew for agencies and high-profile managers. You handle the client, we handle the execution.
        </p>
        <a href="#about" class="btn-secondary" style="margin-right:1rem;">Our Model</a>
        <a href="#services" class="btn-primary">View Capabilities</a>
      </div>
      
      <!-- Optional Hero Visual Placeholder -->
      <div class="hero-editorial-image">
        <!-- Replaced with abstract CSS geometry for now instead of a broken image link -->
        <div style="width: 400px; height: 500px; background: linear-gradient(to top right, rgba(229, 157, 44, 0.2), transparent); border: 1px solid rgba(229,157,44,0.3); border-radius: 24px; display:flex; align-items:center; justify-content:center;">
          <p style="opacity:0.5; font-family:monospace; text-align:center;">[ Production Reel <br/> Placeholder ]</p>
        </div>
      </div>
    </div>
  </section>

  <!-- STATS BAR -->
  <section id="stats">
    <div class="stats-grid">
      <div>
        <div class="stat-number">400+</div>
        <div class="stat-label">Projects Delivered</div>
      </div>
      <div>
        <div class="stat-number">45+</div>
        <div class="stat-label">Agencies Partnered With</div>
      </div>
      <div>
        <div class="stat-number">8,000+</div>
        <div class="stat-label">Hours of Content</div>
      </div>
      <div>
        <div class="stat-number">100%</div>
        <div class="stat-label">White-Labeled</div>
      </div>
    </div>
  </section>

  <!-- JOURNEY / ABOUT -->
  <section id="about">
    <div class="journey-grid">
      <div class="journey-sticky">
        <span class="badge-tag">B2B EXECUTION</span>
        <h2>We stay behind the scenes.<br><span style="color:var(--accent-gold);">You take the credit.</span></h2>
      </div>
      <div class="journey-body">
        <p>Founded on the premise that executing high-end production is fundamentally different from client management, <strong>JayAds</strong> was built specifically for agencies, PR firms, and talent managers.</p>
        
        <p>We know that as an agency, your most valuable asset is your client relationship. Building an in-house shooting and editing team is expensive, volatile, and deeply time-consuming.</p>
        
        <p>That is exactly where we step in. We act as your plug-and-play, invisible production department. From on-ground camera crews and lighting to high-end post-production, VFX, and color grading, we execute the entire project seamlessly under your banner.</p>
        
        <p><strong>We never contact your clients directly.</strong> We do not compete with you. We are simply the raw execution engine that allows you to confidently pitch massive campaigns knowing you have a world-class production crew on standby.</p>
        
        <p>Over the years, we have quietly produced the assets behind some of the most visible influencer campaigns and corporate films, completely white-labeled. That is our power.</p>
      </div>
    </div>
  </section>

  <!-- SERVICES / CAPABILITIES -->
  <section id="services" style="padding: 6rem 0; background: #0b0f19;">
    <div style="max-width: var(--container-max); margin: 0 auto; padding: 0 var(--section-px);">
      <div style="margin-bottom: 4rem;">
        <span class="badge-tag">OUR ARSENAL</span>
        <h2 style="font-size: 3.5rem; margin-top: 1rem;">Full-Scale Production.</h2>
      </div>
      
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
        
        <!-- Service 1 -->
        <div class="service-detail-block" style="padding: 3rem; background: rgba(255,255,255,0.02); border-radius: 16px;">
          <h3 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--accent-gold);">On-Ground Shooting</h3>
          <p style="opacity: 0.8; margin-bottom: 1.5rem;">We deploy fully equipped camera crews, lighting technicians, and sound engineers to capture high-end footage for your campaigns. Whether it's a studio shoot or a live event, we handle the logistics.</p>
          <ul style="opacity: 0.7; font-size: 0.9rem; margin-left: 1rem; list-style-type: square;">
            <li>Director of Photography (DoP)</li>
            <li>Lighting & Gaffer Crew</li>
            <li>Drone & Aerial Footage</li>
          </ul>
        </div>

        <!-- Service 2 -->
        <div class="service-detail-block" style="padding: 3rem; background: rgba(255,255,255,0.02); border-radius: 16px;">
          <h3 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--accent-gold);">Post-Production & Editing</h3>
          <p style="opacity: 0.8; margin-bottom: 1.5rem;">Raw footage is nothing without rhythm. Our editing bays process terabytes of data to deliver polished, narrative-driven content optimized for both cinema and social platforms.</p>
          <ul style="opacity: 0.7; font-size: 0.9rem; margin-left: 1rem; list-style-type: square;">
            <li>Narrative & Offline Editing</li>
            <li>Advanced Color Grading</li>
            <li>Multi-Format Exporting (9:16, 16:9)</li>
          </ul>
        </div>

        <!-- Service 3 -->
        <div class="service-detail-block" style="padding: 3rem; background: rgba(255,255,255,0.02); border-radius: 16px;">
          <h3 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--accent-gold);">VFX & Motion Graphics</h3>
          <p style="opacity: 0.8; margin-bottom: 1.5rem;">We elevate standard footage with high-end 2D/3D motion graphics, text tracking, and visual effects to ensure your client's deliverables look exceptionally premium.</p>
          <ul style="opacity: 0.7; font-size: 0.9rem; margin-left: 1rem; list-style-type: square;">
            <li>3D Product Integration</li>
            <li>Cleanups & Object Removal</li>
            <li>Dynamic Typography</li>
          </ul>
        </div>
        
      </div>
    </div>
  </section>

  <!-- CONTACT / CTA -->
  <section id="contact" style="padding: 10rem 0; text-align: center; border-top: 1px solid rgba(255,255,255,0.05);">
    <div style="max-width: 600px; margin: 0 auto; padding: 0 var(--section-px);">
      <h2 style="font-size: 4rem; line-height: 1; margin-bottom: 2rem;">Let's build your<br />production pipeline.</h2>
      <p style="font-size: 1.25rem; opacity: 0.8; margin-bottom: 3rem;">Ready to scale your agency without the overhead of an in-house crew? Let's discuss a partnership.</p>
      <a href="mailto:hello@jayads.com" class="btn-primary" style="padding: 1rem 3rem; font-size: 1.1rem;">Contact Us</a>
    </div>
  </section>

  <!-- Scripts -->
  <script src="ui_interactions.js"></script>

</body>
</html>
"""
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

build_single_page()
