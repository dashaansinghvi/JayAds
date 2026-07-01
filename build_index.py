import os

def build_index():
    html = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8" />
    <title>JayAds - B2B White-Label Production & Editing Partner</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="The silent execution engine for agencies. We provide white-label production, editing, and shooting." />
    <meta name="keywords"
        content="white label production, b2b video editing, camera crew, agency partner" />
    <meta content="Uniquecrew" name="author" />
    <link rel="icon" href="favicon.ico">
    <!-- Google Material Icons -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <!-- Google reCAPTCHA v3 -->
    <script src="https://www.google.com/recaptcha/api.js?render=6LfAIAItAAAAAFYA4LvKoBfZ0zugAuNPoP9eNXpe"></script>
    <!-- Open Graph -->
    <meta property="og:title" content="JayAds - B2B White-Label Production & Editing Partner">
    <meta property="og:description" content="The silent execution engine for agencies. We provide white-label production, editing, and shooting.">
    <meta property="og:image" content="original_files/InterMentalist_logo_png-01.webp">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary_large_image">

    <link rel="stylesheet" href="styles.css">
</head>

<body>

    <!-- ====================================================
     NAVIGATION
==================================================== -->
    <nav id="nav" aria-label="Main navigation">
        <div class="wrap nav-wrap">
            <a href="#home" class="nav-logo" aria-label="JayAds Home">
                <img src="" style="display:none;" alt="JayAds" id="nav-logo-img"
                    width="2083" height="792">
            </a>
            <ul class="nav-links">
                <li><a href="#home" id="nl-home">Home</a></li>
                <li><a href="#journey-inner" id="nl-about">About</a></li>
                <li><a href="#portfolio" id="nl-portfolio">Portfolio</a></li>
                <li><a href="#clients" id="nl-clients">Clientele</a></li>
                <li><a href="#contact" id="nl-contact">Contact Us</a></li>
            </ul>

            <button class="ham" id="ham" aria-label="Menu" aria-expanded="false">
                <span></span><span></span><span></span>
            </button>
        </div>
    </nav>

    <!-- MOBILE MENU -->
    <div class="mob-menu" id="mob-menu" aria-hidden="true">
        <a href="#home">Home</a>
        <a href="#journey-inner">About</a>
        <a href="#portfolio">Portfolio</a>
        <a href="#clients">Clientele</a>
        <a href="#contact">Contact Us</a>
    </div>

    <!-- ====================================================
     HERO — Editorial Magazine Cover
==================================================== -->
    <section id="home" aria-label="Hero">
        <div class="hero-texture"></div>
        <div class="hero-blue-accent"></div>

        <!-- Founder image — right side, large -->
        <div class="hero-founder-wrap">
            <img src="https://images.unsplash.com/photo-1601506521937-0121a7fc2a6b?q=80&w=1024&auto=format&fit=crop" style="border-radius: 12px; filter: grayscale(100%);" alt="Shivashish Tarkas — Founder, JayAds"
                id="hero-founder-img" width="1024" height="1024">
        </div>

        <!-- Text — left side, high z-index to overlap image -->
        <div class="hero-content">
            <div class="wrap">
                <div class="hero-inner">
                    <h1 class="hero-headline">
                        The Silent <span class="accent-word">Engine</span><br>
                        Behind The Best<br>
                        Campaigns.
                    </h1>
                    <p class="hero-sub">
                        We are the dedicated, white-label production & editing crew for agencies and high-profile managers. You handle the client, we handle the execution.
                    </p>

                </div>
            </div>
        </div>

        <!-- Scroll indicator -->
        <div class="hero-scroll">
            <div class="hero-scroll-line"></div>
            <span class="hero-scroll-txt">Scroll</span>
        </div>

        <!-- Year watermark -->
        <div class="hero-badge">
            <span class="hero-badge-year">2026</span>
        </div>
    </section>

    <!-- ====================================================
     STATS — Full-width dark dramatic section
==================================================== -->
    <section id="stats" aria-label="Key Statistics">
        <div class="stats-inner">
            <div class="stat-cell fade">
                <div class="stat-n"><span class="counter" data-t="1000">0</span><span class="acc">+</span></div>
                <div class="stat-l">Projects Delivered</div>
            </div>
            <div class="stat-cell fade d1">
                <div class="stat-n"><span class="counter" data-t="100">0</span><span class="acc">+</span></div>
                <div class="stat-l">Agencies Partnered With</div>
            </div>
            <div class="stat-cell fade d2">
                <div class="stat-n"><span class="counter" data-t="10000">0</span><span class="acc">+</span></div>
                <div class="stat-l">Hours of Content</div>
            </div>
            <div class="stat-cell fade d3">
                <div class="stat-n"><span class="counter" data-t="200">0</span><span class="acc">+</span></div>
                <div class="stat-l">White-Labeled</div>
            </div>
        </div>
    </section>

    <!-- ====================================================
     ABOUT
