import os

def build_head(title):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="JayAds provides cinematic ad films, performance-grade social commerce campaigns, and high-performance web experiences." />
  <link rel="icon" type="image/png" href="favicon.png" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Playfair+Display:ital,wght@0,700;0,800;1,700;1,800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="styles.css" />
  <style>
    :root {{
      --clr-pearl: #EBDDC5;
      --clr-police-blue: #2E4365;
      --clr-marigold: #E59D2C;
      --clr-buff: #F3D58D;
      --clr-citrine: #8A3B08;
    }}
    .bg-pearl {{ background-color: var(--clr-pearl); color: var(--clr-police-blue); }}
    .bg-police-blue {{ background-color: var(--clr-police-blue); color: var(--clr-pearl); }}
    .bg-marigold {{ background-color: var(--clr-marigold); color: var(--clr-police-blue); }}
    .bg-buff {{ background-color: var(--clr-buff); color: var(--clr-citrine); }}
    .bg-citrine {{ background-color: var(--clr-citrine); color: var(--clr-pearl); }}
    
    .massive-section {{
      padding: 140px 5%;
      position: relative;
      overflow: hidden;
    }}
    
    .section-title-mega {{
      font-size: clamp(3rem, 5vw, 6rem);
      font-weight: 900;
      line-height: 1.05;
      margin-bottom: 40px;
      letter-spacing: -0.03em;
    }}
    .section-desc-mega {{
      font-size: clamp(1.2rem, 2vw, 1.8rem);
      line-height: 1.6;
      max-width: 900px;
      margin-bottom: 80px;
      opacity: 0.9;
      font-weight: 400;
    }}
    
    /* Bento Grid System */
    .bento-grid {{
      display: grid;
      grid-template-columns: repeat(12, 1fr);
      gap: 30px;
      max-width: 1400px;
      margin: 0 auto;
    }}
    .bento-item {{
      background: rgba(255,255,255,0.06);
      border: 1px solid rgba(255,255,255,0.1);
      border-radius: 32px;
      padding: 50px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: transform 0.4s cubic-bezier(0.165, 0.84, 0.44, 1), box-shadow 0.4s ease;
      backdrop-filter: blur(12px);
    }}
    .bento-item:hover {{
      transform: translateY(-8px);
      box-shadow: 0 30px 60px rgba(0,0,0,0.15);
    }}
    .bg-pearl .bento-item, .bg-buff .bento-item, .bg-marigold .bento-item {{
      background: rgba(0,0,0,0.04);
      border-color: rgba(0,0,0,0.08);
      box-shadow: 0 10px 30px rgba(0,0,0,0.03);
    }}
    .bg-pearl .bento-item:hover, .bg-buff .bento-item:hover, .bg-marigold .bento-item:hover {{
      box-shadow: 0 30px 60px rgba(0,0,0,0.08);
    }}
    
    .bento-col-12 {{ grid-column: span 12; }}
    .bento-col-8 {{ grid-column: span 8; }}
    .bento-col-4 {{ grid-column: span 4; }}
    .bento-col-6 {{ grid-column: span 6; }}
    .bento-col-3 {{ grid-column: span 3; }}
    .bento-col-9 {{ grid-column: span 9; }}
    .bento-col-7 {{ grid-column: span 7; }}
    .bento-col-5 {{ grid-column: span 5; }}
    
    @media (max-width: 1024px) {{
      .bento-col-8, .bento-col-4, .bento-col-6, .bento-col-3, .bento-col-9, .bento-col-7, .bento-col-5 {{ grid-column: span 12; }}
    }}
    
    .bento-tag {{
      display: inline-block;
      padding: 8px 16px;
      border-radius: 50px;
      font-size: 0.9rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1.5px;
      margin-bottom: 30px;
      align-self: flex-start;
      background: rgba(255,255,255,0.15);
    }}
    .bg-pearl .bento-tag, .bg-buff .bento-tag, .bg-marigold .bento-tag {{
      background: rgba(0,0,0,0.1);
    }}
    
    .bento-item h3 {{
      font-size: clamp(2rem, 3vw, 3rem);
      font-weight: 800;
      margin-bottom: 24px;
      line-height: 1.1;
      letter-spacing: -0.02em;
    }}
    .bento-item p {{
      font-size: 1.25rem;
      line-height: 1.7;
      opacity: 0.85;
      margin-bottom: 30px;
    }}
    .bento-stat {{
      font-size: clamp(3rem, 5vw, 6rem);
      font-weight: 900;
      line-height: 1;
      margin-bottom: 10px;
      letter-spacing: -0.05em;
    }}
    .bento-stat-desc {{
      font-size: 1.2rem;
      font-weight: 600;
      opacity: 0.8;
      text-transform: uppercase;
      letter-spacing: 1px;
    }}
    .bento-list {{
      list-style: none;
      padding: 0;
      margin: 0;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }}
    .bento-list li {{
      position: relative;
      padding-left: 36px;
      font-size: 1.2rem;
      font-weight: 600;
      line-height: 1.4;
    }}
    .bento-list li::before {{
      content: '→';
      position: absolute;
      left: 0;
      top: 0;
      font-weight: 900;
      color: inherit;
      opacity: 0.5;
    }}
    .bento-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      border-radius: 16px;
      margin-top: 30px;
    }}
    .bento-img-full {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      border-radius: 16px;
      position: absolute;
      top: 0;
      left: 0;
      z-index: -1;
      opacity: 0.6;
    }}
    .has-bg-img {{
      position: relative;
      overflow: hidden;
    }}
  </style>
