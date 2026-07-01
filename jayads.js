/* =====================================================
   JAYADS — Main JS
   ===================================================== */
'use strict';

document.addEventListener('DOMContentLoaded', () => {

  /* ── SCROLL PROGRESS BAR ── */
  const bar = document.getElementById('scroll-bar');
  if (bar) {
    window.addEventListener('scroll', () => {
      const h = document.documentElement;
      const pct = (h.scrollTop / (h.scrollHeight - h.clientHeight)) * 100;
      bar.style.width = pct + '%';
    }, { passive: true });
  }

  /* ── CUSTOM CURSOR ── */
  const dot  = document.getElementById('cursor-dot');
  const ring = document.getElementById('cursor-ring');
  if (dot && ring && window.matchMedia('(hover: hover)').matches) {
    let mx = 0, my = 0, rx = 0, ry = 0;
    window.addEventListener('mousemove', e => { mx = e.clientX; my = e.clientY; });
    function animCursor() {
      dot.style.left  = mx + 'px';
      dot.style.top   = my + 'px';
      rx += (mx - rx) * 0.12;
      ry += (my - ry) * 0.12;
      ring.style.left = rx + 'px';
      ring.style.top  = ry + 'px';
      requestAnimationFrame(animCursor);
    }
    animCursor();
    // Expand ring on interactive elements
    document.querySelectorAll('a, button, [role="button"], .service-item, .ig-item').forEach(el => {
      el.addEventListener('mouseenter', () => {
        ring.style.width  = '60px';
        ring.style.height = '60px';
      });
      el.addEventListener('mouseleave', () => {
        ring.style.width  = '36px';
        ring.style.height = '36px';
      });
    });
  }

  /* ── NAV SCROLL EFFECT ── */
  const nav = document.getElementById('nav');
  if (nav) {
    const onScroll = () => nav.classList.toggle('scrolled', window.scrollY > 40);
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ── HAMBURGER ── */
  const ham  = document.getElementById('ham');
  const mob  = document.getElementById('mob-menu');
  if (ham && mob) {
    ham.addEventListener('click', () => {
      const open = mob.classList.toggle('open');
      ham.setAttribute('aria-expanded', open);
      mob.setAttribute('aria-hidden', !open);
    });
    mob.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => {
        mob.classList.remove('open');
        ham.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* ── FADE-IN ON SCROLL ── */
  const fadeEls = document.querySelectorAll('.fade');
  if (fadeEls.length) {
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.12 });
    fadeEls.forEach(el => {
      // If already in viewport on page load, show immediately
      const rect = el.getBoundingClientRect();
      if (rect.top < window.innerHeight && rect.bottom > 0) {
        el.classList.add('in');
      } else {
        io.observe(el);
      }
    });
  }

  /* ── COUNTERS ── */
  const counters = document.querySelectorAll('.counter');
  if (counters.length) {
    const cntObs = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        const el = entry.target;
        const target = parseInt(el.dataset.t, 10);
        const dur = 1600;
        const start = performance.now();
        const step = now => {
          const p = Math.min((now - start) / dur, 1);
          const ease = 1 - Math.pow(1 - p, 3);
          el.textContent = Math.round(ease * target).toLocaleString();
          if (p < 1) requestAnimationFrame(step);
        };
        requestAnimationFrame(step);
        cntObs.unobserve(el);
      });
    }, { threshold: 0.5 });
    counters.forEach(c => cntObs.observe(c));
  }

  /* ── REEL VIDEO HOVER PREVIEW ── */
  const igItems = document.querySelectorAll('.ig-item');
  igItems.forEach(item => {
    const vid = item.querySelector('video');
    if (!vid) return;
    item.addEventListener('mouseenter', () => {
      vid.play().catch(() => {});
    });
    item.addEventListener('mouseleave', () => {
      vid.pause();
      vid.currentTime = 0;
    });
  });

  /* ── REEL LIGHTBOX MODAL ── */
  const modal      = document.getElementById('reels-modal');
  const modalVid   = document.getElementById('reels-modal-video');
  const modalCap   = document.getElementById('reels-modal-caption');
  const closeBtn   = document.getElementById('reels-modal-close');
  const prevBtn    = document.getElementById('reels-prev');
  const nextBtn    = document.getElementById('reels-next');

  // Build index of reel items (exclude promo card)
  const reelItems = [...document.querySelectorAll('.ig-item[data-index]')];
  let currentIdx  = 0;

  function openModal(idx) {
    if (!modal || !modalVid) return;
    currentIdx = idx;
    const item   = reelItems[idx];
    const vid    = item.querySelector('video');
    const cap    = item.querySelector('.reel-caption-bar');
    modalVid.src = vid ? vid.src : '';
    if (modalCap) modalCap.textContent = cap ? cap.textContent : '';
    modal.classList.add('open');
    document.body.style.overflow = 'hidden';
    modalVid.play().catch(() => {});
  }

  function closeModal() {
    if (!modal) return;
    modal.classList.remove('open');
    document.body.style.overflow = '';
    if (modalVid) { modalVid.pause(); modalVid.src = ''; }
  }

  reelItems.forEach((item, idx) => {
    item.addEventListener('click', () => openModal(idx));
    item.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openModal(idx); } });
  });

  if (closeBtn) closeBtn.addEventListener('click', closeModal);
  if (modal) {
    modal.addEventListener('click', e => { if (e.target === modal || e.target === modal.querySelector('.reels-modal-wrapper')) closeModal(); });
  }
  if (prevBtn) prevBtn.addEventListener('click', () => openModal((currentIdx - 1 + reelItems.length) % reelItems.length));
  if (nextBtn) nextBtn.addEventListener('click', () => openModal((currentIdx + 1) % reelItems.length));

  document.addEventListener('keydown', e => {
    if (!modal || !modal.classList.contains('open')) return;
    if (e.key === 'Escape') closeModal();
    if (e.key === 'ArrowLeft') openModal((currentIdx - 1 + reelItems.length) % reelItems.length);
    if (e.key === 'ArrowRight') openModal((currentIdx + 1) % reelItems.length);
  });

  /* ── CLIENT LOGO MARQUEE ── */
  const row1 = [
    { src: 'images/Logos/A23.webp', alt: 'A23' },
    { src: 'images/Logos/Abbott_Laboratories_logo.svg', alt: 'Abbott' },
    { src: 'images/Logos/Boost.webp', alt: 'Boost' },
    { src: 'images/Logos/Complan_2.webp', alt: 'Complan' },
    { src: 'images/Logos/DAC.webp', alt: 'DAC' },
    { src: 'images/Logos/Dabur-Logo.wine.webp', alt: 'Dabur' },
    { src: 'images/Logos/Disney+_Hotstar_logo.svg', alt: 'Disney+ Hotstar' },
    { src: 'images/Logos/Godrej_Logo.svg.webp', alt: 'Godrej' },
    { src: 'images/Logos/Head_Shoulders_Logo.svg', alt: 'Head & Shoulders' },
    { src: 'images/Logos/Kotak_Mahindra_Bank_logo.svg.webp', alt: 'Kotak Mahindra' },
    { src: 'images/Logos/LG.webp', alt: 'LG' },
    { src: 'images/Logos/MG motors logo.webp', alt: 'MG Motors' },
    { src: 'images/Logos/MTR logo.webp', alt: 'MTR' },
    { src: 'images/Logos/ajio.webp', alt: 'Ajio' },
    { src: 'images/Logos/apollo.webp', alt: 'Apollo' },
    { src: 'images/Logos/samsung.webp', alt: 'Samsung' },
  ];
  const row2 = [
    { src: 'images/Logos/duroflex.webp', alt: 'Duroflex' },
    { src: 'images/Logos/freshtohome.webp', alt: 'FreshToHome' },
    { src: 'images/Logos/horlicks.webp', alt: 'Horlicks' },
    { src: 'images/Logos/jio.webp', alt: 'Jio' },
    { src: 'images/Logos/kellogs.svg', alt: 'Kelloggs' },
    { src: 'images/Logos/mamaearth.webp', alt: 'Mamaearth' },
    { src: 'images/Logos/meesho.webp', alt: 'Meesho' },
    { src: 'images/Logos/myntra.svg', alt: 'Myntra' },
    { src: 'images/Logos/nestle logo png.webp', alt: 'Nestle' },
    { src: 'images/Logos/oreo.webp', alt: 'Oreo' },
    { src: 'images/Logos/pantene.webp', alt: 'Pantene' },
    { src: 'images/Logos/prime video.webp', alt: 'Prime Video' },
    { src: 'images/Logos/reliance digital.webp', alt: 'Reliance Digital' },
    { src: 'images/Logos/saffola.webp', alt: 'Saffola' },
    { src: 'images/Logos/spotify.webp', alt: 'Spotify' },
    { src: 'images/Logos/tanishq.webp', alt: 'Tanishq' },
  ];
  const row3 = [
    { src: 'images/Logos/parachute.webp', alt: 'Parachute' },
    { src: 'images/Logos/plum.webp', alt: 'Plum' },
    { src: 'images/Logos/surf excel.webp', alt: 'Surf Excel' },
    { src: 'images/Logos/tata tea.webp', alt: 'Tata Tea' },
    { src: 'images/Logos/titan.webp', alt: 'Titan' },
    { src: 'images/Logos/uber.webp', alt: 'Uber' },
    { src: 'images/Logos/volini.webp', alt: 'Volini' },
    { src: 'images/Logos/wow skincare.webp', alt: 'Wow Skincare' },
    { src: 'images/Logos/zee tv.svg', alt: 'Zee TV' },
    { src: 'images/Logos/snapchat.webp', alt: 'Snapchat' },
    { src: 'images/Logos/sunfeast.webp', alt: 'Sunfeast' },
    { src: 'images/Logos/starhealth.webp', alt: 'Star Health' },
    { src: 'images/Logos/bata logo.webp', alt: 'Bata' },
    { src: 'images/Logos/berger paints logo.webp', alt: 'Berger Paints' },
    { src: 'images/Logos/cinthol.webp', alt: 'Cinthol' },
    { src: 'images/Logos/dettol.webp', alt: 'Dettol' },
  ];

  function populateMarquee(id, logos) {
    const track = document.getElementById(id);
    if (!track) return;
    [...logos, ...logos].forEach(logo => {
      const wrap = document.createElement('div');
      wrap.className = 'logo-item';
      const img = document.createElement('img');
      img.src = logo.src; img.alt = logo.alt; img.loading = 'lazy';
      img.onerror = () => wrap.style.display = 'none';
      wrap.appendChild(img);
      track.appendChild(wrap);
    });
  }
  populateMarquee('marquee-track-1', row1);
  populateMarquee('marquee-track-2', row2);
  populateMarquee('marquee-track-3', row3);

  /* ── CONTACT FORM ── */
  const form     = document.getElementById('c-form');
  const submitBtn = document.getElementById('cf-submit');
  if (form && submitBtn) {
    form.addEventListener('submit', async e => {
      e.preventDefault();
      const span = submitBtn.querySelector('span:first-child');
      submitBtn.disabled = true;
      if (span) span.textContent = 'Sending…';
      try {
        const res = await fetch(form.action, {
          method: 'POST',
          body: new FormData(form),
          headers: { Accept: 'application/json' },
        });
        if (res.ok) {
          if (span) span.textContent = 'Message Sent ✓';
          form.reset();
        } else {
          throw new Error('Failed');
        }
      } catch {
        if (span) span.textContent = 'Error — try again';
        submitBtn.disabled = false;
      }
    });
  }

  /* ── BACK TO TOP ── */
  const btt = document.getElementById('btt');
  if (btt) {
    window.addEventListener('scroll', () => btt.classList.toggle('show', window.scrollY > 400), { passive: true });
    btt.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
  }

});