==================================================== -->
    <section id="about" aria-label="About">
        <!-- Journey / About JayAds -->
        <div class="journey" id="journey-inner">
            <div class="wrap">
                <div class="journey-grid">
                    <div class="journey-sticky">
                        <span class="t-label fade">B2B EXECUTION</span>
                        <h2 class="t-lg fade d1" style="margin-top:10px">We Stay Behind The Scenes,<br><span
                                style="color:var(--blue)">You Take The Credit.</span></h2>
                    </div>
                    <div class="journey-body fade">
                        <p>Founded on the premise that executing high-end production is fundamentally different from client management, <strong>JayAds</strong> was built specifically for agencies, PR firms, and talent managers.</p>
                        <p>We know that as an agency, your most valuable asset is your client relationship. Building an in-house shooting and editing team is expensive, volatile, and deeply time-consuming. That is exactly where we step in.</p>
                        <p>We act as your plug-and-play, invisible production department. From on-ground camera crews and lighting to high-end post-production, VFX, and color grading, we execute the entire project seamlessly under your banner.</p>
                        <p>From influencer marketing and digital movie promotions to creator strategy, scripting,
                            production, and campaign analytics, JayAds operates as a <strong>full-scale
                                strategic partner</strong> built specifically for South India.</p>
                        <p>Over the years, we have quietly produced the assets behind some of the most visible influencer campaigns and corporate films, completely white-labeled. That is our power.</p>
                        <p>At its core lies a rare capability: <em>the power to influence the people who influence
                                culture</em>. That is what makes JayAds the preferred partner for brands,
                            studios, and agencies looking to build real impact in South India.</p>
                    </div>
                </div>
            </div>
        </div>

        <div class="wrap" style="padding-top: 100px; padding-bottom: 0;">
            <!-- About the Founder -->
            <div class="about-grid">
                <!-- Left: Image -->
                <div class="about-img-wrap fade">
                    <img src="https://images.unsplash.com/photo-1574717024453-354056aaddfa?q=80&w=985&auto=format&fit=crop" style="border-radius: 12px; filter: grayscale(100%);" alt="Shivashish Tarkas, Founder of JayAds"
                        loading="lazy" width="985" height="1333">
                    <div class="about-badge">
                        <span class="about-badge-n">10+</span>
                        <span class="about-badge-l">Years of Experience<br>and Expertise</span>
                    </div>
                </div>
                <!-- Right: Text -->
                <div class="about-text">
                    <span class="t-label fade">Our Capabilities</span>
                    <h2 class="about-name fade d1">Full-Scale <br> <span style="color:var(--blue)">Production</span></h2>
                    <p class="about-role fade d1">Founder &amp; CEO — JayAds</p>
                    <div class="about-body fade d2">
                        <p><strong>1. On-Ground Shooting</strong><br>We deploy fully equipped camera crews, lighting technicians, and sound engineers to capture high-end footage for your campaigns. Whether it's a studio shoot or a live event, we handle the logistics.</p>
                        <p><strong>2. Post-Production & Editing</strong><br>Raw footage is nothing without rhythm. Our editing bays process terabytes of data to deliver polished, narrative-driven content optimized for both cinema and social platforms.</p>
                        <p><strong>3. VFX & Motion Graphics</strong><br>We elevate standard footage with high-end 2D/3D motion graphics, text tracking, and visual effects to ensure your client's deliverables look exceptionally premium.</p>
                        <p></p>
                        <p></p>
                        <p></p>
                        <p></p>
                    </div>

                </div>
            </div>
        </div>

        <!-- Services -->
        <div class="services">
            <div class="wrap">
                <span class="t-label fade">All Operations Under One Roof</span>
                <h2 class="t-lg fade d1" style="margin-top:10px">What <span style="color:var(--blue)">We Do</span></h2>
            </div>
            <div class="cards-stack-wrap">
                <div class="cards-stack">
                    <!-- Card 1: Research -->
                    <div class="atm-card fade">
                        <div class="card-logo">
                            <span class="material-icons">search</span>
                        </div>
                        <span class="card-vertical-title">Research</span>
                        <div class="card-info">
                            <h4 class="card-title">Market &amp; <br> Audience <br> Research</h4>
                        </div>
                    </div>

                    <!-- Card 2: Strategy -->
                    <div class="atm-card fade d1">
                        <div class="card-logo">
                            <span class="material-icons">insights</span>
                        </div>
                        <span class="card-vertical-title">Strategy</span>
                        <div class="card-info">
                            <h4 class="card-title">Campaign <br> Strategy</h4>
                        </div>
                    </div>

                    <!-- Card 3: Influencer Sourcing -->
                    <div class="atm-card fade d2">
                        <div class="card-logo">
                            <span class="material-icons">person_search</span>
                        </div>
                        <span class="card-vertical-title">Sourcing</span>
                        <div class="card-info">
                            <h4 class="card-title">Influencer <br> Sourcing &amp; <br> Casting</h4>
                        </div>
                    </div>

                    <!-- Card 4: Production -->
                    <div class="atm-card fade d3">
                        <div class="card-logo">
                            <span class="material-icons">videocam</span>
                        </div>
                        <span class="card-vertical-title">Production</span>
                        <div class="card-info">
                            <h4 class="card-title">Pre &amp; Post <br> Production</h4>
                        </div>
                    </div>

                    <!-- Card 5: Execution -->
                    <div class="atm-card fade d4">
                        <div class="card-logo">
                            <span class="material-icons">offline_bolt</span>
                        </div>
                        <span class="card-vertical-title">Execution</span>
                        <div class="card-info">
                            <h4 class="card-title">Seamless <br> Execution</h4>
                        </div>
                    </div>

                    <!-- Card 6: Statistics & Analytics -->
                    <div class="atm-card fade d1">
                        <div class="card-logo">
                            <span class="material-icons">analytics</span>
                        </div>
                        <span class="card-vertical-title">Analytics</span>
                        <div class="card-info">
                            <h4 class="card-title">Statistics &amp; <br> Analytics</h4>
                        </div>
                    </div>

                    <!-- Card 7: UGC & DVC Videos -->
                    <div class="atm-card fade d2">
                        <div class="card-logo">
                            <span class="material-icons">smart_display</span>
                        </div>
                        <span class="card-vertical-title">Videos</span>
                        <div class="card-info">
                            <h4 class="card-title">UGC &amp; DVC <br> Videos</h4>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ====================================================
     CREDENTIALS — Recognised By / Featured In
