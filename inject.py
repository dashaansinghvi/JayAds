idx_content = open('index.html', 'r', encoding='utf-8').read()

new_sections = '''
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
          We measure success purely by bottom-line growth. Here's a snapshot of what happens when you combine elite cinematic creative with ruthless media buying.
        </p>
      </div>

      <div class="services-grid">
        <!-- Case Study 1 -->
        <div class="service-card animate-on-scroll">
          <div class="card-icon">📈</div>
          <span class="card-number">3.8X</span>
          <h3 class="card-title">D2C Apparel Brand</h3>
          <p class="card-description">Scaled from $10k/mo to $150k/mo in 90 days. We completely overhauled their creative stack with cinematic social commerce ads and restructured their Meta buying.</p>
          <div class="card-tags">
            <span class="tag">Meta Ads</span>
            <span class="tag">Ad Films</span>
            <span class="tag">+400% Revenue</span>
          </div>
        </div>

        <!-- Case Study 2 -->
        <div class="service-card animate-on-scroll">
          <div class="card-icon">🔥</div>
          <span class="card-number">$1M+</span>
          <h3 class="card-title">SaaS Platform</h3>
          <p class="card-description">Generated over $1M in enterprise pipeline within 6 months. Executed a complete brand repositioning, high-end explainer videos, and organic SEO architecture.</p>
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
          <div class="adv-icon">🎬</div>
          <h3 class="adv-title">Project Based</h3>
          <p class="adv-desc">Perfect for massive, one-off cinematic ad films, brand identity overhauls, or launch campaigns. Defined scope, fixed timeline, premium delivery.</p>
          <ul style="color: var(--text-secondary); margin-top: 16px; list-style-type: disc; padding-left: 20px; font-size: 0.95rem; line-height: 1.8;">
            <li>TVC & Digital Video Production</li>
            <li>Brand Identity Design</li>
            <li>Web Development Sprints</li>
          </ul>
        </div>

        <!-- Tier 2 -->
        <div class="advantage-card animate-on-scroll">
          <div class="adv-icon">⚡</div>
          <h3 class="adv-title">Hyper-Scale Mode</h3>
          <p class="adv-desc">A monthly retainer where we act as your entire in-house creative and growth department. Continuous ad production, media buying, and CRO.</p>
          <ul style="color: var(--text-secondary); margin-top: 16px; list-style-type: disc; padding-left: 20px; font-size: 0.95rem; line-height: 1.8;">
            <li>Continuous Video Ads Output</li>
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

'''

parts = idx_content.split('<!-- ═══════════════════════════════════════════════════ -->\n  <!-- FINAL CONVERSION CTA')
if len(parts) == 2:
    final_content = parts[0] + new_sections + '<!-- ═══════════════════════════════════════════════════ -->\n  <!-- FINAL CONVERSION CTA' + parts[1]
    open('index.html', 'w', encoding='utf-8').write(final_content)
    print('Injected new sections.')
else:
    print('Failed to find split point')