</head>
<body class="jayads-body">
  <header class="site-header" id="site-header" style="position: sticky; top: 0; z-index: 1000; background: rgba(46, 67, 101, 0.95); backdrop-filter: blur(10px); padding: 20px 5%; border-bottom: 1px solid rgba(255,255,255,0.1);">
    <div class="header-inner" style="display: flex; justify-content: space-between; align-items: center; max-width: 1400px; margin: 0 auto;">
      <a href="index.html" class="logo" aria-label="JayAds Home" style="font-size: 1.8rem; font-weight: 900; color: var(--clr-pearl); text-decoration: none; letter-spacing: -1px;">
        <span class="logo-accent" style="color: var(--clr-marigold);">Jay</span>Ads
      </a>
      <nav class="nav-links" id="nav-links" role="navigation" style="display: flex; gap: 40px; align-items: center;">
        <a href="services.html" style="color: var(--clr-pearl); text-decoration: none; font-weight: 600; font-size: 1.1rem; transition: color 0.3s;">Services</a>
        <a href="work.html" style="color: var(--clr-pearl); text-decoration: none; font-weight: 600; font-size: 1.1rem; transition: color 0.3s;">Our Work</a>
        <a href="about.html" style="color: var(--clr-pearl); text-decoration: none; font-weight: 600; font-size: 1.1rem; transition: color 0.3s;">About &amp; Process</a>
        <a href="contact.html" style="color: var(--clr-pearl); text-decoration: none; font-weight: 600; font-size: 1.1rem; transition: color 0.3s;">Contact</a>
      </nav>
      <a href="contact.html" class="nav-cta desktop-only" style="background: var(--clr-marigold); color: var(--clr-police-blue); padding: 12px 24px; border-radius: 50px; font-weight: 800; text-decoration: none; transition: transform 0.3s;">Book a Call</a>
    </div>
  </header>
'''

def build_footer():
    return '''
  <footer class="site-footer" style="background-color: var(--clr-police-blue); color: var(--clr-pearl); padding: 120px 5% 60px; text-align: center; border-top: 1px solid rgba(235, 221, 197, 0.1);">
    <h2 style="font-size: clamp(2.5rem, 4vw, 4.5rem); margin-bottom: 24px; font-weight: 900; letter-spacing: -0.03em;">Ready to dominate your market?</h2>
    <p style="font-size: clamp(1.2rem, 2vw, 1.5rem); margin-bottom: 50px; opacity: 0.8; max-width: 600px; margin-left: auto; margin-right: auto;">Join the elite brands partnering with JayAds for unfair creative advantages.</p>
    <a href="contact.html" style="display: inline-block; padding: 24px 50px; background-color: var(--clr-marigold); color: var(--clr-police-blue); text-decoration: none; font-weight: 900; border-radius: 50px; font-size: 1.3rem; transition: transform 0.3s; box-shadow: 0 10px 30px rgba(229, 157, 44, 0.3);">Start Your Project Now</a>
    
    <div style="margin-top: 100px; padding-top: 40px; border-top: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between; align-items: center; max-width: 1400px; margin-left: auto; margin-right: auto; flex-wrap: wrap; gap: 20px;">
      <div style="font-weight: 800; font-size: 1.5rem; letter-spacing: -1px;">
        <span style="color: var(--clr-marigold);">Jay</span>Ads
      </div>
      <div style="opacity: 0.6; font-size: 1rem; font-weight: 500;">
        &copy; 2026 JayAds. All rights reserved. Shot in the morning. Delivered by 4 PM.
      </div>
    </div>
  </footer>