==================================================== -->
    <section id="credentials" aria-label="Credentials">
        <div class="wrap">
            <span class="t-label fade">Trusted Across The Industry</span>
            <h2 class="t-lg fade d1" style="margin-top:10px">Recognised by media, trusted by brands, <span
                    style="color:var(--blue)">respected across the ecosystem.</span></h2>

            <div class="cred-columns">
                <!-- Recognised By -->
                <div class="cred-column fade d2">
                    <h3 class="cred-col-title">Recognised By</h3>
                    <div class="cred-grid">
                        <div class="cred-logo-item"><img src="images/Logos/recognized/_BusinessOutreachLogo.webp"
                                alt="Business Outreach" loading="lazy"
                                onerror="this.parentElement.style.display='none'"></div>
                        <div class="cred-logo-item"><img src="images/Logos/recognized/Entrepreneur_logo.webp"
                                alt="Entrepreneur" loading="lazy" onerror="this.parentElement.style.display='none'">
                        </div>
                        <div class="cred-logo-item"><img src="images/Logos/recognized/images.webp" alt="Prime Insights"
                                loading="lazy" onerror="this.parentElement.style.display='none'"></div>
                    </div>
                </div>

                <!-- Featured In -->
                <div class="cred-column fade d3">
                    <h3 class="cred-col-title">Featured In</h3>
                    <div class="cred-grid featured">
                        <div class="cred-logo-item"><img src="images/Logos/featured/Social Samosa.webp"
                                alt="Social Samosa" loading="lazy" onerror="this.parentElement.style.display='none'">
                        </div>
                        <div class="cred-logo-item"><img src="images/Logos/featured/afaqs.webp" alt="Afaqs!"
                                loading="lazy" onerror="this.parentElement.style.display='none'"></div>
                        <div class="cred-logo-item"><img src="images/Logos/featured/impact.webp" alt="Impact"
                                loading="lazy" onerror="this.parentElement.style.display='none'"></div>
                        <div class="cred-logo-item"><img src="images/Logos/featured/unnamed.webp" alt="e4m"
                                loading="lazy" onerror="this.parentElement.style.display='none'"></div>
                        <div class="cred-logo-item"><img src="images/Logos/featured/adgully.webp" alt="Adgully"
                                loading="lazy" onerror="this.parentElement.style.display='none'"></div>
                        <div class="cred-logo-item"><img
                                src="images/Logos/featured/218-2186575_thehindu-logo-logo-of-the-hindu-newspaper-hd.webp"
                                alt="The Hindu" loading="lazy" onerror="this.parentElement.style.display='none'"></div>
                        <div class="cred-logo-item"><img
                                src="images/Logos/featured/Branding-in-Asia-Featured-Image.webp" alt="Branding in Asia"
                                loading="lazy" onerror="this.parentElement.style.display='none'">
                        </div>
                        <div class="cred-logo-item"><img src="images/Logos/featured/Businessworld_(logo).webp"
                                alt="BW Businessworld" loading="lazy" onerror="this.parentElement.style.display='none'">
                        </div>
                        <div class="cred-logo-item"><img src="images/Logos/featured/MediaNews4U.webp" alt="MediaNews4U"
                                loading="lazy" onerror="this.parentElement.style.display='none'"></div>
                        <div class="cred-logo-item"><img src="images/Logos/featured/The_Economic_Times_logo.svg.webp"
                                alt="The Economic Times" loading="lazy"
                                onerror="this.parentElement.style.display='none'"></div>
                        <div class="cred-logo-item"><img src="images/Logos/featured/AdTech-Today-Logo.webp"
                                alt="AdTech Today" loading="lazy" onerror="this.parentElement.style.display='none'">
                        </div>
                        <div class="cred-logo-item"><img src="images/Logos/featured/logo-mediabrief.webp"
                                alt="MediaBrief" loading="lazy" onerror="this.parentElement.style.display='none'"></div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- ====================================================
     PORTFOLIO — Instagram Reels Grid
