import os

visual_enhancements = """
/* ==========================================================================
   VISUAL ENHANCEMENTS (21st.dev / Modern Agency Aesthetic)
   ========================================================================== */

/* 1. Subtle Dot-Matrix Background & Floating Ambient Orbs */
body {
  position: relative;
  background-image: radial-gradient(rgba(255, 255, 255, 0.04) 1px, transparent 1px);
  background-size: 24px 24px;
}

body::before, body::after {
  content: "";
  position: fixed;
  width: 60vw;
  height: 60vw;
  border-radius: 50%;
  z-index: -1;
  filter: blur(140px);
  pointer-events: none;
  animation: orbFloat 25s infinite alternate ease-in-out;
  opacity: 0.12;
}
body::before {
  top: -20%; left: -10%;
  background: radial-gradient(circle, var(--accent-gold), transparent 70%);
}
body::after {
  bottom: -20%; right: -10%;
  background: radial-gradient(circle, #5b32ff, transparent 70%); /* subtle deep purple for depth */
  animation-delay: -12s;
}
@keyframes orbFloat {
  0% { transform: translate(0, 0) scale(1); }
  100% { transform: translate(10vw, 5vh) scale(1.1); }
}

/* 2. Glassmorphism Upgrades */
.site-header {
  background: rgba(30, 41, 59, 0.4) !important; /* more transparent */
  backdrop-filter: blur(24px) saturate(180%) !important;
  -webkit-backdrop-filter: blur(24px) saturate(180%) !important;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06) !important;
}
.site-header.scrolled {
  background: rgba(30, 41, 59, 0.7) !important;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4) !important;
}
.mega-dropdown {
  background: rgba(20, 27, 41, 0.85) !important;
  backdrop-filter: blur(30px) saturate(200%) !important;
  -webkit-backdrop-filter: blur(30px) saturate(200%) !important;
  border: 1px solid rgba(255,255,255,0.08) !important;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5) !important;
}

/* 3. Typography Gradients */
.hero-heading, .section-heading, h1 {
  background: linear-gradient(135deg, #ffffff 0%, var(--accent-gold) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  text-shadow: 0 0 40px rgba(229, 157, 44, 0.15); /* very faint ambient glow */
}

/* 4. Micro-Interactions (Cards & Buttons) */
.service-detail-block, .work-card, .visual-card {
  transition: all 0.4s var(--ease-out-expo) !important;
  border: 1px solid rgba(255,255,255,0.04);
}
.service-detail-block:hover, .work-card:hover, .visual-card:hover {
  transform: translateY(-6px);
  border-color: rgba(229, 157, 44, 0.4);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4), 0 0 20px rgba(229, 157, 44, 0.15) !important;
}

.btn-primary, .hero-book-btn {
  transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
  position: relative;
  overflow: hidden;
  box-shadow: 0 4px 15px rgba(229, 157, 44, 0.2);
}
.btn-primary:hover, .hero-book-btn:hover {
  transform: scale(1.03) translateY(-2px);
  box-shadow: 0 10px 30px rgba(229, 157, 44, 0.4);
}
"""

with open('styles.css', 'a', encoding='utf-8') as f:
    f.write(visual_enhancements)