</body>
</html>
'''

# Build Services
services_html = build_head("Our Services | JayAds") + '''
  <section class="massive-section bg-police-blue">
    <div class="bento-grid" style="margin-bottom: 60px;">
      <div class="bento-item bento-col-12" style="padding: 100px 50px; text-align: center; border: none; background: transparent; box-shadow: none;">
        <h1 class="section-title-mega" style="font-size: clamp(4rem, 8vw, 8rem); margin-bottom: 30px; text-transform: uppercase;">Creative that<br><span style="color: var(--clr-marigold);">Performs.</span> At Scale.</h1>
        <p class="section-desc-mega" style="margin: 0 auto; font-size: clamp(1.4rem, 2vw, 2rem);">We are an elite, full-stack creative and growth powerhouse. We don't just make pretty pictures. We engineer scalable revenue engines through cinematic video, rapid-fire social commerce, and high-converting web architecture.</p>
      </div>
    </div>
    
    <div class="bento-grid">
      <div class="bento-item bento-col-8 has-bg-img" style="min-height: 400px; background: var(--clr-citrine); color: var(--clr-pearl); border: none;">
        <span class="bento-tag">The JayAds Advantage</span>
        <h3 style="font-size: 3.5rem;">Faster than an agency.<br>Better than in-house.</h3>
        <p style="font-size: 1.5rem; max-width: 600px;">We’ve condensed the traditional 3-week agency bloated timeline into a deadly 48-hour sprint. Top 1% creative talent directly integrated into your slack channel.</p>
      </div>
      <div class="bento-item bento-col-4" style="background: var(--clr-marigold); color: var(--clr-police-blue); border: none; justify-content: center; align-items: center; text-align: center;">
        <div class="bento-stat">12x</div>
        <div class="bento-stat-desc">Faster Turnaround</div>
        <div style="margin-top: 30px; width: 100%; height: 2px; background: rgba(0,0,0,0.1);"></div>
        <div class="bento-stat" style="margin-top: 30px;">40%</div>
        <div class="bento-stat-desc">Lower Customer Acquisition Cost</div>
      </div>
    </div>
  </section>

  <section class="massive-section bg-pearl" id="ad-films">
    <h2 class="section-title-mega">Cinematic Ad Films <br>&amp; Video Production</h2>
    <p class="section-desc-mega">Stop scrolling. Start converting. We bring Hollywood-level production quality to digital performance marketing. TV-ready commercials built for the Instagram generation.</p>
    
    <div class="bento-grid">
      <div class="bento-item bento-col-7">
        <span class="bento-tag">Deliverables</span>
        <h3>Full-Scale Production</h3>
        <p>From script to screen in days, not months. We handle the entire pipeline internally, eliminating agency middlemen and bloat.</p>
        <ul class="bento-list">
          <li>Concept Development & Scriptwriting</li>
          <li>Talent Sourcing & Location Scouting</li>
          <li>4K/6K Cinematic Principle Photography</li>
          <li>Advanced Color Grading (DaVinci Resolve)</li>
          <li>Sound Design & Custom Audio Mixing</li>
          <li>VFX & Motion Graphics Overlays</li>
        </ul>
      </div>
      
      <div class="bento-item bento-col-5 bg-police-blue" style="color: var(--clr-pearl);">
        <span class="bento-tag" style="background: rgba(255,255,255,0.1);">The Stack</span>
        <h3>We shoot on the best.</h3>
        <div class="bento-grid" style="grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 20px;">
          <div>
            <div style="font-weight: 900; font-size: 2rem;">ARRI</div>
            <p style="font-size: 0.9rem; opacity: 0.7;">Alexa Mini LF</p>
          </div>
          <div>
            <div style="font-weight: 900; font-size: 2rem;">RED</div>
            <p style="font-size: 0.9rem; opacity: 0.7;">V-Raptor 8K</p>
          </div>
          <div>
            <div style="font-weight: 900; font-size: 2rem;">Sony</div>
            <p style="font-size: 0.9rem; opacity: 0.7;">FX9 & FX6 Series</p>
          </div>
          <div>
            <div style="font-weight: 900; font-size: 2rem;">Aputure</div>
            <p style="font-size: 0.9rem; opacity: 0.7;">Pro Lighting Grid</p>
          </div>
        </div>
      </div>

      <div class="bento-item bento-col-12">
        <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 40px;">
          <div style="flex: 1; min-width: 300px;">
            <h3>The "Shot by 10 AM, Live by 4 PM" Guarantee</h3>
            <p>Our proprietary on-set DIT and real-time editing workflows mean we can cut variations of your ad while the cameras are still rolling. Immediate turnaround for rapid A/B testing.</p>
          </div>
          <div style="flex: 1; min-width: 300px; display: flex; gap: 20px;">
             <div style="flex: 1; background: var(--clr-buff); padding: 30px; border-radius: 20px; text-align: center;">
               <div style="font-size: 3rem; font-weight: 900; color: var(--clr-citrine);">100+</div>
               <div style="font-weight: 700; color: var(--clr-police-blue);">Ads Shipped</div>
             </div>
             <div style="flex: 1; background: var(--clr-marigold); padding: 30px; border-radius: 20px; text-align: center;">
               <div style="font-size: 3rem; font-weight: 900; color: var(--clr-police-blue);">15M+</div>
               <div style="font-weight: 700; color: var(--clr-police-blue);">Views Generated</div>
             </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="massive-section bg-marigold" id="social">
    <h2 class="section-title-mega">Social Commerce <br>&amp; Performance Ads</h2>
    <p class="section-desc-mega">We build creative that algorithms love and humans click. Stop guessing what works and start testing at scale with our high-volume performance creative engine.</p>
    
    <div class="bento-grid">
      <div class="bento-item bento-col-4 bg-police-blue" style="color: var(--clr-pearl);">
        <span class="bento-tag">Volume</span>
        <h3>Creative Fatigue is Dead</h3>
        <p>You can't scale a Meta or TikTok ad account with one video a month. We deliver batches of 15, 30, or 50 ad variations per sprint.</p>
        <div class="bento-stat" style="margin-top: 40px;">300%</div>
        <div class="bento-stat-desc">Avg. ROAS Increase</div>
      </div>
      
      <div class="bento-item bento-col-8">
        <span class="bento-tag">Framework</span>
        <h3>The Anatomy of a Winning Ad</h3>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 30px; margin-top: 20px;">
          <div>
            <h4 style="font-size: 1.5rem; font-weight: 800; margin-bottom: 10px;">1. The 3-Second Hook</h4>
            <p style="font-size: 1rem; opacity: 0.8;">Visual interruption patterns designed specifically to halt the thumb-scroll immediately.</p>
          </div>
          <div>
            <h4 style="font-size: 1.5rem; font-weight: 800; margin-bottom: 10px;">2. Native Integration</h4>
            <p style="font-size: 1rem; opacity: 0.8;">UGC-style content that looks organic to the platform, avoiding the "banner blindness" effect.</p>
          </div>
          <div>
            <h4 style="font-size: 1.5rem; font-weight: 800; margin-bottom: 10px;">3. The Value Wedge</h4>
            <p style="font-size: 1rem; opacity: 0.8;">Rapid problem-agitation-solution frameworks that compress buying decisions into seconds.</p>
          </div>
          <div>
            <h4 style="font-size: 1.5rem; font-weight: 800; margin-bottom: 10px;">4. Frictionless CTA</h4>
            <p style="font-size: 1rem; opacity: 0.8;">Direct-response psychological triggers that command immediate off-platform action.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="massive-section bg-citrine" id="web">
    <h2 class="section-title-mega">Web Architecture <br>&amp; Organic Growth</h2>
    <p class="section-desc-mega">Traffic without conversion is just server cost. We build insanely fast, beautifully structured web experiences that turn visitors into evangelical customers.</p>
    
    <div class="bento-grid">
      <div class="bento-item bento-col-12" style="background: var(--clr-police-blue); color: var(--clr-pearl);">
        <div style="display: flex; gap: 60px; align-items: center; flex-wrap: wrap;">
          <div style="flex: 1; min-width: 300px;">
            <span class="bento-tag">Tech Stack</span>
            <h3>Next-Gen Infrastructure</h3>
            <p>We abandoned slow, bloated WordPress sites years ago. We build on modern JavaScript frameworks to achieve perfect 100/100 Lighthouse scores.</p>
            <ul class="bento-list" style="margin-top: 30px;">
              <li>React / Next.js Frontends</li>
              <li>Headless CMS (Sanity, Contentful)</li>
              <li>Global Edge CDN Deployment</li>
              <li>Sub-second LCP and TTI Metrics</li>
            </ul>
          </div>
          <div style="flex: 1; min-width: 300px; display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
             <div style="background: rgba(255,255,255,0.05); padding: 30px; border-radius: 20px; text-align: center; border: 1px solid rgba(255,255,255,0.1);">
               <div style="font-size: 2.5rem; font-weight: 900; color: var(--clr-marigold);">100</div>
               <div style="font-size: 0.9rem; font-weight: 700; text-transform: uppercase;">Lighthouse Score</div>
             </div>
             <div style="background: rgba(255,255,255,0.05); padding: 30px; border-radius: 20px; text-align: center; border: 1px solid rgba(255,255,255,0.1);">
               <div style="font-size: 2.5rem; font-weight: 900; color: var(--clr-marigold);">&lt;0.8s</div>
               <div style="font-size: 0.9rem; font-weight: 700; text-transform: uppercase;">Load Time</div>
             </div>
             <div style="background: rgba(255,255,255,0.05); padding: 30px; border-radius: 20px; text-align: center; border: 1px solid rgba(255,255,255,0.1);">
               <div style="font-size: 2.5rem; font-weight: 900; color: var(--clr-marigold);">+65%</div>
               <div style="font-size: 0.9rem; font-weight: 700; text-transform: uppercase;">Conv. Rate</div>
             </div>
             <div style="background: rgba(255,255,255,0.05); padding: 30px; border-radius: 20px; text-align: center; border: 1px solid rgba(255,255,255,0.1);">
               <div style="font-size: 2.5rem; font-weight: 900; color: var(--clr-marigold);">#1</div>
               <div style="font-size: 0.9rem; font-weight: 700; text-transform: uppercase;">SEO Rankings</div>
             </div>
          </div>
        </div>
      </div>
    </div>
  </section>