==================================================== -->
    <section id="portfolio" aria-label="Portfolio">
        <div class="wrap">
            <div class="port-header">
                <div>
                    <span class="t-label fade">The work speaks louder than promises.</span>
                    <h2 class="t-lg fade d1" style="margin-top:10px">The Portfolio Starts Here.<br><span
                            style="color:var(--blue)">Instagram Finishes the Story.</span></h2>
                </div>
            </div>



            <!-- Instagram Reels 3-col portrait grid -->
            <div class="ig-grid" id="ig-grid">

                <!-- Reel 1 -->
                <div class="ig-item" data-index="0" tabindex="0" role="button" aria-label="Play reel 1">
                    <video
                        src="reels/A campaign that was emotionally driven for the select few from the Chennai city. Couldnt have m.mp4"
                        poster="reels/cover/A_campaign_that_was_emotionally_driven_for_the_select_few_from_the_Chennai_city_Couldnt_have_made_it_any_better_India_southindia_reelsinstagram_reelsv_Cy_R-vOSHzd.webp"
                        muted playsinline preload="none" loop></video>
                    <div class="reel-overlay"></div>
                    <div class="reel-badge"><svg viewBox="0 0 24 24">
                            <path
                                d="M15 10l4.553-2.277A1 1 0 0 1 21 8.56v6.88a1 1 0 0 1-1.447.894L15 14M3 8a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8z" />
                        </svg></div>
                    <div class="reel-play-icon"><svg viewBox="0 0 24 24">
                            <polygon points="5 3 19 12 5 21 5 3" />
                        </svg></div>
                    <div class="reel-caption">A campaign emotionally driven for Chennai city.</div>
                </div>

                <!-- Reel 2 -->
                <div class="ig-item" data-index="1" tabindex="0" role="button" aria-label="Play reel 2">
                    <video
                        src="reels/All good things happen in behind the scenes. The hardwork,The effort,The perseveranceAnd what no.mp4"
                        poster="reels/cover/All_good_things_happen_in_behind_the_scenes_The_hardwork_The_effort_The_perseverance_And_what_not_Yet_another_bts_on_our_recent_campaign_with_Bhavana_CcPB08ZprL-.webp"
                        muted playsinline preload="none" loop></video>
                    <div class="reel-overlay"></div>
                    <div class="reel-badge"><svg viewBox="0 0 24 24">
                            <path
                                d="M15 10l4.553-2.277A1 1 0 0 1 21 8.56v6.88a1 1 0 0 1-1.447.894L15 14M3 8a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8z" />
                        </svg></div>
                    <div class="reel-play-icon"><svg viewBox="0 0 24 24">
                            <polygon points="5 3 19 12 5 21 5 3" />
                        </svg></div>
                    <div class="reel-caption">All good things happen behind the scenes.</div>
                </div>

                <!-- Reel 3 -->
                <div class="ig-item" data-index="2" tabindex="0" role="button" aria-label="Play reel 3">
                    <video
                        src="reels/Campaign for Kotak Mahindra Bank Ltd Ft. @keerthysureshofficial Another collaboration with @kota.mp4"
                        poster="reels/cover/Campaign_for_Kotak_Mahindra_Bank_Ltd_Ft_keerthysureshofficial_Another_collaboration_with_kotakbankltd_this_time_a_much_bigger_step_Getting_to_work_wit_Cbjk28sDyzH.webp"
                        muted playsinline preload="none" loop></video>
                    <div class="reel-overlay"></div>
                    <div class="reel-badge"><svg viewBox="0 0 24 24">
                            <path
                                d="M15 10l4.553-2.277A1 1 0 0 1 21 8.56v6.88a1 1 0 0 1-1.447.894L15 14M3 8a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8z" />
                        </svg></div>
                    <div class="reel-play-icon"><svg viewBox="0 0 24 24">
                            <polygon points="5 3 19 12 5 21 5 3" />
                        </svg></div>
                    <div class="reel-caption">Campaign for Kotak Mahindra Bank ft. Keerthy Suresh.</div>
                </div>

                <!-- Reel 4 -->
                <div class="ig-item" data-index="3" tabindex="0" role="button" aria-label="Play reel 4">
                    <video
                        src="reels/Every stunning moment with the Samsung Galaxy Z Flip 6 reflects our relentless dedication and ha.mp4"
                        poster="reels/cover/Every_stunning_moment_with_the_Samsung_Galaxy_Z_Flip_6_reflects_our_relentless_dedication_and_hard_work_From_brainstorming_to_perfecting_every_shot_ou_C-cIM3cSSsS.webp"
                        muted playsinline preload="none" loop></video>
                    <div class="reel-overlay"></div>
                    <div class="reel-badge"><svg viewBox="0 0 24 24">
                            <path
                                d="M15 10l4.553-2.277A1 1 0 0 1 21 8.56v6.88a1 1 0 0 1-1.447.894L15 14M3 8a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8z" />
                        </svg></div>
                    <div class="reel-play-icon"><svg viewBox="0 0 24 24">
                            <polygon points="5 3 19 12 5 21 5 3" />
                        </svg></div>
                    <div class="reel-caption">Samsung Galaxy Z Flip 6 — stunning campaign moments.</div>
                </div>

                <!-- Reel 5 -->
                <div class="ig-item" data-index="4" tabindex="0" role="button" aria-label="Play reel 5">
                    <video
                        src="reels/From Karnataka to AP-Telangana to Tamil Nadu to Kerala , our influencer reach covers all corners.mp4"
                        poster="reels/cover/From_Karnataka_to_APTelangana_to_Tamil_Nadu_to_Kerala_our_influencer_reach_covers_all_corners_of_South_India_ensuring_targeted_campaigns_and_top-tier_DJDyX9ASMY0.webp"
                        muted playsinline preload="none" loop></video>
                    <div class="reel-overlay"></div>
                    <div class="reel-badge"><svg viewBox="0 0 24 24">
                            <path
                                d="M15 10l4.553-2.277A1 1 0 0 1 21 8.56v6.88a1 1 0 0 1-1.447.894L15 14M3 8a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8z" />
                        </svg></div>
                    <div class="reel-play-icon"><svg viewBox="0 0 24 24">
                            <polygon points="5 3 19 12 5 21 5 3" />
                        </svg></div>
                    <div class="reel-caption">Karnataka • Telangana • Tamil Nadu • Kerala — our reach is pan-South.
                    </div>
                </div>

                <!-- Reel 6 -->
                <div class="ig-item" data-index="5" tabindex="0" role="button" aria-label="Play reel 6">
                    <video
                        src="reels/Its surreal for anyone to collaborate with the very person they look up! The Intermentalist tea.mp4"
                        poster="reels/cover/Its_surreal_for_anyone_to_collaborate_with_the_very_person_they_look_up_The_Intermentalist_team_got_a_chance_to_live_the_dream_while_shooting_the_deli_CjcNnvHD6XU.webp"
                        muted playsinline preload="none" loop></video>
                    <div class="reel-overlay"></div>
                    <div class="reel-badge"><svg viewBox="0 0 24 24">
                            <path
                                d="M15 10l4.553-2.277A1 1 0 0 1 21 8.56v6.88a1 1 0 0 1-1.447.894L15 14M3 8a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8z" />
                        </svg></div>
                    <div class="reel-play-icon"><svg viewBox="0 0 24 24">
                            <polygon points="5 3 19 12 5 21 5 3" />
                        </svg></div>
                    <div class="reel-caption">It's surreal to collaborate with the very person you look up to.</div>
                </div>

                <!-- Reel 7 -->
                <div class="ig-item" data-index="6" tabindex="0" role="button" aria-label="Play reel 7">
                    <video
                        src="reels/One brick at a time has led us here. 2023 has kickstarted on a high note as we collaborate with.mp4"
                        poster="reels/cover/One_brick_at_a_time_has_led_us_here_2023_has_kickstarted_on_a_high_note_as_we_collaborate_with_badminton_legend_-_the_one_and_only_Saina_Nehwal_for_So_Cnl0Tj_oOOY.webp"
                        muted playsinline preload="none" loop></video>
                    <div class="reel-overlay"></div>
                    <div class="reel-badge"><svg viewBox="0 0 24 24">
                            <path
                                d="M15 10l4.553-2.277A1 1 0 0 1 21 8.56v6.88a1 1 0 0 1-1.447.894L15 14M3 8a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8z" />
                        </svg></div>
                    <div class="reel-play-icon"><svg viewBox="0 0 24 24">
                            <polygon points="5 3 19 12 5 21 5 3" />
                        </svg></div>
                    <div class="reel-caption">One brick at a time. 2023 kicks off with a major collab.</div>
                </div>

                <!-- Reel 8 -->
                <div class="ig-item" data-index="7" tabindex="0" role="button" aria-label="Play reel 8">
                    <video
                        src="reels/One of the most iconic campaigns of ours in recent times. For Acharya - Prime video, We collabor.mp4"
                        poster="reels/cover/One_of_the_most_iconic_campaigns_of_ours_in_recent_times_For_Acharya_Prime_video_We_collaborated_with_Actress_Aishwarya_Rajesh_and_results_were_way_be_CfDobbpj57_.webp"
                        muted playsinline preload="none" loop></video>
                    <div class="reel-overlay"></div>
                    <div class="reel-badge"><svg viewBox="0 0 24 24">
                            <path
                                d="M15 10l4.553-2.277A1 1 0 0 1 21 8.56v6.88a1 1 0 0 1-1.447.894L15 14M3 8a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8z" />
                        </svg></div>
                    <div class="reel-play-icon"><svg viewBox="0 0 24 24">
                            <polygon points="5 3 19 12 5 21 5 3" />
                        </svg></div>
                    <div class="reel-caption">Acharya × Prime Video — one of our most iconic campaigns.</div>
                </div>

                <!-- Reel 9 -->
                <div class="ig-item" data-index="8" tabindex="0" role="button" aria-label="Play reel 9">
                    <video
                        src="reels/Priya Anand, what a journey it’s been! 😬 After five years, we finally made it happen. Loved eve.mp4"
                        poster="reels/cover/Priya_Anand_what_a_journey_its_been_After_five_years_we_finally_made_it_happen_Loved_every_moment_of_our_shoot_and_cant_wait_for_more_adventures_toget_C9ZFC0nSXTT.webp"
                        muted playsinline preload="none" loop></video>
                    <div class="reel-overlay"></div>
                    <div class="reel-badge"><svg viewBox="0 0 24 24">
                            <path
                                d="M15 10l4.553-2.277A1 1 0 0 1 21 8.56v6.88a1 1 0 0 1-1.447.894L15 14M3 8a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8z" />
                        </svg></div>
                    <div class="reel-play-icon"><svg viewBox="0 0 24 24">
                            <polygon points="5 3 19 12 5 21 5 3" />
                        </svg></div>
                    <div class="reel-caption">Priya Anand — five years in the making, finally here.</div>
                </div>

                <!-- Reel 10 -->
                <div class="ig-item" data-index="9" tabindex="0" role="button" aria-label="Play reel 10">
                    <video
                        src="reels/Quality of work is our preferred business plan. We aint busy but productive always 🔥Our recent.mp4"
                        poster="reels/cover/Quality_of_work_is_our_preferred_business_plan_We_aint_busy_but_productive_always_Our_recent_association_with_Nabha_Natesh_TheInterMentalist_Influence_C7okdvYyaD0.webp"
                        muted playsinline preload="none" loop></video>
                    <div class="reel-overlay"></div>
                    <div class="reel-badge"><svg viewBox="0 0 24 24">
                            <path
                                d="M15 10l4.553-2.277A1 1 0 0 1 21 8.56v6.88a1 1 0 0 1-1.447.894L15 14M3 8a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8z" />
                        </svg></div>
                    <div class="reel-play-icon"><svg viewBox="0 0 24 24">
                            <polygon points="5 3 19 12 5 21 5 3" />
                        </svg></div>
                    <div class="reel-caption">Quality is our business plan — not busy, but productive. 🔥</div>
                </div>

                <!-- Reel 11 -->
                <div class="ig-item" data-index="10" tabindex="0" role="button" aria-label="Play reel 11">
                    <video
                        src="reels/Thats a wrap up !All Out x JayAds 🤘Have you checked out other campaign videos of o.mp4"
                        poster="reels/cover/Thats_a_wrap_up_All_Out_x_The_InterMentalist_Have_you_checked_out_other_campaign_videos_of_ours_for_the_same_brand_If_not_do_have_a_look_at_our_highli_C7ioayhSx_q.webp"
                        muted playsinline preload="none" loop></video>
                    <div class="reel-overlay"></div>
                    <div class="reel-badge"><svg viewBox="0 0 24 24">
                            <path
                                d="M15 10l4.553-2.277A1 1 0 0 1 21 8.56v6.88a1 1 0 0 1-1.447.894L15 14M3 8a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8z" />
                        </svg></div>
                    <div class="reel-play-icon"><svg viewBox="0 0 24 24">
                            <polygon points="5 3 19 12 5 21 5 3" />
                        </svg></div>
                    <div class="reel-caption">That's a wrap! All Out × JayAds 🤘</div>
                </div>

                <!-- Reel 12 -->
                <div class="ig-item" data-index="11" tabindex="0" role="button" aria-label="Play reel 12">
                    <video
                        src="reels/Thrilled to team up with Subramanian Badrinath for our latest project! Collaborating with a vete.mp4"
                        poster="reels/cover/Thrilled_to_team_up_with_Subramanian_Badrinath_for_our_latest_project_Collaborating_with_a_veteran_cricketer_and_commentator_is_always_an_inspiring_ex_C9kEzu7yFs3.webp"
                        muted playsinline preload="none" loop></video>
                    <div class="reel-overlay"></div>
                    <div class="reel-badge"><svg viewBox="0 0 24 24">
                            <path
                                d="M15 10l4.553-2.277A1 1 0 0 1 21 8.56v6.88a1 1 0 0 1-1.447.894L15 14M3 8a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8z" />
                        </svg></div>
                    <div class="reel-play-icon"><svg viewBox="0 0 24 24">
                            <polygon points="5 3 19 12 5 21 5 3" />
                        </svg></div>
                    <div class="reel-caption">Thrilled to team up with Subramanian Badrinath!</div>
                </div>

                <!-- Reel 13 -->
                <div class="ig-item" data-index="12" tabindex="0" role="button" aria-label="Play reel 13">
                    <video
                        src="reels/We had an amazing time shooting for Reliance TRENDS with Andrea Jeremiah! 🌟🎥 The campaign requ.mp4"
                        poster="reels/cover/We_had_an_amazing_time_shooting_for_Reliance_TRENDS_with_Andrea_Jeremiah_The_campaign_required_a_lot_of_planning_and_visualizing_every_shot_before_the_DDCU_gVSQRt.webp"
                        muted playsinline preload="none" loop></video>
                    <div class="reel-overlay"></div>
                    <div class="reel-badge"><svg viewBox="0 0 24 24">
                            <path
                                d="M15 10l4.553-2.277A1 1 0 0 1 21 8.56v6.88a1 1 0 0 1-1.447.894L15 14M3 8a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8z" />
                        </svg></div>
                    <div class="reel-play-icon"><svg viewBox="0 0 24 24">
                            <polygon points="5 3 19 12 5 21 5 3" />
                        </svg></div>
                    <div class="reel-caption">Reliance TRENDS × Andrea Jeremiah — an amazing shoot! 🌟</div>
                </div>

                <!-- Reel 14 -->
                <div class="ig-item" data-index="13" tabindex="0" role="button" aria-label="Play reel 14">
                    <video
                        src="reels/We turn bold ideas into unstoppable campaigns. ⚡Every powerful collaboration starts with the rig.mp4"
                        poster="reels/cover/We_turn_bold_ideas_into_unstoppable_campaigns_Every_powerful_collaboration_starts_with_the_right_connection_and_we_made_it_real_bringing_together_bran_DPfxDiUkgBc.webp"
                        muted playsinline preload="none" loop></video>
                    <div class="reel-overlay"></div>
                    <div class="reel-badge"><svg viewBox="0 0 24 24">
                            <path
                                d="M15 10l4.553-2.277A1 1 0 0 1 21 8.56v6.88a1 1 0 0 1-1.447.894L15 14M3 8a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8z" />
                        </svg></div>
                    <div class="reel-play-icon"><svg viewBox="0 0 24 24">
                            <polygon points="5 3 19 12 5 21 5 3" />
                        </svg></div>
                    <div class="reel-caption">We turn bold ideas into unstoppable campaigns. ⚡</div>
                </div>

                <!-- Reel 15 -->
                <div class="ig-item" data-index="14" tabindex="0" role="button" aria-label="Play reel 15">
                    <video
                        src="reels/What an experience we had working with Suma Kanakala for  Apollos influencer campaign. Our team.mp4"
                        poster="reels/cover/What_an_experience_we_had_working_with_Suma_Kanakala_for_Apollos_influencer_campaign_Our_team_reached_Hyderabad_early_in_the_morning_after_completing_Cr8HkdKtp1r.webp"
                        muted playsinline preload="none" loop></video>
                    <div class="reel-overlay"></div>
                    <div class="reel-badge"><svg viewBox="0 0 24 24">
                            <path
                                d="M15 10l4.553-2.277A1 1 0 0 1 21 8.56v6.88a1 1 0 0 1-1.447.894L15 14M3 8a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8z" />
                        </svg></div>
                    <div class="reel-play-icon"><svg viewBox="0 0 24 24">
                            <polygon points="5 3 19 12 5 21 5 3" />
                        </svg></div>
                    <div class="reel-caption">Suma Kanakala for Apollo's influencer campaign — what an experience!</div>
                </div>

                <!-- Reel 16 -->
                <div class="ig-item" data-index="15" tabindex="0" role="button" aria-label="Play reel 16">
                    <video
                        src="reels/When you think of uber cool outfits, you think of AJIO. When AJIO thinks of driving their digita.mp4"
                        poster="reels/cover/When_you_think_of_uber_cool_outfits_you_think_of_AJIO_When_AJIO_thinks_of_driving_their_digital_campaign_for_South_they_think_of_US_first_We_are_alway_CqAqjY_jmtt.webp"
                        muted playsinline preload="none" loop></video>
                    <div class="reel-overlay"></div>
                    <div class="reel-badge"><svg viewBox="0 0 24 24">
                            <path
                                d="M15 10l4.553-2.277A1 1 0 0 1 21 8.56v6.88a1 1 0 0 1-1.447.894L15 14M3 8a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8z" />
                        </svg></div>
                    <div class="reel-play-icon"><svg viewBox="0 0 24 24">
                            <polygon points="5 3 19 12 5 21 5 3" />
                        </svg></div>
                    <div class="reel-caption">AJIO × JayAds — uber cool campaigns.</div>
                </div>

                <!-- Reel 17 -->
                <div class="ig-item" data-index="16" tabindex="0" role="button" aria-label="Play reel 17">
                    <video
                        src="reels/Where the good road ends, off-roading begins.Here is our campaign for MG Motors for their vehicl.mp4"
                        poster="reels/cover/Where_the_good_road_ends_off-roading_begins_Here_is_our_campaign_for_MG_Motors_for_their_vehicle_-_GLOSTER_Watch_outthe_road_is_gonna_get_tough_India_Cs5fb4isJdG.webp"
                        muted playsinline preload="none" loop></video>
                    <div class="reel-overlay"></div>
                    <div class="reel-badge"><svg viewBox="0 0 24 24">
                            <path
                                d="M15 10l4.553-2.277A1 1 0 0 1 21 8.56v6.88a1 1 0 0 1-1.447.894L15 14M3 8a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8z" />
                        </svg></div>
                    <div class="reel-play-icon"><svg viewBox="0 0 24 24">
                            <polygon points="5 3 19 12 5 21 5 3" />
                        </svg></div>
                    <div class="reel-caption">Where the good road ends, off-roading begins. MG Motors campaign.</div>
                </div>

                <!-- Instagram Promo Card (18th Slot) -->
                <div class="ig-promo-card">
                    <div class="ig-promo-content">
                        <svg class="ig-promo-logo" viewBox="0 0 24 24">
                            <rect x="2" y="2" width="20" height="20" rx="5" ry="5" />
                            <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z" />
                            <line x1="17.5" y1="6.5" x2="17.51" y2="6.5" />
                        </svg>
                        <p class="ig-promo-tag">You have seen the proof, now see the volume</p>
                        <a href="https://www.instagram.com/intermentalist/" target="_blank"
                            class="btn btn-primary btn-ig-custom">
                            <span>Visit Instagram</span>
                        </a>
                    </div>
                </div>

            </div><!-- /.ig-grid -->

            <!-- Actions: PDF Download -->
            <div class="port-actions">
                <a href="updated-content/The_InterMentalist_Portfolio.pdf" target="_blank" class="btn btn-primary"
                    id="pdf-download-btn" download>
                    <span>Download our Portfolio</span>
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"
                        stroke-linecap="round" stroke-linejoin="round">
                        <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
                        <polyline points="7 10 12 15 17 10" />
                        <line x1="12" y1="15" x2="12" y2="3" />
                    </svg>
                </a>
                <p class="port-note">A closer look at our journey, our systems, and the elite brands and personalities
                    we've worked with.</p>
            </div>
        </div>
    </section>

    <!-- ====================================================
     REELS LIGHTBOX MODAL
