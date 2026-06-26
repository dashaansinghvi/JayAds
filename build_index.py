import os

# Read modal code if exists, but we can write the entire content directly
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>JayAds — Your Elite In-House Growth &amp; Marketing Team | Chennai</title>
  <meta name="description" content="JayAds is Chennai's premium digital marketing agency. Data-driven performance ads, social commerce, brand strategy &amp; web growth — all under one roof." />
  <meta name="keywords" content="JayAds, digital marketing agency Chennai, performance marketing, brand strategy, social media marketing, video production, Jayanth S" />
  <meta name="author" content="JayAds — Jayanth S." />
  <meta property="og:title" content="JayAds — Your Elite In-House Growth &amp; Marketing Team" />
  <meta property="og:description" content="Data-driven performance campaigns, social commerce, and full-stack brand growth." />
  <meta property="og:type" content="website" />
  <meta name="twitter:card" content="summary_large_image" />
  <link rel="icon" type="image/png" href="favicon.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Playfair+Display:ital,wght@0,700;0,800;1,700;1,800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="styles.css" />
</head>
<body>

  <!-- ═══════════════════════════════════════════════════ -->
  <!-- PRELOADER                                           -->
  <!-- ═══════════════════════════════════════════════════ -->
  <div class="preloader" id="preloader">
    <div class="preloader-inner">
      <div class="preloader-logo">
        <span class="logo-accent">Jay</span>Ads
      </div>
      <div class="preloader-bar">
        <div class="preloader-fill"></div>
      </div>
      <p class="preloader-text">Crafting Your Experience…</p>
    </div>
  </div>

  <!-- ═══════════════════════════════════════════════════ -->
  <!-- SCROLL PROGRESS BAR                                 -->
  <!-- ═══════════════════════════════════════════════════ -->
  <div class="scroll-progress" id="scroll-progress"></div>

  <!-- ═══════════════════════════════════════════════════ -->
  <!-- GLOBAL HEADER & NAVIGATION                         -->
  <!-- ═══════════════════════════════════════════════════ -->
  <header class="site-header" id="site-header">
    <div class="header-inner">
      <a href="index.html" class="logo" aria-label="JayAds Home">
        <span class="logo-accent">Jay</span>Ads
      </a>

      <nav class="nav-links" id="nav-links" role="navigation" aria-label="Main Navigation">
        <a href="index.html" class="active nav-home-link" data-section="home">Home</a>
        <div class="nav-item-dropdown">
          <a href="services.html" class="dropdown-trigger" data-section="services">Services <svg class="chevron-svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="margin-left:4px; vertical-align:middle; margin-bottom:3px; opacity:0.8;"><polyline points="6 9 12 15 18 9"></polyline></svg></a>
          <div class="mega-dropdown">
            <div class="mega-dropdown-inner">
              <div class="mega-col-links">
                <span class="mega-title">Growth & Marketing</span>
                <a href="services.html#digital-marketing" class="mega-link-item">
                  <div class="mega-link-icon" style="width:24px;height:24px;display:flex;align-items:center;justify-content:center;color:var(--accent-gold);">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>
                  </div>
                  <div>
                    <span class="mega-link-title">Digital Marketing Strategy</span>
                    <span class="mega-link-desc">Data-driven growth plans</span>
                  </div>
                </a>
                <a href="services.html#seo" class="mega-link-item">
                  <div class="mega-link-icon" style="width:24px;height:24px;display:flex;align-items:center;justify-content:center;color:var(--accent-gold);">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
                  </div>
                  <div>
                    <span class="mega-link-title">Organic Growth (SEO)</span>
                    <span class="mega-link-desc">Long-term search visibility</span>
                  </div>
                </a>
                <a href="services.html#paid-ads" class="mega-link-item">
                  <div class="mega-link-icon" style="width:24px;height:24px;display:flex;align-items:center;justify-content:center;color:var(--accent-gold);">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
                  </div>
                  <div>
                    <span class="mega-link-title">Paid Advertising</span>
                    <span class="mega-link-desc">Google Ads &amp; Meta Campaigns</span>
                  </div>
                </a>
              </div>
              <div class="mega-col-links">
                <span class="mega-title">Design & Consulting</span>
                <a href="services.html#web-design" class="mega-link-item">
                  <div class="mega-link-icon" style="width:24px;height:24px;display:flex;align-items:center;justify-content:center;color:var(--accent-gold);">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg>
                  </div>
                  <div>
                    <span class="mega-link-title">Website Design</span>
                    <span class="mega-link-desc">High-converting online presence</span>
                  </div>
                </a>
                <a href="services.html#branding" class="mega-link-item">
                  <div class="mega-link-icon" style="width:24px;height:24px;display:flex;align-items:center;justify-content:center;color:var(--accent-gold);">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
                  </div>
                  <div>
                    <span class="mega-link-title">Brand Identity</span>
                    <span class="mega-link-desc">Positioning and visual assets</span>
                  </div>
                </a>
                <a href="services.html#consulting" class="mega-link-item">
                  <div class="mega-link-icon" style="width:24px;height:24px;display:flex;align-items:center;justify-content:center;color:var(--accent-gold);">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
                  </div>
                  <div>
                    <span class="mega-link-title">Marketing Consulting</span>
                    <span class="mega-link-desc">Expert strategy and advisory</span>
                  </div>
                </a>
              </div>
            </div>
          </div>
        </div>
        <a href="work.html" data-section="portfolio">Work</a>
        <a href="about.html" data-section="process">About</a>
      </nav>

      <button class="nav-cta desktop-only" id="nav-book-btn" aria-label="Book a Call">Book a Call</button>

      <button class="hamburger" id="hamburger" aria-label="Open Menu" aria-expanded="false">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>

    <!-- Mobile Menu Overlay -->
    <div class="mobile-nav" id="mobile-nav">
      <a href="index.html" class="active">Home</a>
      <a href="services.html">Services</a>
      <a href="work.html">Work</a>
      <a href="about.html">About</a>
      <button class="nav-cta mobile-book-btn" id="mobile-book-btn">Book a Call</button>
    </div>
  </header>

  <!-- ═══════════════════════════════════════════════════ -->
  <!-- HERO SECTION                                        -->
  <!-- ═══════════════════════════════════════════════════ -->
  <section class="hero" id="hero">
    <div class="hero-bg-mesh"></div>

    <!-- Animated floating orbs -->
    <div class="hero-orb hero-orb-1"></div>
    <div class="hero-orb hero-orb-2"></div>
    <div class="hero-orb hero-orb-3"></div>

    <div class="hero-content">
      <div class="hero-badge">
        <span class="badge-dot"></span>
        Accepting New Clients for Q3 2026
      </div>
      <h1 class="hero-headline">
        Your Dedicated <span class="accent word-reveal">Digital</span><br />
        Marketing &amp;<br />
        Growth Partner.
      </h1>
      <p class="hero-sub">
        Strategic execution. Measurable growth.<br />
        Data-driven campaigns designed to scale your brand.
      </p>
      <div class="hero-cta-group">
        <button class="btn-primary hero-book-btn" id="hero-book-btn" aria-label="Book a Call">
          Book a Call
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
        </button>
        <a href="services.html" class="btn-secondary">
          Explore Services
        </a>
      </div>
    </div>

    <!-- Decorative floating cards -->
    <div class="hero-float-card hero-float-card-1">
      <div class="float-card-icon" style="color:var(--accent-gold);">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
      </div>
      <div>
        <div class="float-card-title">Campaign Launched</div>
        <div class="float-card-sub">E-Commerce Brand • 10:30 AM</div>
      </div>
    </div>
    <div class="hero-float-card hero-float-card-2">
      <div class="float-card-icon" style="color:var(--accent-gold);">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg>
      </div>
      <div>
        <div class="float-card-title">Traffic Increased</div>
        <div class="float-card-sub">Organic Search Optimization</div>
      </div>
    </div>
  </section>

  <!-- ═══════════════════════════════════════════════════ -->
  <!-- TRUSTED BY MARQUEE                                  -->
  <!-- ═══════════════════════════════════════════════════ -->
  <section class="marquee-section" id="work-marquee">
    <p class="section-label">Trusted by Industry Leaders</p>
    <div class="marquee-container">
      <div class="marquee-track">
        <span class="marquee-item"><span class="marquee-dot"></span> Brand Strategy</span>
        <span class="marquee-item"><span class="marquee-dot"></span> SEO Growth</span>
        <span class="marquee-item"><span class="marquee-dot"></span> Digital Marketing</span>
        <span class="marquee-item"><span class="marquee-dot"></span> Web Design</span>
        <span class="marquee-item"><span class="marquee-dot"></span> Social Media</span>
        <span class="marquee-item"><span class="marquee-dot"></span> Content Creation</span>
        <span class="marquee-item"><span class="marquee-dot"></span> Paid Advertising</span>
        <span class="marquee-item"><span class="marquee-dot"></span> Brand Identity</span>
        <span class="marquee-item"><span class="marquee-dot"></span> Market Research</span>
        <!-- Duplicate for seamless infinite scroll -->
        <span class="marquee-item"><span class="marquee-dot"></span> Brand Strategy</span>
        <span class="marquee-item"><span class="marquee-dot"></span> SEO Growth</span>
        <span class="marquee-item"><span class="marquee-dot"></span> Digital Marketing</span>
        <span class="marquee-item"><span class="marquee-dot"></span> Web Design</span>
        <span class="marquee-item"><span class="marquee-dot"></span> Social Media</span>
        <span class="marquee-item"><span class="marquee-dot"></span> Content Creation</span>
        <span class="marquee-item"><span class="marquee-dot"></span> Paid Advertising</span>
        <span class="marquee-item"><span class="marquee-dot"></span> Brand Identity</span>
        <span class="marquee-item"><span class="marquee-dot"></span> Market Research</span>
      </div>
    </div>
  </section>

  <!-- ═══════════════════════════════════════════════════ -->
  <!-- SERVICES GRID                                       -->
  <!-- ═══════════════════════════════════════════════════ -->
  <section class="services-section" id="services">
    <div class="container">
      <div class="section-header animate-on-scroll">
        <span class="heading-accent"></span>
        <p class="section-label">Our Capabilities</p>
        <h2 class="section-heading">Full-Stack Creative<br />&amp; Growth Services.</h2>
        <p class="section-description">
          We don't do piecemeal. Every engagement is a fully integrated marketing and 
          marketing operation — from concept to conversion.
        </p>
      </div>

      <div class="services-grid">

        <!-- SERVICE 1 — Featured / Ad Films -->
        <div class="service-card featured animate-on-scroll" data-delay="1">
          <span class="card-number">01</span>
          <div class="service-icon" data-icon="film">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="2.18" ry="2.18"/><line x1="7" y1="2" x2="7" y2="22"/><line x1="17" y1="2" x2="17" y2="22"/><line x1="2" y1="12" x2="22" y2="12"/><line x1="2" y1="7" x2="7" y2="7"/><line x1="2" y1="17" x2="7" y2="17"/><line x1="17" y1="17" x2="22" y2="17"/><line x1="17" y1="7" x2="22" y2="7"/></svg>
          </div>
          <h3 class="card-title">Digital Marketing Strategy</h3>
          <p class="card-description">
            We engineer the strategic foundation your brand is built on. Comprehensive communication plans and data-driven marketing frameworks that give you an unfair advantage in every market you enter.
          </p>
          <div class="card-tags">
            <span class="tag">Brand Identity</span>
            <span class="tag">Communication Plans</span>
            <span class="tag">Market Research</span>
            <span class="tag">Positioning</span>
          </div>
          <a href="#" class="card-cta" id="service-1-cta" onclick="openModal(); return false;">Get Started →</a>
        </div>

        <!-- SERVICE 2 — Social Commerce -->
        <div class="service-card animate-on-scroll" data-delay="2">
          <span class="card-number">02</span>
          <div class="service-icon" data-icon="social">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
          </div>
          <h3 class="card-title">Social Media &amp; Performance Advertising</h3>
          <p class="card-description">
            We plan, produce, and deploy high-converting campaigns across social channels. From Meta Business Suite management to end-to-end ad platform execution — we drive revenue, not just impressions.
          </p>
          <div class="card-tags">
            <span class="tag">Meta Ads</span>
            <span class="tag">Media Buying</span>
            <span class="tag">Social Strategy</span>
            <span class="tag">Performance Marketing</span>
          </div>
          <a href="#" class="card-cta" id="service-2-cta" onclick="openModal(); return false;">Get Started →</a>
        </div>

        <!-- SERVICE 3 — Brand Strategy -->
        <div class="service-card animate-on-scroll" data-delay="3">
          <span class="card-number">03</span>
          <div class="service-icon" data-icon="brand">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>
          </div>
          <h3 class="card-title">Web Design &amp; Development</h3>
          <p class="card-description">
            We build responsive, fast-loading, and conversion-optimized websites. From landing pages to full corporate platforms, our designs are crafted to engage your audience and drive action.
          </p>
          <div class="card-tags">
            <span class="tag">UI/UX Design</span>
            <span class="tag">Web Development</span>
            <span class="tag">Landing Pages</span>
            <span class="tag">E-Commerce</span>
          </div>
          <a href="#" class="card-cta" id="service-3-cta" onclick="openModal(); return false;">Get Started →</a>
        </div>

        <!-- SERVICE 4 — Web & SEO -->
        <div class="service-card animate-on-scroll" data-delay="4">
          <span class="card-number">04</span>
          <div class="service-icon" data-icon="web">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
          </div>
          <h3 class="card-title">SEO &amp; Organic Growth</h3>
          <p class="card-description">
            We optimize your digital ecosystem for compounding, long-term growth. Through technical SEO audits and content strategy, we ensure your brand dominates the search results that matter.
          </p>
          <div class="card-tags">
            <span class="tag">SEO</span>
            <span class="tag">Organic Traffic</span>
            <span class="tag">Content Strategy</span>
            <span class="tag">Link Building</span>
          </div>
          <a href="#" class="card-cta" id="service-4-cta" onclick="openModal(); return false;">Get Started →</a>
        </div>

      </div>
    </div>
  </section>

  <!-- ═══════════════════════════════════════════════════ -->
  <!-- PORTFOLIO / OUR WORK                               -->
  <!-- ═══════════════════════════════════════════════════ -->
  <section class="portfolio-section" id="portfolio">
    <div class="container">
      <div class="section-header animate-on-scroll">
        <span class="heading-accent"></span>
        <p class="section-label">Our Work</p>
        <h2 class="section-heading">Data-Driven Work.<br />Measurable Results.</h2>
        <p class="section-description">
          A glimpse into the productions we've delivered. Every frame, every campaign — built to convert.
        </p>
      </div>
            <div class="portfolio-grid">
        <!-- Project 1 -->
        <div class="portfolio-card animate-on-scroll" data-delay="1">
          <div class="portfolio-thumb portfolio-thumb-1">
            <span class="portfolio-tag">Paid Ads</span>
          </div>
          <div class="portfolio-info">
            <h3 class="portfolio-title">E-Commerce Retail Brand</h3>
            <p class="portfolio-desc">Performance marketing campaign designed to scale customer acquisition.</p>
          </div>
        </div>

        <!-- Project 2 -->
        <div class="portfolio-card animate-on-scroll" data-delay="2">
          <div class="portfolio-thumb portfolio-thumb-2">
            <span class="portfolio-tag">Social Media</span>
          </div>
          <div class="portfolio-info">
            <h3 class="portfolio-title">FMCG Product Launch</h3>
            <p class="portfolio-desc">Comprehensive social media strategy and content rollout.</p>
          </div>
        </div>

        <!-- Project 3 -->
        <div class="portfolio-card animate-on-scroll" data-delay="3">
          <div class="portfolio-thumb portfolio-thumb-3">
            <span class="portfolio-tag">Web Design</span>
          </div>
          <div class="portfolio-info">
            <h3 class="portfolio-title">Tech Startup Portal</h3>
            <p class="portfolio-desc">High-performance corporate website engineered for rapid lead generation.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ═══════════════════════════════════════════════════ -->
  <!-- WORKFLOW / THE PROCESS & UNFAIR ADVANTAGE           -->
  <!-- ═══════════════════════════════════════════════════ -->
  <section class="process-section" id="process">
    <div class="container">
      <div class="section-header animate-on-scroll">
        <span class="heading-accent"></span>
        <p class="section-label">The Process</p>
        <h2 class="section-heading">The JayAds<br />Operating System.</h2>
        <p class="section-description">
          While other agencies are scheduling meetings about meetings, we're already on set. 
          Here's the precision-engineered workflow behind our same-day delivery guarantee.
        </p>
      </div>

      <div class="process-timeline">
        <!-- Step 1 -->
        <div class="process-step animate-on-scroll">
          <div class="step-number">01</div>
          <div class="step-content">
            <h3 class="step-title">Strategic Discovery</h3>
            <p class="step-description">
              We begin by deeply understanding your brand, target audience, and business objectives. We don't just execute; we architect a plan that aligns with your goals.
            </p>
          </div>
        </div>
        <!-- Step 2 -->
        <div class="process-step animate-on-scroll">
          <div class="step-number">02</div>
          <div class="step-content">
            <h3 class="step-title">Data-Driven Execution</h3>
            <p class="step-description">
              Our team launches campaigns based on insights, utilizing the latest digital marketing tools and platforms to maximize reach and engagement.
            </p>
          </div>
        </div>
        <!-- Step 3 -->
        <div class="process-step animate-on-scroll">
          <div class="step-number">03</div>
          <div class="step-content">
            <h3 class="step-title">Continuous Optimization</h3>
            <p class="step-description">
              We monitor performance in real-time, making precise adjustments to targeting, creative, and bidding to ensure optimal return on investment.
            </p>
          </div>
        </div>
        <!-- Step 4 -->
        <div class="process-step animate-on-scroll">
          <div class="step-number">04</div>
          <div class="step-content">
            <h3 class="step-title">Scaling Success</h3>
            <p class="step-description">
              Once we find the winning formula, we scale the campaigns sustainably, driving consistent growth and long-term brand authority.
            </p>
          </div>
        </div>
      </div>

      <!-- Advantage Cards -->
      <div class="advantage-grid">
        <div class="advantage-card animate-on-scroll" data-delay="1">
          <div class="advantage-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          </div>
          <h4 class="advantage-title">Agile Execution</h4>
          <p class="advantage-desc">
            We move quickly to capitalize on trends and market opportunities, ensuring your brand stays ahead.
          </p>
        </div>
        <div class="advantage-card animate-on-scroll" data-delay="2">
          <div class="advantage-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
          </div>
          <h4 class="advantage-title">Premium Quality</h4>
          <p class="advantage-desc">
            Every deliverable, from ad copy to web design, is crafted with the highest professional standards in mind.
          </p>
        </div>
        <div class="advantage-card animate-on-scroll" data-delay="3">
          <div class="advantage-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>
          </div>
          <h4 class="advantage-title">Infinite Scalability</h4>
          <p class="advantage-desc">
            Strategic partners extend our operational capacity, 
            ensuring your campaigns never stall — regardless of volume.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- ═══════════════════════════════════════════════════ -->
  <!-- TESTIMONIALS SLIDER SECTION                        -->
  <!-- ═══════════════════════════════════════════════════ -->
  <section id="testimonials" class="testimonials-section" style="background-color: var(--bg-surface);">
    <div class="container">
      <div class="section-header animate-on-scroll" style="text-align: center;">
        <span class="heading-accent" style="margin: 0 auto;"></span>
        <p class="section-label">Client Voices</p>
        <h2 class="section-heading">What Our Clients<br />Actually Say.</h2>
        <p class="section-description" style="margin-left: auto; margin-right: auto;">
          Real experiences. Genuine feedback. Trusted by leading brands.
        </p>
      </div>

      <div class="testimonial-carousel-container animate-on-scroll" style="max-width: 800px; margin: 0 auto;">
        <div class="testimonial-track" id="testimonial-track">
          <!-- Slide 1 -->
          <div class="testimonial-slide">
            <div class="testimonial-card" style="background: var(--bg-primary); padding: 48px; border-radius: 24px; text-align: center; border: 1px solid var(--border-light); margin: 0 auto; max-width: 760px; height: 100%;">
              <div class="quote-mark" style="font-size: 4rem; color: var(--accent-gold); opacity: 0.3; line-height: 1; margin-bottom: -10px;">"</div>
              <p class="quote-text" style="font-size: 1.25rem; font-style: italic; line-height: 1.8; color: var(--text-primary);">
                JayAds completely transformed how we show up on social media. The digital campaign they designed outperformed three months of our previous efforts. 
                Genuinely shocked by the quality and the speed.
              </p>
              <div class="quote-author" style="margin-top: 24px; display: flex; flex-direction: column; align-items: center; gap: 8px;">
                <div class="author-name" style="font-size: 1.2rem; font-weight: 700; color: var(--accent-gold);">Rajesh K.</div>
                <div class="author-role" style="font-size: 0.9rem; color: var(--text-secondary); opacity:0.8;">Marketing Director, Tech Startup</div>
                <div class="author-stars" style="color: var(--accent-gold); letter-spacing: 2px;">★★★★★</div>
              </div>
            </div>
          </div>
          <!-- Slide 2 -->
          <div class="testimonial-slide">
            <div class="testimonial-card" style="background: var(--bg-primary); padding: 48px; border-radius: 24px; text-align: center; border: 1px solid var(--border-light); margin: 0 auto; max-width: 760px; height: 100%;">
              <div class="quote-mark" style="font-size: 4rem; color: var(--accent-gold); opacity: 0.3; line-height: 1; margin-bottom: -10px;">"</div>
              <p class="quote-text" style="font-size: 1.25rem; font-style: italic; line-height: 1.8; color: var(--text-primary);">
                We hired JayAds for a product launch campaign and they exceeded every expectation. 
                Incredible ROI on Meta in the first month, rapid turnarounds, and a strategic direction that actually matched our brand voice. This is what a real agency looks like.
              </p>
              <div class="quote-author" style="margin-top: 24px; display: flex; flex-direction: column; align-items: center; gap: 8px;">
                <div class="author-name" style="font-size: 1.2rem; font-weight: 700; color: var(--accent-gold);">Sunita P.</div>
                <div class="author-role" style="font-size: 0.9rem; color: var(--text-secondary); opacity:0.8;">Founder, Local Business</div>
                <div class="author-stars" style="color: var(--accent-gold); letter-spacing: 2px;">★★★★★</div>
              </div>
            </div>
          </div>
          <!-- Slide 3 -->
          <div class="testimonial-slide">
            <div class="testimonial-card" style="background: var(--bg-primary); padding: 48px; border-radius: 24px; text-align: center; border: 1px solid var(--border-light); margin: 0 auto; max-width: 760px; height: 100%;">
              <div class="quote-mark" style="font-size: 4rem; color: var(--accent-gold); opacity: 0.3; line-height: 1; margin-bottom: -10px;">"</div>
              <p class="quote-text" style="font-size: 1.25rem; font-style: italic; line-height: 1.8; color: var(--text-primary);">
                What sets JayAds apart is the ownership. Jayanth and his team treat your brand like it's 
                their own business. We've scaled our marketing efforts significantly, and the quality of their work has never once dipped. They're not an agency — they're an asset.
              </p>
              <div class="quote-author" style="margin-top: 24px; display: flex; flex-direction: column; align-items: center; gap: 8px;">
                <div class="author-name" style="font-size: 1.2rem; font-weight: 700; color: var(--accent-gold);">Arjun M.</div>
                <div class="author-role" style="font-size: 0.9rem; color: var(--text-secondary); opacity:0.8;">CEO, E-Commerce Brand</div>
                <div class="author-stars" style="color: var(--accent-gold); letter-spacing: 2px;">★★★★★</div>
              </div>
            </div>
          </div>
        </div>

        <div class="testimonial-nav-btns">
          <button class="testimonial-nav-btn" onclick="slideTestimonial(-1)" aria-label="Previous testimonial">←</button>
          <button class="testimonial-nav-btn" onclick="slideTestimonial(1)" aria-label="Next testimonial">→</button>
        </div>
      </div>
    </div>
  </section>

  <!-- ═══════════════════════════════════════════════════ -->
  <!-- SCALE EVIDENCE / RESULTS SECTION                    -->
  <!-- ═══════════════════════════════════════════════════ -->
  <section class="services-section" style="padding-top: 60px;">
    <div class="container">
      <div class="section-header animate-on-scroll">
        <span class="section-label">The Proof</span>
        <h2 class="section-heading">Unreasonable <span class="text-gold"><em>Results</em></span>.</h2>
        <div class="heading-accent"></div>
        <p class="section-description">
          We measure success purely by bottom-line growth. Here's a snapshot of what happens when you combine elite creative strategy with ruthless media buying.
        </p>
      </div>

      <div class="services-grid">
        <!-- Case Study 1 -->
        <div class="service-card animate-on-scroll">
          <div class="card-icon" style="color:var(--accent-gold);"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg></div>
          <span class="card-number">Growth</span>
          <h3 class="card-title">D2C Apparel Brand</h3>
          <p class="card-description">We completely overhauled their digital presence and restructured their ad buying, resulting in significant sustained growth.</p>
          <div class="card-tags">
            <span class="tag">Meta Ads</span>
            <span class="tag">Strategy</span>
            <span class="tag">Scale</span>
          </div>
        </div>

        <!-- Case Study 2 -->
        <div class="service-card animate-on-scroll">
          <div class="card-icon" style="color:var(--accent-gold);"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="23 6 13.5 15.5 8.5 10.5 1 18"/><polyline points="17 6 23 6 23 12"/></svg></div>
          <span class="card-number">Results</span>
          <h3 class="card-title">SaaS Platform</h3>
          <p class="card-description">Executed a complete digital marketing strategy and organic SEO architecture, leading to a massive increase in qualified leads.</p>
          <div class="card-tags">
            <span class="tag">B2B Tech</span>
            <span class="tag">SEO Architecture</span>
            <span class="tag">Brand Strategy</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ═══════════════════════════════════════════════════ -->
  <!-- ENGAGEMENT MODELS (HOW WE WORK)                     -->
  <!-- ═══════════════════════════════════════════════════ -->
  <section class="process-section" style="padding-bottom: 120px;">
    <div class="container">
      <div class="section-header animate-on-scroll">
        <span class="section-label">Partnership Tiers</span>
        <h2 class="section-heading">How We <span class="text-gold"><em>Engage</em></span>.</h2>
        <div class="heading-accent"></div>
        <p class="section-description">
          Whether you need a single massive campaign or a fully integrated growth team, we have a model built to execute.
        </p>
      </div>

      <div class="advantage-grid">
        <!-- Tier 1 -->
        <div class="advantage-card animate-on-scroll">
          <div class="adv-icon"></div>
          <h3 class="adv-title">Project Based</h3>
          <p class="adv-desc">Perfect for massive, comprehensive digital campaigns, brand identity overhauls, or launch campaigns. Defined scope, fixed timeline, premium delivery.</p>
          <ul style="color: var(--text-secondary); margin-top: 16px; list-style-type: disc; padding-left: 20px; font-size: 0.95rem; line-height: 1.8;">
            <li>Performance Ads & Paid Media</li>
            <li>Brand Identity Design</li>
            <li>Web Development Sprints</li>
          </ul>
        </div>

        <!-- Tier 2 -->
        <div class="advantage-card animate-on-scroll">
          <div class="adv-icon"></div>
          <h3 class="adv-title">Hyper-Scale Mode</h3>
          <p class="adv-desc">A monthly retainer where we act as your entire in-house growth department. Continuous campaign management, media buying, and CRO.</p>
          <ul style="color: var(--text-secondary); margin-top: 16px; list-style-type: disc; padding-left: 20px; font-size: 0.95rem; line-height: 1.8;">
            <li>Continuous Campaign Management</li>
            <li>Full-Funnel Media Buying</li>
            <li>Priority Resource Allocation</li>
          </ul>
        </div>

        <!-- Tier 3 -->
        <div class="advantage-card animate-on-scroll">
          <div class="adv-icon">✦</div>
          <h3 class="adv-title">Organic Architect</h3>
          <p class="adv-desc">A specialized sprint focused purely on SEO and long-term organic web traffic. We build the content architecture that prints passive leads.</p>
          <ul style="color: var(--text-secondary); margin-top: 16px; list-style-type: disc; padding-left: 20px; font-size: 0.95rem; line-height: 1.8;">
            <li>Technical SEO Audits</li>
            <li>Programmatic Content Silos</li>
            <li>High-DR Backlink Acquisition</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- ═══════════════════════════════════════════════════ -->
  <!-- DYNAMIC FAQ SECTION                                 -->
  <!-- ═══════════════════════════════════════════════════ -->
  <section class="services-section" style="padding: 100px 0; background-color: var(--bg-primary);">
    <div class="container">
      <div class="section-header animate-on-scroll" style="text-align: center;">
        <span class="heading-accent" style="margin: 0 auto;"></span>
        <span class="section-label" style="color: var(--text-secondary);">FAQ</span>
        <h2 class="section-heading">Frequently Asked Questions</h2>
        <p class="section-description" style="margin-left: auto; margin-right: auto;">Everything you need to know about our turnaround time, travel policy, and packages.</p>
      </div>

      <div class="faq-grid-custom animate-on-scroll">
        <!-- FAQ 1 -->
        <div class="faq-item-custom">
          <button class="faq-question-custom" onclick="toggleFaq(this)">
            How do you measure campaign success?
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>
          </button>
          <div class="faq-answer-custom">
            <div class="faq-answer-inner">
              We track key performance indicators (KPIs) tailored to your goals, providing transparent reporting and regular check-ins.
            </div>
          </div>
        </div>
        <!-- FAQ 2 -->
        <div class="faq-item-custom">
          <button class="faq-question-custom" onclick="toggleFaq(this)">
            Do you have standard packages?
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>
          </button>
          <div class="faq-answer-custom">
            <div class="faq-answer-inner">
              Every brand's requirements are unique. That's why our pricing isn't one-size-fits-all. We connect with you, discuss your marketing goals, and draft a customized package just for your brand campaign or project scale.
            </div>
          </div>
        </div>
        <!-- FAQ 3 -->
        <div class="faq-item-custom">
          <button class="faq-question-custom" onclick="toggleFaq(this)">
            What is your onboarding process like?
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>
          </button>
          <div class="faq-answer-custom">
            <div class="faq-answer-inner">
              Once we agree on the scope, we kick off with a deep-dive discovery session, followed by a detailed strategy roadmap before execution begins.
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ═══════════════════════════════════════════════════ -->
  <!-- FINAL CONVERSION CTA                                -->
  <!-- ═══════════════════════════════════════════════════ -->
  <section class="final-cta" id="final-cta">
    <div class="cta-bg-orb"></div>
    <div class="container final-cta-content animate-on-scroll">
      <p class="section-label">Ready to Move?</p>
      <h2 class="cta-headline">
        Stop Guessing with Your Marketing.<br />
        <span class="text-gold">Start Scaling with Certainty.</span>
      </h2>
      <p class="cta-description">
        Your competitors are already producing at the speed of culture. 
        Book a call and discover what a dedicated, elite marketing 
        and growth team can do for your brand — starting this week.
      </p>
      <button class="btn-cta-large" id="cta-book-btn" aria-label="Book a Call">
        Book a Call
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
      </button>
      <div class="cta-trust-badges">
        <span class="trust-badge"> No Commitment Required</span>
        <span class="trust-badge"> Response in 2 Hours</span>
        <span class="trust-badge"> Free Strategy Session</span>
      </div>
    </div>
  </section>

  <!-- ═══════════════════════════════════════════════════ -->
  <!-- FOOTER                                              -->
  <!-- ═══════════════════════════════════════════════════ -->
  <footer class="site-footer" id="contact">
    <div class="footer-main">
      <div class="container">
        <div class="footer-grid">

          <!-- Brand Column -->
          <div class="footer-column footer-brand">
            <a href="#" class="logo footer-logo">
              <span class="logo-accent">Jay</span>Ads
            </a>
            <p class="footer-about">
              Chennai's premium in-house marketing and digital growth team. 
              Premium quality. Ruthless speed. Guaranteed results.
            </p>
            <div class="social-icons">
              <a href="https://www.instagram.com/jayads_official/?hl=en" target="_blank" rel="noopener noreferrer" class="social-icon" aria-label="Instagram">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>
              </a>
              <a href="https://wa.me/919876543210?text=Hi%20JayAds!%20I%20found%20you%20on%20your%20website%20and%20want%20to%20discuss%20a%20project." target="_blank" rel="noopener noreferrer" class="social-icon" aria-label="WhatsApp">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
              </a>
              <a href="#" class="social-icon" aria-label="Justdial" title="Find us on Justdial">
                <span style="font-size:0.7rem;font-weight:800;letter-spacing:-0.5px;color:inherit;">Jd</span>
              </a>
            </div>
          </div>

          <!-- Quick Links -->
          <div class="footer-column">
            <h4 class="footer-heading">Explore</h4>
            <div class="footer-links">
              <a href="#services">Services</a>
              <a href="#portfolio">Our Work</a>
              <a href="#process">The Process</a>
              <a href="#testimonials">Testimonials</a>
              <a href="#contact">Contact</a>
            </div>
          </div>

          <!-- Contact / Headquarters -->
          <div class="footer-column">
            <h4 class="footer-heading">Headquarters</h4>
            <div class="footer-contact-info">
              <div class="contact-item">
                <svg class="contact-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
                <address style="font-style:normal;">
                  Door No. 7, 40/1, 6th St,<br />
                  Kumaran Nagar, A Block,<br />
                  Anna Nagar East,<br />
                  Chennai – 600102, Tamil Nadu.
                </address>
              </div>
              <div class="contact-item">
                <svg class="contact-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 12 19.79 19.79 0 0 1 1.61 3.37 2 2 0 0 1 3.6 1h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.91 8.91a16 16 0 0 0 6 6l.92-.92a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 21.73 16a2 2 0 0 1 .19.92z"/></svg>
                <a href="tel:+919876543210" style="color:inherit;">+91 98765 43210</a>
              </div>
              <div class="contact-item">
                <svg class="contact-icon" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                <a href="mailto:hello@jayads.in" style="color:inherit;">hello@jayads.in</a>
              </div>
            </div>
          </div>

          <!-- Hours -->
          <div class="footer-column">
            <h4 class="footer-heading">Operating Hours</h4>
            <div class="footer-hours">
              <div class="hours-row">
                <span class="day">Mon — Fri</span>
                <span class="time">9:30 AM – 6:00 PM</span>
              </div>
              <div class="hours-row">
                <span class="day">Saturday</span>
                <span class="time">10:00 AM – 6:00 PM</span>
              </div>
              <div class="hours-row">
                <span class="day">Sunday</span>
                <span class="time">Closed</span>
              </div>
            </div>
            <button class="footer-cta-btn" id="footer-cta-btn" aria-label="Book a Call">Book a Free Call →</button>
          </div>

        </div>
      </div>
    </div>

    <!-- Footer Bottom -->
    <div class="footer-bottom">
      <div class="footer-bottom-inner">
        <p class="footer-copyright">&copy; 2026 JayAds. All rights reserved. Built by Jayanth S.</p>
        <a href="#hero" class="back-to-top" aria-label="Back to top">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="m18 15-6-6-6 6"/></svg>
          Back to Top
        </a>
      </div>
    </div>
  </footer>

  <!-- ═══════════════════════════════════════════════════ -->
  <!-- BOOK A CALL MODAL                                   -->
  <!-- ═══════════════════════════════════════════════════ -->
  <div class="modal-overlay" id="modal-overlay" role="dialog" aria-modal="true" aria-labelledby="modal-title">
    <div class="modal-card">
      <button class="modal-close" id="modal-close" aria-label="Close modal">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>

      <div class="modal-header">
        <div class="modal-logo"><span class="logo-accent">Jay</span>Ads</div>
        <h2 class="modal-title" id="modal-title">Book Your Free Strategy Call</h2>
        <p class="modal-subtitle">We'll respond within 2 hours. No fluff — just a direct conversation about your brand's potential.</p>
      </div>

      <!-- Success State -->
      <div class="modal-success" id="modal-success" style="display:none;">
        <div class="success-icon"></div>
        <h3 class="success-title">You're Booked In!</h3>
        <p class="success-text">We'll reach out within 2 hours to confirm your call time. Check your email for a confirmation.</p>
        <button class="btn-primary" onclick="closeModal();" style="margin-top:24px;">Close</button>
      </div>

      <!-- Form State -->
      <form class="modal-form" id="booking-form">
        <div class="form-group">
          <label for="booking-name" class="form-label">Full Name *</label>
          <input type="text" id="booking-name" class="form-input" placeholder="Jayanth S." required />
        </div>

        <div class="form-group">
          <label for="booking-email" class="form-label">Work Email *</label>
          <input type="email" id="booking-email" class="form-input" placeholder="jayanth@brand.com" required />
        </div>

        <div class="form-group">
          <label for="booking-company" class="form-label">Company / Brand Name</label>
          <input type="text" id="booking-company" class="form-input" placeholder="JayAds Ltd." />
        </div>

        <div class="form-group">
          <label for="booking-service" class="form-label">What do you need help with? *</label>
          <select id="booking-service" class="form-select" required>
            <option value="" disabled selected>Select a primary goal</option>
            <option value="paid-ads"> Ad Films &amp; Video Production</option>
            <option value="social-commerce"> Social Commerce Ads (Same-Day Delivery)</option>
            <option value="branding"> Brand Strategy &amp; Identity</option>
            <option value="organic-growth">✦ Web Design &amp; SEO Growth</option>
            <option value="other"> All of the Above (Hyper-Scale Mode)</option>
          </select>
        </div>

        <div class="form-group">
          <label for="booking-message" class="form-label">Tell us about your project</label>
          <textarea id="booking-message" class="form-textarea" rows="3" placeholder="Briefly describe your product, target audience, or current bottlenecks..."></textarea>
        </div>

        <button type="submit" class="btn-primary form-submit-btn" id="form-submit-btn">
          Confirm Strategy Session →
        </button>
      </form>
    </div>
  </div>

  <!-- ═══════════════════════════════════════════════════ -->
  <!-- FLOATING ACTIONS & WIDGETS                          -->
  <!-- ═══════════════════════════════════════════════════ -->
  <!-- WhatsApp Widget -->
  <a href="https://wa.me/919876543210?text=Hi%20JayAds!%20I'm%20interested%20in%20scaling%20my%20brand%20with%20cinematic%20ad%20creative." 
     target="_blank" rel="noopener noreferrer" class="float-whatsapp" aria-label="Chat on WhatsApp">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>
  </a>

  <!-- Floating Call Booking CTA (Visible on scroll) -->
  <button class="float-booking" id="float-booking" aria-label="Quick Booking" onclick="openModal();">
    <span>Book Call</span>
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg>
  </button>

  <!-- ═══════════════════════════════════════════════════ -->
  <!-- JAVASCRIPT ANIMATIONS & INTERACTIONS               -->
  <!-- ═══════════════════════════════════════════════════ -->
  <script>
    // PRELOADER
    window.addEventListener('load', () => {
      const preloader = document.getElementById('preloader');
      setTimeout(() => {
        preloader.classList.add('fade-out');
        document.body.classList.add('loaded');
        setTimeout(() => {
          preloader.style.display = 'none';
        }, 600);
      }, 800);
    });

    // SCROLL PROGRESS BAR
    window.addEventListener('scroll', () => {
      const scrollProgress = document.getElementById('scroll-progress');
      const scrollTop = window.scrollY || document.documentElement.scrollTop;
      const docHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrollPercent = (scrollTop / docHeight) * 100;
      if (scrollProgress) {
        scrollProgress.style.width = scrollPercent + '%';
      }
      
      // Floating CTA visibility
      const floatBooking = document.getElementById('float-booking');
      if (floatBooking) {
        if (scrollTop > 400) {
          floatBooking.classList.add('visible');
        } else {
          floatBooking.classList.remove('visible');
        }
      }

      // Sticky Header Background change on scroll
      const siteHeader = document.getElementById('site-header');
      if (siteHeader) {
        if (scrollTop > 50) {
          siteHeader.classList.add('scrolled');
        } else {
          siteHeader.classList.remove('scrolled');
        }
      }
    });

    // MOBILE MENU
    const hamburger = document.getElementById('hamburger');
    const mobileNav = document.getElementById('mobile-nav');

    if (hamburger && mobileNav) {
      hamburger.addEventListener('click', () => {
        const expanded = hamburger.getAttribute('aria-expanded') === 'true';
        hamburger.setAttribute('aria-expanded', !expanded);
        hamburger.classList.toggle('active');
        mobileNav.classList.toggle('active');
        document.body.classList.toggle('no-scroll');
      });

      // Close menu on navigation click
      mobileNav.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
          hamburger.setAttribute('aria-expanded', 'false');
          hamburger.classList.remove('active');
          mobileNav.classList.remove('active');
          document.body.classList.remove('no-scroll');
        });
      });
    }

    // BOOK A CALL MODAL
    const modalOverlay = document.getElementById('modal-overlay');
    const modalClose = document.getElementById('modal-close');
    const bookingForm = document.getElementById('booking-form');
    const modalSuccess = document.getElementById('modal-success');

    function openModal() {
      if (modalOverlay) {
        modalOverlay.classList.add('active');
        document.body.classList.add('no-scroll');
        // Reset form & state
        if (bookingForm) bookingForm.style.display = 'flex';
        if (modalSuccess) modalSuccess.style.display = 'none';
      }
    }

    function closeModal() {
      if (modalOverlay) {
        modalOverlay.classList.remove('active');
        document.body.classList.remove('no-scroll');
      }
    }

    if (modalClose) {
      modalClose.addEventListener('click', closeModal);
    }
    
    if (modalOverlay) {
      modalOverlay.addEventListener('click', (e) => {
        if (e.target === modalOverlay) closeModal();
      });
    }

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') closeModal();
    });

    // Attach modal events to all CTA buttons
    const bookButtons = document.querySelectorAll('.hero-book-btn, .mini-book-btn, #nav-book-btn, #mobile-book-btn, #cta-book-btn, #footer-cta-btn');
    bookButtons.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        openModal();
      });
    });

    // Form submission
    if (bookingForm) {
      bookingForm.addEventListener('submit', (e) => {
        e.preventDefault();
        const submitBtn = document.getElementById('form-submit-btn');
        if (submitBtn) {
          submitBtn.disabled = true;
          submitBtn.innerText = 'Reserving Spot...';
        }

        // Mock Submission timeout
        setTimeout(() => {
          if (bookingForm) bookingForm.style.display = 'none';
          if (modalSuccess) modalSuccess.style.display = 'flex';
          if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.innerText = 'Confirm Strategy Session →';
          }
        }, 1200);
      });
    }

    // TESTIMONIALS SLIDER
    let currentSlide = 0;
    function slideTestimonial(direction) {
      const track = document.getElementById('testimonial-track');
      const totalSlides = 3;
      currentSlide = (currentSlide + direction + totalSlides) % totalSlides;
      if (track) {
        track.style.transform = `translateX(-${currentSlide * 100}%)`;
      }
    }

    // FAQ ACCORDIONS
    function toggleFaq(btn) {
      const parent = btn.parentElement;
      const isActive = parent.classList.contains('active');
      
      // Close all FAQs
      document.querySelectorAll('.faq-item-custom').forEach(item => {
        item.classList.remove('active');
        const ans = item.querySelector('.faq-answer-custom');
        if (ans) ans.style.maxHeight = null;
      });
      
      if (!isActive) {
        parent.classList.add('active');
        const answer = parent.querySelector('.faq-answer-custom');
        if (answer) {
          answer.style.maxHeight = answer.scrollHeight + "px";
        }
      }
    }

    // ANIMATE ON SCROLL (INTERSECTION OBSERVER)
    const animScrollElements = document.querySelectorAll('.animate-on-scroll');
    const scrollObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: "0px 0px -50px 0px"
    });

    animScrollElements.forEach(el => scrollObserver.observe(el));

    // STATS COUNT-UP ANIMATION
    const statNumbers = document.querySelectorAll('.stat-number');
    const countObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const target = entry.target;
          const countTo = parseInt(target.getAttribute('data-count'), 10);
          const suffix = target.getAttribute('data-suffix') || '';
          let count = 0;
          const duration = 1500; // ms
          const stepTime = Math.max(Math.floor(duration / countTo), 15);
          
          const timer = setInterval(() => {
            count += Math.ceil(countTo / 20); // Increment
            if (count >= countTo) {
              target.innerText = countTo + suffix;
              clearInterval(timer);
            } else {
              target.innerText = count + suffix;
            }
          }, stepTime);
          
          observer.unobserve(target);
        }
      });
    }, { threshold: 0.5 });

    statNumbers.forEach(num => countObserver.observe(num));

    // DYNAMIC RADIAL GRADIENT SPOTLIGHT CARD EFFECT
    const spotCards = document.querySelectorAll('.advantage-card, .service-panel, .testimonial-card, .mega-dropdown');
    spotCards.forEach(card => {
      card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        card.style.setProperty('--mouse-x', `${x}px`);
        card.style.setProperty('--mouse-y', `${y}px`);
      });
    });

    // DRAW TIMELINE PROCESS ANIMATION
    const processTimeline = document.querySelector('.process-timeline');
    if (processTimeline) {
      window.addEventListener('scroll', () => {
        const timelineRect = processTimeline.getBoundingClientRect();
        const windowHeight = window.innerHeight;
        
        // Calculate how much of the timeline is visible in viewport
        let percent = 0;
        if (timelineRect.top < windowHeight) {
          const distanceScrolled = windowHeight - timelineRect.top;
          percent = Math.min(100, Math.max(0, (distanceScrolled / (timelineRect.height + windowHeight * 0.2)) * 100));
        }
        processTimeline.style.setProperty('--timeline-progress', `${percent}%`);
      });
    }

  </script>
</body>
</html>"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated index.html")
