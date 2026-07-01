(function () {
    'use strict';

    /* ===================================================
       REELS — Hover play + lightbox
    =================================================== */
    const reelItems = Array.from(document.querySelectorAll('.ig-item'));
    const reelSrcs = reelItems.map(el => el.querySelector('video').src);
    const reelCaptions = reelItems.map(el => el.querySelector('.reel-caption').textContent.trim());
    let currentPlayingVideo = null;
    let currentPlayingItem = null;
    let isModalOpen = false;

    function playGridVideo(item, video) {
        if (currentPlayingVideo && currentPlayingVideo !== video) {
            currentPlayingVideo.pause();
            currentPlayingVideo.load(); // Reset to show the poster
            if (currentPlayingItem) currentPlayingItem.classList.remove('reel-active');
        }
        if (video) {
            video.play().catch(() => { });
            item.classList.add('reel-active');
            currentPlayingVideo = video;
            currentPlayingItem = item;
        } else {
            currentPlayingVideo = null;
            currentPlayingItem = null;
        }
    }

    function pauseGridVideo() {
        if (currentPlayingVideo) {
            currentPlayingVideo.pause();
            currentPlayingVideo.load(); // Reset to show the poster
            if (currentPlayingItem) currentPlayingItem.classList.remove('reel-active');
            currentPlayingVideo = null;
            currentPlayingItem = null;
        }
    }

    // Hover logic (desktop)
    reelItems.forEach((item, i) => {
        const video = item.querySelector('video');

        item.addEventListener('mouseenter', () => {
            if (isModalOpen) return;
            if (currentPlayingVideo !== video) {
                playGridVideo(item, video);
            }
        });

        item.addEventListener('mouseleave', () => {
            if (isModalOpen) return;
            if (currentPlayingVideo === video) {
                pauseGridVideo();
            }
        });

        item.addEventListener('click', () => openModal(i));
        item.addEventListener('keydown', e => {
            if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); openModal(i); }
        });
    });

    // Lightbox logic
    const modal = document.getElementById('reels-modal');
    const modalVideo = document.getElementById('reels-modal-video');
    const modalCaption = document.getElementById('reels-modal-caption');
    const modalClose = document.getElementById('reels-modal-close');
    const prevBtn = document.getElementById('reels-prev');
    const nextBtn = document.getElementById('reels-next');
    let modalIndex = 0;

    function openModal(index) {
        isModalOpen = true;
        pauseGridVideo();
        modalIndex = index;
        const src = reelSrcs[index];
        const caption = reelCaptions[index];
        modalVideo.src = src;
        modalVideo.currentTime = 0;
        modalCaption.textContent = caption;
        modal.classList.add('open');
        document.body.style.overflow = 'hidden';
        modalVideo.play().catch(() => { });
    }

    function closeModal() {
        modalVideo.pause();
        modalVideo.src = '';
        modal.classList.remove('open');
        document.body.style.overflow = '';
        isModalOpen = false;
    }

    modalClose.addEventListener('click', closeModal);
    modal.addEventListener('click', e => {
        if (e.target === modal || e.target.classList.contains('reels-modal-wrapper')) {
            closeModal();
        }
    });

    prevBtn.addEventListener('click', e => {
        e.stopPropagation();
        const prev = (modalIndex - 1 + reelSrcs.length) % reelSrcs.length;
        openModal(prev);
    });

    nextBtn.addEventListener('click', e => {
        e.stopPropagation();
        const next = (modalIndex + 1) % reelSrcs.length;
        openModal(next);
    });

    document.addEventListener('keydown', e => {
        if (!modal.classList.contains('open')) return;
        if (e.key === 'Escape') closeModal();
        if (e.key === 'ArrowLeft') { const p = (modalIndex - 1 + reelSrcs.length) % reelSrcs.length; openModal(p); }
        if (e.key === 'ArrowRight') { const n = (modalIndex + 1) % reelSrcs.length; openModal(n); }
    });



    /* --- NAV scroll & hamburger --- */
    const nav = document.getElementById('nav');
    const ham = document.getElementById('ham');
    const mob = document.getElementById('mob-menu');
    const btt = document.getElementById('btt');

    window.addEventListener('scroll', () => {
        const y = window.scrollY;
        nav.classList.toggle('scrolled', y > 60);
        btt.classList.toggle('vis', y > 500);
    }, { passive: true });

    ham.addEventListener('click', () => {
        ham.classList.toggle('open');
        mob.classList.toggle('open');
        ham.setAttribute('aria-expanded', mob.classList.contains('open'));
        mob.setAttribute('aria-hidden', !mob.classList.contains('open'));
    });
    mob.querySelectorAll('a').forEach(a => {
        a.addEventListener('click', () => {
            ham.classList.remove('open');
            mob.classList.remove('open');
            ham.setAttribute('aria-expanded', 'false');
            mob.setAttribute('aria-hidden', 'true');
        });
    });
    btt.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

    /* --- Smooth scroll for nav links --- */
    document.querySelectorAll('a[href^="#"]').forEach(a => {
        a.addEventListener('click', e => {
            const target = document.querySelector(a.getAttribute('href'));
            if (target) {
                e.preventDefault();
                const top = target.getBoundingClientRect().top + window.pageYOffset - parseInt(getComputedStyle(document.documentElement).getPropertyValue('--nav-h'));
                window.scrollTo({ top, behavior: 'smooth' });
            }
        });
    });

    /* --- Active nav link highlight --- */
    const sectionIds = ['home', 'journey-inner', 'portfolio', 'clients', 'contact'];
    const navLinkMap = {
        'home': document.getElementById('nl-home'),
        'journey-inner': document.getElementById('nl-about'),
        'portfolio': document.getElementById('nl-portfolio'),
        'clients': document.getElementById('nl-clients'),
        'contact': document.getElementById('nl-contact')
    };
    const sectObs = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.id;
                Object.values(navLinkMap).forEach(l => { if (l) l.classList.remove('active'); });
                if (navLinkMap[id]) navLinkMap[id].classList.add('active');
            }
        });
    }, { threshold: 0.25 });
    sectionIds.forEach(id => {
        const el = document.getElementById(id);
        if (el) sectObs.observe(el);
    });

    /* --- Fade-in on scroll --- */
    const fades = document.querySelectorAll('.fade');
    const fadeObs = new IntersectionObserver(entries => {
        entries.forEach(e => {
            if (e.isIntersecting) {
                e.target.classList.add('in');
                // Remove entrance delay classes after transition is complete so they don't delay hover interactions
                setTimeout(() => {
                    e.target.classList.remove('d1', 'd2', 'd3', 'd4');
                }, 1000);
                fadeObs.unobserve(e.target);
            }
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
    fades.forEach(el => fadeObs.observe(el));

    /* --- Cards stack intro fanning animation --- */
    const cardsStack = document.querySelector('.cards-stack');
    if (cardsStack) {
        const stackObs = new IntersectionObserver(entries => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    cardsStack.classList.add('fan-out');
                    // Remove the class after the animation completes so hover transitions are not overridden/interfered with
                    setTimeout(() => {
                        cardsStack.classList.remove('fan-out');
                    }, 2200);
                    stackObs.unobserve(entry.target);
                }
            });
        }, { threshold: 0.15 });
        stackObs.observe(cardsStack);
    }

    /* --- Stats stat-cell bar animation --- */
    const statCellObs = new IntersectionObserver(entries => {
        entries.forEach(e => {
            if (e.isIntersecting) {
                e.target.classList.add('in');
                statCellObs.unobserve(e.target);
            }
        });
    }, { threshold: 0.3 });
    document.querySelectorAll('.stat-cell').forEach(el => statCellObs.observe(el));

    /* --- Counter animation --- */
    const counters = document.querySelectorAll('.counter');
    const cntObs = new IntersectionObserver(entries => {
        entries.forEach(e => {
            if (!e.isIntersecting) return;
            const el = e.target;
            const target = parseInt(el.dataset.t);
            const dur = 1800;
            const start = performance.now();
            function frame(now) {
                const prog = Math.min((now - start) / dur, 1);
                const eased = 1 - Math.pow(1 - prog, 3);
                el.textContent = Math.floor(eased * target).toLocaleString();
                if (prog < 1) requestAnimationFrame(frame);
                else el.textContent = target.toLocaleString();
            }
            requestAnimationFrame(frame);
            cntObs.unobserve(el);
        });
    }, { threshold: 0.5 });
    counters.forEach(c => cntObs.observe(c));

    /* --- Happy Clients Slider Dynamic Population --- */
    const row1Logos = [
        { src: 'images/Logos/A23.webp', alt: 'A23' },
        { src: 'images/Logos/Abbott_Laboratories_logo.svg', alt: 'Abbott Laboratories' },
        { src: 'images/Logos/Boost.webp', alt: 'Boost' },
        { src: 'images/Logos/Complan_2.webp', alt: 'Complan' },
        { src: 'images/Logos/DAC.webp', alt: 'DAC' },
        { src: 'images/Logos/Dabur-Logo.wine.webp', alt: 'Dabur' },
        { src: 'images/Logos/Disney+_Hotstar_logo.svg', alt: 'Disney+ Hotstar' },
        { src: 'images/Logos/Endhanteur logo.webp', alt: 'Enchanteur' },
        { src: 'images/Logos/Godrej_Logo.svg.webp', alt: 'Godrej' },
        { src: 'images/Logos/Head_Shoulders_Logo.svg', alt: 'Head & Shoulders' },
        { src: 'images/Logos/Hershey-Logo.webp', alt: 'Hershey' },
        { src: 'images/Logos/Kotak_Mahindra_Bank_logo.svg.webp', alt: 'Kotak Mahindra' },
        { src: 'images/Logos/LG.webp', alt: 'LG' },
        { src: 'images/Logos/LPU.webp', alt: 'LPU' },
        { src: 'images/Logos/Lever ayush.webp', alt: 'Lever Ayush' },
        { src: 'images/Logos/MG motors logo.webp', alt: 'MG Motors' },
        { src: 'images/Logos/MTR logo.webp', alt: 'MTR' },
        { src: 'images/Logos/McDonald\'s_logo.svg.webp', alt: 'McDonald\'s' },
        { src: 'images/Logos/OPPO_Logo_wiki.webp', alt: 'Oppo' },
        { src: 'images/Logos/Smart_Bazaar_logo.webp', alt: 'Smart Bazaar' },
        { src: 'images/Logos/YTshorts.webp', alt: 'YouTube Shorts' },
        { src: 'images/Logos/ajio.webp', alt: 'Ajio' },
        { src: 'images/Logos/ajmal bismi.webp', alt: 'Ajmal Bismi' },
        { src: 'images/Logos/allout.svg', alt: 'Allout' },
        { src: 'images/Logos/apollo.webp', alt: 'Apollo' },
        { src: 'images/Logos/apollo247.webp', alt: 'Apollo 24/7' },
        { src: 'images/Logos/bata logo.webp', alt: 'Bata' },
        { src: 'images/Logos/berger paints logo.webp', alt: 'Berger Paints' },
        { src: 'images/Logos/big boss 4.webp', alt: 'Bigg Boss' },
        { src: 'images/Logos/bru.webp', alt: 'Bru' },
        { src: 'images/Logos/centerfresh.webp', alt: 'Center Fresh' },
        { src: 'images/Logos/cinthol.webp', alt: 'Cinthol' },
        { src: 'images/Logos/cokestudio.webp', alt: 'Coke Studio' },
        { src: 'images/Logos/dettol.webp', alt: 'Dettol' }
    ];

    const row2Logos = [
        { src: 'images/Logos/duroflex.webp', alt: 'Duroflex' },
        { src: 'images/Logos/freshtohome.webp', alt: 'FreshToHome' },
        { src: 'images/Logos/galaxy.svg', alt: 'Galaxy' },
        { src: 'images/Logos/good knight.webp', alt: 'Good Knight' },
        { src: 'images/Logos/gritzo logo png.webp', alt: 'Gritzo' },
        { src: 'images/Logos/hk vitals.webp', alt: 'HK Vitals' },
        { src: 'images/Logos/horlicks.webp', alt: 'Horlicks' },
        { src: 'images/Logos/imcaffeine.webp', alt: 'mCaffeine' },
        { src: 'images/Logos/indulekha.webp', alt: 'Indulekha' },
        { src: 'images/Logos/jio.webp', alt: 'Jio' },
        { src: 'images/Logos/jiomart.webp', alt: 'JioMart' },
        { src: 'images/Logos/josh.svg', alt: 'Josh' },
        { src: 'images/Logos/jovees.webp', alt: 'Jovees' },
        { src: 'images/Logos/kaleesuwari.webp', alt: 'Kaleesuwari' },
        { src: 'images/Logos/kellogs.svg', alt: 'Kelloggs' },
        { src: 'images/Logos/licious logo png.webp', alt: 'Licious' },
        { src: 'images/Logos/liebherr.webp', alt: 'Liebherr' },
        { src: 'images/Logos/lipton logo.webp', alt: 'Lipton' },
        { src: 'images/Logos/mamaearth.webp', alt: 'Mamaearth' },
        { src: 'images/Logos/mangaldeep logo.webp', alt: 'Mangaldeep' },
        { src: 'images/Logos/meesho.webp', alt: 'Meesho' },
        { src: 'images/Logos/moj.webp', alt: 'Moj' },
        { src: 'images/Logos/muthoot-fincorp-logo.webp', alt: 'Muthoot Fincorp' },
        { src: 'images/Logos/myntra.svg', alt: 'Myntra' },
        { src: 'images/Logos/nature protect.webp', alt: 'Nature Protect' },
        { src: 'images/Logos/nature\'s essense.webp', alt: 'Natures Essence' },
        { src: 'images/Logos/nestle logo png.webp', alt: 'Nestle' },
        { src: 'images/Logos/niyo logo.webp', alt: 'Niyo' },
        { src: 'images/Logos/nushakthi.webp', alt: 'NuShakthi' },
        { src: 'images/Logos/oganic harvest.webp', alt: 'Organic Harvest' },
        { src: 'images/Logos/om shakthy.webp', alt: 'Om Shakthy' },
        { src: 'images/Logos/oreo.webp', alt: 'Oreo' },
        { src: 'images/Logos/oyalo.avif', alt: 'Oyalo' },
        { src: 'images/Logos/pantene.webp', alt: 'Pantene' }
    ];

    const row3Logos = [
        { src: 'images/Logos/parachute.webp', alt: 'Parachute' },
        { src: 'images/Logos/paragon.webp', alt: 'Paragon' },
        { src: 'images/Logos/plum.webp', alt: 'Plum' },
        { src: 'images/Logos/pnb housing.webp', alt: 'PNB Housing' },
        { src: 'images/Logos/poco phone.webp', alt: 'Poco' },
        { src: 'images/Logos/prime video.webp', alt: 'Prime Video' },
        { src: 'images/Logos/pure it logo.webp', alt: 'Pure It' },
        { src: 'images/Logos/reliance digital.webp', alt: 'Reliance Digital' },
        { src: 'images/Logos/renee.webp', alt: 'Renee' },
        { src: 'images/Logos/rummycircle.webp', alt: 'Rummy Circle' },
        { src: 'images/Logos/saffola.webp', alt: 'Saffola' },
        { src: 'images/Logos/samsung.webp', alt: 'Samsung' },
        { src: 'images/Logos/snapchat.webp', alt: 'Snapchat' },
        { src: 'images/Logos/snickers.webp', alt: 'Snickers' },
        { src: 'images/Logos/sodexo logo.svg', alt: 'Sodexo' },
        { src: 'images/Logos/spotify.webp', alt: 'Spotify' },
        { src: 'images/Logos/st ives.webp', alt: 'St Ives' },
        { src: 'images/Logos/starhealth.webp', alt: 'Star Health' },
        { src: 'images/Logos/sunfeast.webp', alt: 'Sunfeast' },
        { src: 'images/Logos/surf excel.webp', alt: 'Surf Excel' },
        { src: 'images/Logos/tanishq.webp', alt: 'Tanishq' },
        { src: 'images/Logos/tata tea.webp', alt: 'Tata Tea' },
        { src: 'images/Logos/tataq.webp', alt: 'Tata Q' },
        { src: 'images/Logos/titan.webp', alt: 'Titan' },
        { src: 'images/Logos/trends.webp', alt: 'Trends' },
        { src: 'images/Logos/tvs emerald logo png.webp', alt: 'TVS Emerald' },
        { src: 'images/Logos/uber.webp', alt: 'Uber' },
        { src: 'images/Logos/urbanrise.webp', alt: 'Urbanrise' },
        { src: 'images/Logos/vanaura.webp', alt: 'Vanaura' },
        { src: 'images/Logos/vanish logo png.webp', alt: 'Vanish' },
        { src: 'images/Logos/volini.webp', alt: 'Volini' },
        { src: 'images/Logos/wow skincare.webp', alt: 'Wow Skincare' },
        { src: 'images/Logos/zee tv.svg', alt: 'Zee TV' }
    ];

    function populateTrack(trackId, logos) {
        const track = document.getElementById(trackId);
        if (!track) return;

        // Duplicate the logos list to make infinite scroll seamless
        const doubleLogos = [...logos, ...logos];

        doubleLogos.forEach(logo => {
            const item = document.createElement('div');
            item.className = 'logo-item';

            const img = document.createElement('img');
            img.src = logo.src;
            img.alt = logo.alt;
            img.loading = 'lazy';
            img.onerror = function () {
                item.style.display = 'none';
            };

            item.appendChild(img);
            track.appendChild(item);
        });
    }

    populateTrack('marquee-track-1', row1Logos);
    populateTrack('marquee-track-2', row2Logos);
    populateTrack('marquee-track-3', row3Logos);



    /* --- Contact form submission --- */
    const cForm = document.getElementById('c-form');
    const cfSubmit = document.getElementById('cf-submit');

    async function submitForm() {
        const btnSpan = cfSubmit.querySelector('span');

        // Set button to sending/progress state
        cfSubmit.disabled = true;
        cfSubmit.className = 'btn btn-primary sending';
        btnSpan.textContent = 'Sending…';

        try {
            const res = await fetch(cForm.action, {
                method: 'POST',
                body: new FormData(cForm),
                headers: { Accept: 'application/json' }
            });
            if (res.ok) {
                const data = await res.json();
                console.log("FormSubmit response:", data, "status:", res.status);
                if (data && (data.success === "true" || data.success === true)) {
                    // Message sent successfully
                    cfSubmit.className = 'btn btn-primary sent';
                    btnSpan.textContent = 'Message Sent';
                    cForm.reset();

                    // Revert button after 4 seconds
                    setTimeout(() => {
                        cfSubmit.className = 'btn btn-primary';
                        btnSpan.textContent = 'Send Message';
                        cfSubmit.disabled = false;
                    }, 4000);
                } else {
                    // If FormSubmit fails, show error feedback on button
                    cfSubmit.className = 'btn btn-primary error';
                    btnSpan.textContent = 'Error — Try Again';

                    // Revert button after 3 seconds
                    setTimeout(() => {
                        cfSubmit.className = 'btn btn-primary';
                        btnSpan.textContent = 'Send Message';
                        cfSubmit.disabled = false;
                    }, 3000);
                }
            } else {
                throw new Error();
            }
        } catch (err) {
            console.error("Form submit error:", err);
            cfSubmit.className = 'btn btn-primary error';
            btnSpan.textContent = 'Error — Try Again';

            // Revert button after 3 seconds
            setTimeout(() => {
                cfSubmit.className = 'btn btn-primary';
                btnSpan.textContent = 'Send Message';
                cfSubmit.disabled = false;
            }, 3000);
        }
    }

    if (cForm) {
        cForm.addEventListener('submit', e => {
            e.preventDefault();

            if (typeof grecaptcha === 'undefined') {
                submitForm();
                return;
            }

            const btnSpan = cfSubmit.querySelector('span');
            cfSubmit.disabled = true;
            cfSubmit.className = 'btn btn-primary sending';
            btnSpan.textContent = 'Verifying…';

            grecaptcha.ready(() => {
                grecaptcha.execute('6LfAIAItAAAAAFYA4LvKoBfZ0zugAuNPoP9eNXpe', { action: 'submit_contact_form' })
                    .then(token => {
                        document.getElementById('g-recaptcha-response').value = token;
                        submitForm();
                    })
                    .catch(err => {
                        console.error('reCAPTCHA execution error:', err);
                        cfSubmit.className = 'btn btn-primary error';
                        btnSpan.textContent = 'Verification Failed';

                        setTimeout(() => {
                            cfSubmit.className = 'btn btn-primary';
                            btnSpan.textContent = 'Send Message';
                            cfSubmit.disabled = false;
                        }, 3000);
                    });
            });
        });
    }

})();