==================================================== -->
    <div id="reels-modal" role="dialog" aria-modal="true" aria-label="Reel viewer">
        <div class="reels-modal-wrapper">
            <div class="reels-modal-inner">
                <!-- Top bar -->
                <div class="reels-modal-bar">
                    <div class="reels-modal-user">
                        <div class="reels-modal-avatar">
                            <img src="" style="display:none;" alt="intermentalist" width="2083"
                                height="792">
                        </div>
                        <span class="reels-modal-name">intermentalist</span>
                    </div>
                    <button class="reels-modal-close" id="reels-modal-close" aria-label="Close">
                        <svg viewBox="0 0 24 24">
                            <line x1="18" y1="6" x2="6" y2="18" />
                            <line x1="6" y1="6" x2="18" y2="18" />
                        </svg>
                    </button>
                </div>
                <!-- Video -->
                <video id="reels-modal-video" controls playsinline></video>
                <!-- Caption -->
                <div class="reels-modal-caption" id="reels-modal-caption"></div>
            </div>
            <!-- Prev / Next -->
            <button class="reels-nav-btn" id="reels-prev" aria-label="Previous reel">
                <svg viewBox="0 0 24 24">
                    <polyline points="15 18 9 12 15 6" />
                </svg>
            </button>
            <button class="reels-nav-btn" id="reels-next" aria-label="Next reel">
                <svg viewBox="0 0 24 24">
                    <polyline points="9 18 15 12 9 6" />
                </svg>
            </button>
        </div>
    </div>

    <!-- ====================================================
     CLIENTS / CLIENTELE