''' + build_footer()

# Build Work
work_html = build_head("Our Work | JayAds") + '''
  <section class="massive-section bg-marigold">
    <div class="bento-grid">
      <div class="bento-item bento-col-12" style="padding: 120px 50px; text-align: center; border: none; background: transparent; box-shadow: none;">
        <h1 class="section-title-mega" style="font-size: clamp(4rem, 8vw, 8rem); margin-bottom: 30px; text-transform: uppercase;">Work that <br><span style="color: var(--clr-police-blue);">Stops the Scroll.</span></h1>
        <p class="section-desc-mega" style="margin: 0 auto; font-size: clamp(1.4rem, 2vw, 2rem); color: var(--clr-police-blue);">We don't build portfolios. We build profit engines. Here is a deconstruction of how we've scaled industry leaders through ruthless creative strategy.</p>
      </div>
    </div>
  </section>

  <section class="massive-section bg-police-blue">
    <div class="bento-tag" style="margin-bottom: 40px; font-size: 1.2rem; background: var(--clr-marigold); color: var(--clr-police-blue);">Case Study 01</div>
    <h2 class="section-title-mega" style="margin-bottom: 10px;">Scaling a Global D2C Titan</h2>
    <p class="section-desc-mega" style="margin-bottom: 60px; color: var(--clr-pearl); opacity: 0.7;">Fashion & Apparel • Performance Creative • Meta Ads</p>

    <div class="bento-grid">
      <div class="bento-item bento-col-8" style="background: var(--clr-pearl); color: var(--clr-police-blue);">
        <h3>The Challenge</h3>
        <p>The brand had hit a severe plateau at $1M MRR. Creative fatigue on Meta was destroying their CAC. Their internal team couldn't produce high-quality video assets fast enough to feed the algorithm.</p>
        <h3 style="margin-top: 40px;">The Solution</h3>
        <p>JayAds deployed a 4-week "Content Avalanche" strategy. We shot 120 unique video hooks in a single 2-day studio session, mapped to 4 distinct buyer personas. We instituted a modular editing framework allowing us to swap hooks, bodies, and CTAs dynamically.</p>
      </div>
      
      <div class="bento-item bento-col-4" style="background: var(--clr-citrine); color: var(--clr-pearl); display: flex; flex-direction: column; gap: 30px;">
        <div>
          <div class="bento-stat" style="color: var(--clr-marigold);">4.2x</div>
          <div class="bento-stat-desc">Return on Ad Spend</div>
        </div>
        <div>
          <div class="bento-stat" style="color: var(--clr-marigold);">-38%</div>
          <div class="bento-stat-desc">Cost Per Acquisition</div>
        </div>
        <div>
          <div class="bento-stat" style="color: var(--clr-marigold);">$3.4M</div>
          <div class="bento-stat-desc">Revenue Generated (Q3)</div>
        </div>
      </div>

      <div class="bento-item bento-col-12" style="background: transparent; border: none; padding: 0;">
        <div class="bento-grid" style="gap: 20px;">
           <div class="bento-item bento-col-4" style="min-height: 400px; background: #111; position: relative; overflow: hidden;">
             <div style="position: absolute; top: 20px; left: 20px; background: rgba(0,0,0,0.5); padding: 5px 15px; border-radius: 20px; color: #fff; font-weight: bold; z-index: 10;">Hook Var A</div>
             <!-- Mock image container -->
             <div style="width: 100%; height: 100%; background: linear-gradient(45deg, #2E4365, #111); position: absolute; top:0; left:0;"></div>
           </div>
           <div class="bento-item bento-col-4" style="min-height: 400px; background: #111; position: relative; overflow: hidden;">
             <div style="position: absolute; top: 20px; left: 20px; background: rgba(0,0,0,0.5); padding: 5px 15px; border-radius: 20px; color: #fff; font-weight: bold; z-index: 10;">Hook Var B</div>
             <div style="width: 100%; height: 100%; background: linear-gradient(45deg, #8A3B08, #111); position: absolute; top:0; left:0;"></div>
           </div>
           <div class="bento-item bento-col-4" style="min-height: 400px; background: #111; position: relative; overflow: hidden;">
             <div style="position: absolute; top: 20px; left: 20px; background: rgba(0,0,0,0.5); padding: 5px 15px; border-radius: 20px; color: #fff; font-weight: bold; z-index: 10;">Hook Var C</div>
             <div style="width: 100%; height: 100%; background: linear-gradient(45deg, #E59D2C, #111); position: absolute; top:0; left:0;"></div>
           </div>
        </div>
      </div>
    </div>
  </section>

  <section class="massive-section bg-pearl">
    <div class="bento-tag" style="margin-bottom: 40px; font-size: 1.2rem; background: var(--clr-citrine); color: var(--clr-pearl);">Case Study 02</div>
    <h2 class="section-title-mega" style="margin-bottom: 10px;">B2B SaaS Lead Generation</h2>
    <p class="section-desc-mega" style="margin-bottom: 60px; color: var(--clr-police-blue); opacity: 0.7;">Enterprise Tech • Brand Film • Landing Page CRO</p>

    <div class="bento-grid">
      <div class="bento-item bento-col-5" style="background: var(--clr-police-blue); color: var(--clr-pearl);">
        <h3 style="color: var(--clr-marigold);">The Anatomy of the Build</h3>
        <ul class="bento-list" style="margin-top: 30px; gap: 24px;">
          <li><strong style="color: var(--clr-marigold);">Brand Film:</strong> 90-second cinematic manifesto explaining complex API tech through visual metaphors.</li>
          <li><strong style="color: var(--clr-marigold);">Web Build:</strong> Complete redesign of the demo booking flow using Next.js for zero-latency loads.</li>
          <li><strong style="color: var(--clr-marigold);">Distribution:</strong> LinkedIn Account-Based Marketing (ABM) targeting CTOs and VP Engineering.</li>
        </ul>
      </div>
      
      <div class="bento-item bento-col-7" style="background: var(--clr-buff); color: var(--clr-police-blue);">
        <h3>The Result</h3>
        <p>By treating B2B marketing with B2C production values, we shattered industry benchmarks. The brand film achieved a 65% VTR (View-Through Rate) on LinkedIn, driving incredibly high-intent traffic to a newly optimized funnel.</p>
        
        <div style="display: flex; gap: 40px; margin-top: 40px; flex-wrap: wrap;">
          <div>
            <div class="bento-stat" style="color: var(--clr-citrine);">+210%</div>
            <div class="bento-stat-desc">Demo Requests</div>
          </div>
          <div>
            <div class="bento-stat" style="color: var(--clr-citrine);">$12M</div>
            <div class="bento-stat-desc">Pipeline Generated</div>
          </div>
        </div>
      </div>
    </div>
  </section>
  
  <section class="massive-section bg-citrine">
    <div style="text-align: center; margin-bottom: 80px;">
      <h2 class="section-title-mega" style="color: var(--clr-pearl);">The Vault</h2>
      <p class="section-desc-mega" style="color: var(--clr-pearl); margin: 0 auto;">A rapid-fire grid of our recent visual destruction.</p>
    </div>
    
    <div class="bento-grid" style="grid-template-columns: repeat(4, 1fr); gap: 15px;">
       <div class="bento-item" style="grid-column: span 2; min-height: 300px; background: #fff;"></div>
       <div class="bento-item" style="grid-column: span 1; min-height: 300px; background: var(--clr-marigold);"></div>
       <div class="bento-item" style="grid-column: span 1; min-height: 300px; background: var(--clr-police-blue);"></div>
       
       <div class="bento-item" style="grid-column: span 1; min-height: 300px; background: var(--clr-buff);"></div>
       <div class="bento-item" style="grid-column: span 2; min-height: 300px; background: #222;"></div>
       <div class="bento-item" style="grid-column: span 1; min-height: 300px; background: var(--clr-pearl);"></div>
    </div>
  </section>
