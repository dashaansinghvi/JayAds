import os

modal_tail = open('modal_code.html', 'r', encoding='utf-8').read()

new_index = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>JayAds | Elite Digital Growth & Production Agency</title>
  <meta name="description" content="JayAds is a premium branding and digital marketing agency based in Chennai. We act as your elite in-house production and growth team." />
  <link rel="stylesheet" href="styles.css" />
</head>
<body class="section-police">
  
  <!-- PRELOADER -->
  <div class="preloader" id="preloader">
    <div class="preloader-inner">
      <div class="preloader-logo">Jay<span class="logo-accent">Ads</span></div>
      <div class="preloader-bar"><div class="preloader-fill"></div></div>
      <div class="preloader-text">Loading Experience</div>
    </div>
  </div>

  <!-- CUSTOM CURSOR -->
  <div class="cursor-dot" id="cursor-dot"></div>
  <div class="cursor-ring" id="cursor-ring"></div>

  <!-- SCROLL PROGRESS -->
  <div class="scroll-progress" id="scroll-progress"></div>

  <!-- ═══════════════════════════════════════════════════ -->
  <!-- HEADER NAVIGATION                                   -->
  <!-- ═══════════════════════════════════════════════════ -->
  <header class="site-header" id="site-header">
    <div class="header-inner">
      <a href="index.html" class="logo">Jay<span class="logo-accent">Ads</span></a>
      <nav class="desktop-nav">
        <ul class="nav-links">
          <li><a href="index.html" class="active" data-section="hero">Home</a></li>
          <li class="nav-item-dropdown">
            <a href="services.html">Services <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m6 9 6 6 6-6"/></svg></a>
            <div class="mega-dropdown">
              <div class="mega-dropdown-inner">
                <div class="mega-col-links">
                  <a href="services.html#adfilms" class="mega-link-item">
                    <span class="mega-link-icon">🎬</span>
                    <div><span class="mega-link-title">Ad Films & Production</span><span class="mega-link-desc">Cinematic brand storytelling</span></div>
                  </a>
                  <a href="services.html#social" class="mega-link-item">
                    <span class="mega-link-icon">⚡</span>
                    <div><span class="mega-link-title">Social Commerce</span><span class="mega-link-desc">High-ROAS paid media</span></div>
                  </a>
                  <a href="services.html#branding" class="mega-link-item">
                    <span class="mega-link-icon">🏆</span>
                    <div><span class="mega-link-title">Brand Identity</span><span class="mega-link-desc">Visual & strategic foundation</span></div>
                  </a>
                  <a href="services.html#organic" class="mega-link-item">
                    <span class="mega-link-icon">✦</span>
                    <div><span class="mega-link-title">Organic Growth</span><span class="mega-link-desc">SEO & content architecture</span></div>
                  </a>
                </div>
                <div class="mega-col-featured">
                  <span class="featured-tag">New Feature</span>
                  <h4>Hyper-Scale Mode</h4>
                  <p>A completely integrated in-house team dedicated solely to scaling your brand's revenue through full-stack production.</p>
                  <button class="btn-pill btn-pill-primary mini-book-btn">Learn More</button>
                </div>
              </div>
            </div>
          </li>
          <li><a href="work.html">Work</a></li>
          <li><a href="about.html">About</a></li>
        </ul>
      </nav>
      <div class="header-actions">
        <button class="btn-pill btn-pill-primary" id="nav-book-btn">Book Call</button>
        <div class="hamburger" id="hamburger" aria-label="Menu" aria-expanded="false">
          <span></span><span></span><span></span>
        </div>
      </div>
    </div>
  </header>

  <!-- MOBILE NAVIGATION -->
  <nav class="mobile-nav" id="mobile-nav">
    <a href="index.html">Home</a>
    <a href="services.html">Services</a>
    <a href="work.html">Work</a>
    <a href="about.html">About</a>
    <button class="btn-pill btn-pill-primary" id="mobile-book-btn" style="margin-top:20px;">Book a Call</button>
  </nav>

  <!-- ═══════════════════════════════════════════════════ -->
  <!-- HERO SECTION (SUPERSIDE STYLE - PEARL)              -->
  <!-- ═══════════════════════════════════════════════════ -->
  <section id="hero" class="hero section-pearl" style="padding-top: 160px; padding-bottom: 80px; position:relative; min-height:100vh; display:flex; align-items:center;">
    <canvas id="hero-particles" style="position:absolute; top:0; left:0; width:100%; height:100%; pointer-events:none; z-index:0;"></canvas>
    <div class="container" style="position:relative; z-index:1; text-align:center;">
      <h1 class="superside-hero-heading animate-on-scroll">Your Elite<br>In-House<br><span style="color: var(--accent-gold);">Growth Team.</span></h1>
      <p class="section-description animate-on-scroll" style="margin: 32px auto; font-size: 1.25rem; max-width: 700px;">
        Stop hiring fragmented freelancers. We are your dedicated cinematic production, branding, and performance marketing powerhouse.
      </p>
      <div class="hero-ctas animate-on-scroll" style="display:flex; gap: 24px; justify-content:center; margin-top: 40px;">
        <button class="btn-pill btn-pill-primary hero-book-btn" style="font-size: 1.1rem; padding: 20px 48px;">Start Scaling Now</button>
        <a href="work.html" class="btn-pill btn-pill-dark" style="font-size: 1.1rem; padding: 20px 48px;">View Our Work</a>
      </div>
    </div>
  </section>

  <!-- ═══════════════════════════════════════════════════ -->
  <!-- MARQUEE SECTION (SUPERSIDE STYLE - MARIGOLD)        -->
  <!-- ═══════════════════════════════════════════════════ -->
  <section class="section-marigold" style="padding: 80px 0; overflow:hidden;">
    <div style="white-space: nowrap; display:flex; gap: 64px; animation: scrollMarquee 20s linear infinite;">
      <h2 class="superside-heading" style="display:inline-block;">✦ 3.8X AVERAGE ROAS ✦ 100M+ IMPRESSIONS ✦ 50+ CINEMATIC ADS ✦ SCALE FASTER</h2>
      <h2 class="superside-heading" style="display:inline-block;">✦ 3.8X AVERAGE ROAS ✦ 100M+ IMPRESSIONS ✦ 50+ CINEMATIC ADS ✦ SCALE FASTER</h2>
    </div>
    <style>
      @keyframes scrollMarquee { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }
    </style>
  </section>

  <!-- ═══════════════════════════════════════════════════ -->
  <!-- BENTO GRID CAPABILITIES (POLICE BLUE)               -->
  <!-- ═══════════════════════════════════════════════════ -->
  <section id="capabilities" class="section-police" style="padding: 120px 0;">
    <div class="container">
      <div class="section-header animate-on-scroll" style="text-align:left;">
        <span class="section-label">The JayAds Advantage</span>
        <h2 class="superside-heading">Everything you need.<br>All in one place.</h2>
      </div>
      
      <div class="bento-grid animate-on-scroll">
        <!-- Big Bento Item -->
        <div class="bento-item" style="grid-column: span 12; display:flex; align-items:center; gap: 40px; background: var(--bg-surface);">
          <div style="flex: 1;">
            <h3 style="font-size: 3rem; font-weight:800; margin-bottom: 24px;">Cinematic Ad Films</h3>
            <p style="font-size: 1.25rem; color: var(--text-secondary); margin-bottom: 32px;">We don't just shoot videos; we craft high-conversion cinematic stories that stop thumbs and drive unparalleled sales metrics.</p>
            <a href="services.html" class="btn-pill btn-pill-primary">Explore Video Production</a>
          </div>
          <div style="flex: 1; background: var(--bg-primary); border-radius: 24px; height: 350px; display:flex; align-items:center; justify-content:center; border: 2px solid var(--border-light);">
            <span style="font-size: 5rem;">🎥</span>
          </div>
        </div>

        <!-- Medium Bento Items -->
        <div class="bento-item" style="grid-column: span 6; background: var(--text-primary); color: var(--bg-primary);">
          <span style="font-size: 3.5rem; margin-bottom: 24px; display:block;">⚡</span>
          <h3 style="font-size: 2.2rem; font-weight:800; margin-bottom: 16px;">Social Commerce</h3>
          <p style="font-size: 1.2rem; color: var(--bg-primary); opacity: 0.8; margin-bottom: 32px;">Rapid-deployment performance creatives tested relentlessly to crush your CPA goals.</p>
          <a href="services.html#social" class="btn-pill btn-pill-dark">See Performance Metrics</a>
        </div>
        
        <div class="bento-item" style="grid-column: span 6; background: var(--accent-gold); color: var(--bg-primary);">
          <span style="font-size: 3.5rem; margin-bottom: 24px; display:block;">✦</span>
          <h3 style="font-size: 2.2rem; font-weight:800; margin-bottom: 16px;">SEO & Architecture</h3>
          <p style="font-size: 1.2rem; color: var(--bg-primary); opacity: 0.9; margin-bottom: 32px;">Premium digital experiences engineered from the ground up for maximum organic visibility.</p>
          <a href="services.html#organic" class="btn-pill btn-pill-dark">View Web Systems</a>
        </div>
      </div>
    </div>
  </section>

  <!-- ═══════════════════════════════════════════════════ -->
  <!-- MODAL INJECTION & FOOTER                            -->
  <!-- ═══════════════════════════════════════════════════ -->
  <div id="modal-overlay" class="modal-overlay">
    <div class="modal-card">
      <button class="modal-close" id="modal-close" aria-label="Close modal">&times;</button>
      <div class="modal-header">
        <h3 style="font-size: 2.5rem; font-weight:800; color:var(--text-primary);">Book Your Growth Session</h3>
        <p style="color:var(--text-secondary); font-size:1.1rem; margin-top:8px;">Schedule a 30-minute discovery call with our production experts.</p>
      </div>
"""

new_index += modal_tail

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_index)

print("Rewrote index.html")