==================================================== -->
    <section id="clients" aria-label="Our Clients">
        <div class="wrap clients-head">
            <span class="t-label fade" style="margin-bottom: 8px;">Creator &amp; Brand Network</span>
            <h2 class="t-lg fade d1">Happy <span style="color:var(--blue)">Clients</span></h2>
            <p class="clients-tagline fade d2">
                Chances are, your favourite brand has already trusted us with its influencer marketing.
            </p>
        </div>
        <!-- Infinite Slider / Ticker -->
        <div class="clients-slider-container fade d2">
            <!-- Row 1: Scrolls Left -->
            <div class="logo-marquee-row marquee-left">
                <div class="logo-marquee-track" id="marquee-track-1">
                    <!-- Logos will be dynamically loaded here -->
                </div>
            </div>

            <!-- Row 2: Scrolls Right -->
            <div class="logo-marquee-row marquee-right">
                <div class="logo-marquee-track" id="marquee-track-2">
                    <!-- Logos will be dynamically loaded here -->
                </div>
            </div>

            <!-- Row 3: Scrolls Left -->
            <div class="logo-marquee-row marquee-left">
                <div class="logo-marquee-track" id="marquee-track-3">
                    <!-- Logos will be dynamically loaded here -->
                </div>
            </div>
        </div>
    </section>


    <!-- ====================================================
     CONTACT