''' + build_footer()

# Build About
about_html = build_head("About & Process | JayAds") + '''
  <section class="massive-section bg-buff">
    <div class="bento-grid">
      <div class="bento-item bento-col-12" style="padding: 120px 50px; text-align: center; border: none; background: transparent; box-shadow: none;">
        <h1 class="section-title-mega" style="font-size: clamp(4rem, 8vw, 8rem); margin-bottom: 30px; text-transform: uppercase; color: var(--clr-citrine);">Not an Agency.<br><span style="color: var(--clr-police-blue);">An In-House Team.</span></h1>
        <p class="section-desc-mega" style="margin: 0 auto; font-size: clamp(1.4rem, 2vw, 2rem); color: var(--clr-police-blue);">Traditional agencies are slow, bloated, and prioritize awards over revenue. JayAds operates as a specialized, elite strike force integrated directly into your company's bloodstream.</p>
      </div>
    </div>
  </section>

  <section class="massive-section bg-pearl">
    <div class="bento-grid">
      <div class="bento-item bento-col-6" style="background: var(--clr-police-blue); color: var(--clr-pearl);">
        <span class="bento-tag" style="background: var(--clr-marigold); color: var(--clr-police-blue);">Our Philosophy</span>
        <h3>Speed is a feature.<br>Quality is a given.</h3>
        <p>In the digital landscape, the brand that tests the most creatives wins. Period. We have engineered our entire business model around eliminating bottlenecks. No account managers playing telephone. No pointless check-in meetings. Just direct access to elite creators and immediate execution.</p>
        <p>We work exclusively on a subscription or sprint model. You get an entire production studio, post-production house, and performance marketing team for less than the cost of one senior hire.</p>
      </div>
      
      <div class="bento-item bento-col-6 bg-marigold" style="color: var(--clr-police-blue); display: flex; flex-direction: column; justify-content: center;">
        <div style="font-size: 5rem; font-weight: 900; line-height: 1; margin-bottom: 20px;">0%</div>
        <div style="font-size: 2rem; font-weight: 800; margin-bottom: 40px;">Agency Bloat</div>
        
        <div style="font-size: 5rem; font-weight: 900; line-height: 1; margin-bottom: 20px;">100%</div>
        <div style="font-size: 2rem; font-weight: 800;">Direct Execution</div>
      </div>
    </div>
  </section>

  <section class="massive-section bg-police-blue">
    <h2 class="section-title-mega" style="color: var(--clr-pearl); text-align: center; margin-bottom: 80px;">The 48-Hour Sprint Protocol</h2>
    
    <div class="bento-grid">
      <div class="bento-item bento-col-4" style="background: var(--clr-pearl); color: var(--clr-police-blue);">
        <div style="font-size: 3rem; font-weight: 900; color: var(--clr-citrine); margin-bottom: 20px;">T-Minus 0</div>
        <h3>The Briefing</h3>
        <p>We receive your objective via our dedicated Slack channel or Notion portal. Within 2 hours, a strategy framework is approved. No formal meetings required.</p>
      </div>
      
      <div class="bento-item bento-col-4" style="background: var(--clr-buff); color: var(--clr-citrine);">
        <div style="font-size: 3rem; font-weight: 900; color: var(--clr-police-blue); margin-bottom: 20px;">Hour 24</div>
        <h3>Production</h3>
        <p>Cameras are rolling. Whether it's our in-house cyclorama studio or on location, our crew executes the shot list with ruthless efficiency, uploading proxies in real-time.</p>
      </div>
      
      <div class="bento-item bento-col-4" style="background: var(--clr-marigold); color: var(--clr-police-blue);">
        <div style="font-size: 3rem; font-weight: 900; color: var(--clr-pearl); margin-bottom: 20px;">Hour 48</div>
        <h3>Delivery & Launch</h3>
        <p>Color-graded, sound-mixed, and formatted assets hit your inbox. Variations are automatically loaded into your ad accounts for immediate A/B testing.</p>
      </div>
    </div>
  </section>

  <section class="massive-section bg-citrine">
    <div class="bento-grid">
      <div class="bento-item bento-col-12" style="background: var(--clr-pearl); color: var(--clr-police-blue); text-align: center;">
        <h2 class="section-title-mega" style="margin-bottom: 20px;">The Arsenal</h2>
        <p class="section-desc-mega" style="margin: 0 auto 60px;">We own all our gear. We host all our software. No rentals, no delays.</p>
        
        <div class="bento-grid" style="grid-template-columns: repeat(3, 1fr); text-align: left;">
          <div>
            <h4 style="font-size: 1.5rem; font-weight: 800; margin-bottom: 20px; color: var(--clr-citrine);">Camera & Lighting</h4>
            <ul class="bento-list">
              <li>RED V-Raptor 8K VV</li>
              <li>ARRI Alexa Mini</li>
              <li>Sony FX6 / A7SIII Fleet</li>
              <li>Aputure 1200d Pro & Nova Grid</li>
              <li>Atlas Orion Anamorphic Lenses</li>
            </ul>
          </div>
          <div>
            <h4 style="font-size: 1.5rem; font-weight: 800; margin-bottom: 20px; color: var(--clr-citrine);">Post-Production</h4>
            <ul class="bento-list">
              <li>M2 Ultra Mac Studio Network</li>
              <li>DaVinci Resolve Advanced Panels</li>
              <li>Adobe Creative Cloud Enterprise</li>
              <li>Cinema 4D & Unreal Engine 5</li>
              <li>100TB High-Speed NAS</li>
            </ul>
          </div>
          <div>
            <h4 style="font-size: 1.5rem; font-weight: 800; margin-bottom: 20px; color: var(--clr-citrine);">Web & Growth</h4>
            <ul class="bento-list">
              <li>Next.js / React</li>
              <li>Vercel Edge Infrastructure</li>
              <li>Figma Pro (Auto-layout Masters)</li>
              <li>Sanity Headless CMS</li>
              <li>TripleWhale Analytics</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </section>
''' + build_footer()

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(services_html)

with open('work.html', 'w', encoding='utf-8') as f:
    f.write(work_html)

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(about_html)

print("All files generated successfully.")