==================================================== -->
    <section id="contact" aria-label="Contact Us">
        <div class="wrap">
            <div style="margin-bottom:48px; text-align: center;">
                <span class="t-label fade">Get In Touch</span>
                <h2 class="t-lg fade d1" style="margin-top:10px">Let's Work <span
                        style="color:var(--blue)">Together</span></h2>
                <p class="t-body fade d2" style="max-width:540px; margin: 14px auto 0;">Ready to win South India? Let’s
                    build influence that actually moves culture</p>
            </div>

            <!-- Designed like a single card -->
            <div class="contact-card-wrap fade d2">
                <form class="c-form-wrap" id="c-form"
                    action="https://formsubmit.co/ajax/shivtarkas@theintermentalist.com" method="POST">
                    <!-- FormSubmit Configuration -->
                    <input type="hidden" name="_captcha" value="false">
                    <input type="hidden" name="_template" value="plain">
                    <input type="hidden" name="_subject" value="New Inquiry from JayAds Website">
                    <div class="c-form-grid">
                        <!-- Left column: 3 stacked inputs -->
                        <div class="c-form-left">
                            <div class="f-group">
                                <label class="f-label" for="cf-name">First Name</label>
                                <input class="f-input" type="text" id="cf-name" name="Name" placeholder="e.g. Rahul"
                                    required>
                            </div>
                            <div class="f-group">
                                <label class="f-label" for="cf-email">Your Email</label>
                                <input class="f-input" type="email" id="cf-email" name="email"
                                    placeholder="you@company.com" required>
                            </div>
                            <div class="f-group">
                                <label class="f-label" for="cf-subject">Your Subject</label>
                                <input class="f-input" type="text" id="cf-subject" name="Subject"
                                    placeholder="e.g. Campaign Inquiry">
                            </div>
                        </div>
                        <!-- Right column: Large textarea -->
                        <div class="c-form-right">
                            <div class="f-group" style="flex:1">
                                <label class="f-label" for="cf-msg">Your Message</label>
                                <textarea class="f-ta" id="cf-msg" name="Message"
                                    placeholder="Tell us about your campaign goals, budget, timeline and target market..."
                                    required></textarea>
                            </div>
                        </div>
                    </div>
                    <!-- Hidden input to store Google reCAPTCHA v3 token (renamed with _ prefix to hide from email body) -->
                    <input type="hidden" name="_recaptcha-response" id="g-recaptcha-response">
                    <!-- Centered send button -->
                    <div class="c-form-submit">
                        <button type="submit" class="btn btn-primary" id="cf-submit">
                            <span>Send Message</span>
                            <svg class="btn-arrow" viewBox="0 0 24 24">
                                <line x1="5" y1="12" x2="19" y2="12" />
                                <polyline points="12 5 19 12 12 19" />
                            </svg>
                            <svg class="btn-tick" viewBox="0 0 24 24">
                                <polyline points="20 6 9 17 4 12" />
                            </svg>
                        </button>
                    </div>
                    <p class="recaptcha-notice">This site is protected by reCAPTCHA and the Google <a
                            href="https://policies.google.com/privacy" target="_blank" rel="noopener">Privacy Policy</a>
                        and <a href="https://policies.google.com/terms" target="_blank" rel="noopener">Terms of
                            Service</a> apply.</p>
                </form>
            </div>
        </div>
    </section>

    <!-- ====================================================
     PREMIUM THICKER FOOTER
==================================================== -->
    <footer>
        <div class="wrap foot-wrap">
            <div class="foot-sep">
                <span class="foot-sep-blue"></span>
                <span class="foot-sep-gap"></span>
                <span class="foot-sep-red"></span>
            </div>
            <!-- Top Row: Logo/Mission left, 3-column inquiries right -->
            <div class="foot-main">
                <!-- Brand & Mission Column -->
                <div class="foot-brand">
                    <div class="foot-logo-wrap">
                        <img src="" style="display:none;" alt="JayAds"
                            class="foot-logo-img" width="2083" height="792">
                    </div>
                    <p class="foot-mission">
                        We are the dedicated, white-label production & editing crew for agencies and high-profile managers. You handle the client, we handle the execution.
                    </p>
                </div>

                <!-- Contact Info & Map Columns -->
                <div class="foot-info-grid">
                    <!-- Location Column (includes Map) -->
                    <div class="foot-info-col">
                        <h3 class="foot-info-title">Location</h3>
                        <div class="foot-detail-item">
                            <div class="foot-detail-icon" aria-hidden="true">
                                <svg viewBox="0 0 24 24">
                                    <path d="M21 10c0 7-9 13-9 13S3 17 3 10a9 9 0 0 1 18 0z" />
                                    <circle cx="12" cy="10" r="3" />
                                </svg>
                            </div>
                            <p class="foot-info-val">
                                No 10, Uttamar Gandhi Salai,<br>
                                Nungambakkam High Rd, Chennai, Tamil Nadu 600034.
                            </p>
                        </div>
                        <!-- Google Map placed near the address -->
                        <div class="foot-map-wrap" style="margin-top: 16px;">
                            <iframe
                                src="https://maps.google.com/maps?q=No%2010,%20Uttamar%20Gandhi%20Salai,%20Nungambakkam%20High%20Rd,%20Chennai,%20Tamil%20Nadu%20600034&t=&z=15&ie=UTF8&iwloc=&output=embed"
                                allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
                                title="Footer location map">
                            </iframe>
                        </div>
                    </div>

                    <!-- Inquiry Column -->
                    <div class="foot-info-col">
                        <h3 class="foot-info-title">Inquiry</h3>

                        <div class="foot-detail-item" style="margin-bottom: 16px;">
                            <div class="foot-detail-icon" aria-hidden="true">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"
                                    stroke-linecap="round" stroke-linejoin="round">
                                    <path
                                        d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" />
                                    <polyline points="22,6 12,13 2,6" />
                                </svg>
                            </div>
                            <p class="foot-info-val">
                                <a href="mailto:shivtarkas@theintermentalist.com"
                                    class="foot-link">shivtarkas@theintermentalist.com</a>
                            </p>
                        </div>

                        <div class="foot-detail-item" style="margin-bottom: 16px;">
                            <div class="foot-detail-icon" aria-hidden="true">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"
                                    stroke-linecap="round" stroke-linejoin="round">
                                    <path
                                        d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.69 9.8 19.79 19.79 0 0 1 1.61 1.17 2 2 0 0 1 3.61 0h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9a16 16 0 0 0 6.29 6.29l1.36-1.36a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z" />
                                </svg>
                            </div>
                            <p class="foot-info-val">
                                <a href="tel:+919500040807" class="foot-link">+91 95000 40807</a>
                            </p>
                        </div>

                        <!-- Instagram -->
                        <div class="foot-detail-item" style="margin-bottom: 16px;">
                            <div class="foot-detail-icon" aria-hidden="true">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                                    stroke-linecap="round" stroke-linejoin="round">
                                    <rect x="2" y="2" width="20" height="20" rx="5" />
                                    <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z" />
                                    <line x1="17.5" y1="6.5" x2="17.51" y2="6.5" />
                                </svg>
                            </div>
                            <p class="foot-info-val">
                                <a href="https://www.instagram.com/intermentalist/" target="_blank"
                                    class="foot-link">@intermentalist</a>
                            </p>
                        </div>

                        <!-- LinkedIn -->
                        <div class="foot-detail-item" style="margin-bottom: 16px;">
                            <div class="foot-detail-icon" aria-hidden="true">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                                    stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7H10V9h4v1.5a4 4 0 0 1 2-1.5z" />
                                    <rect x="2" y="9" width="4" height="12" />
                                    <circle cx="4" cy="4" r="2" />
                                </svg>
                            </div>
                            <p class="foot-info-val">
                                <a href="https://www.linkedin.com/in/shivashishtarkas/" target="_blank"
                                    class="foot-link">Shivashish Tarkas</a>
                            </p>
                        </div>

                        <!-- Facebook -->
                        <div class="foot-detail-item">
                            <div class="foot-detail-icon" aria-hidden="true">
                                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"
                                    stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z" />
                                </svg>
                            </div>
                            <p class="foot-info-val">
                                <a href="https://www.facebook.com/theintermentalist" target="_blank"
                                    class="foot-link">JayAds</a>
                            </p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Bottom Row: Copyright -->
            <div class="foot-bottom">
                <p class="foot-copy">© 2026 JayAds. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <!-- Back to top -->
    <button id="btt" aria-label="Back to top">
        <svg viewBox="0 0 24 24">
            <polyline points="18 15 12 9 6 15" />
        </svg>
    </button>

    <!-- ====================================================
     JAVASCRIPT
==================================================== -->
    <script src="ui_interactions.js" defer></script>
</body>

</html>"""
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

build_index()
