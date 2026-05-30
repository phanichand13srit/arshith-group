import os

# Definition of the 4 detailed subpages with their specific content
subpages_data = {
    "internship-software-dev.html": {
        "title": "Software Development",
        "meta_desc": "Detailed guide, curriculum, and application details for the 3-Month Software Development Internship at Arshit Group.",
        "program": "3 Months Program",
        "subtitle": "Gain foundation engineering training, master core web technologies, and build active project codebases.",
        "about_p": "Step into the software industry with a highly structured program. At Arshit Infotech, you won't just study theoretical principles—you will code, compile, and debug real-world applications alongside senior software engineers. You will learn modern development workflows and collaborate using version control.",
        "stipend": "₹2,000 / month",
        "focus_area": "HTML, CSS, JS, Git",
        "pills": ["HTML5", "CSS3 Responsive", "JavaScript ES6", "Git / GitHub"],
        "who_can_apply": [
            "Students pursuing B.E., B.Tech, MCA, BCA, or equivalent software courses.",
            "Enthusiasts with basic programming knowledge in any programming language (C, C++, Java, JS).",
            "Ambitious individuals eager to learn modern software workflows.",
            "Candidates capable of dedicating at least 15-20 hours a week for projects.",
            "No previous workspace experience required; passion is key!"
        ],
        "milestones": [
            {
                "badge": "Weeks 1 - 4",
                "title": "Core Frontend foundations",
                "desc": "Master HTML5 semantics, responsive CSS architectures (Flexbox, Grid), and modern JavaScript mechanics."
            },
            {
                "badge": "Weeks 5 - 8",
                "title": "Version Control & Project builds",
                "desc": "Understand git branches, pull requests, and deploy 2 custom responsive web portfolios."
            },
            {
                "badge": "Weeks 9 - 12",
                "title": "Capstone & Code Reviews",
                "desc": "Build a complex multi-page operational client platform, perform collaborative debugging, and obtain feedback."
            }
        ],
        "hero_img": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=1600&q=80",
        "div_img1": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=1600&q=80",
        "div_img2": "https://images.unsplash.com/photo-1531403009284-440f080d1e12?auto=format&fit=crop&w=1600&q=80",
        "quote1": "The best way to predict the future is to invent it.",
        "quote2": "Continuous learning is the minimum requirement for success in any field.",
        "theme_color1": "#00ddff",
        "theme_color2": "#f59e0b",
        "cta_h2": "Scale Your Skills to Professional Standards",
        "cta_p": "Build high-end software products and lock in your future career now. Space is strictly limited."
    },
    "internship-fullstack-pro.html": {
        "title": "Full-Stack Dev Pro",
        "meta_desc": "Detailed guide, curriculum, and application details for the 6-Month Full-Stack Dev Pro Internship at Arshit Group.",
        "program": "6 Months Pro Program",
        "subtitle": "Deep dive into full-stack software architectures. Build robust client-server platforms and secure a PPO.",
        "about_p": "The Pro Internship is designed for developers who want to cross the boundary into advanced engineering. You will gain comprehensive hands-on exposure to full-stack systems—covering database scaling, server architectures, API security, and state management. Top performers in this program qualify for Pre-Placement Offers (PPOs).",
        "stipend": "₹5,000 / month",
        "focus_area": "React, Node, Express, MongoDB",
        "pills": ["React JS", "Node JS", "Express Framework", "MongoDB / SQL"],
        "who_can_apply": [
            "Pre-final or final year engineering, MCA, or IT students.",
            "Candidates with prior basic knowledge of React, Node, or backend programming.",
            "Developers eager to learn complex full-stack architecture principles.",
            "Must have a personal computer and be capable of working on independent projects.",
            "Individuals looking to secure a full-time Pre-Placement Offer (PPO) post graduation."
        ],
        "milestones": [
            {
                "badge": "Months 1 - 2",
                "title": "Frontend Engineering",
                "desc": "Master advanced React component trees, custom hooks, Redux/Context state managers, and component profiling."
            },
            {
                "badge": "Months 3 - 4",
                "title": "Backend Architectures & databases",
                "desc": "Learn Node.js REST API creation, Express middlewares, JSON Web Token authentication, and MongoDB schema optimization."
            },
            {
                "badge": "Months 5 - 6",
                "title": "Capstone, AWS Deployment & PPO",
                "desc": "Launch a live application on cloud servers (AWS/Vercel/Heroku), secure it, perform load testing, and present to directors."
            }
        ],
        "hero_img": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=1600&q=80",
        "div_img1": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=1600&q=80",
        "div_img2": "https://images.unsplash.com/photo-1531403009284-440f080d1e12?auto=format&fit=crop&w=1600&q=80",
        "quote1": "Simplicity is the soul of efficiency.",
        "quote2": "Make it work, make it right, make it fast.",
        "theme_color1": "#b388ff",
        "theme_color2": "#6366f1",
        "cta_h2": "Scale Your Skills to Professional Standards",
        "cta_p": "Build high-end software products and lock in your future career now. Space is strictly limited."
    },
    "internship-ecommerce-ops.html": {
        "title": "E-Commerce Ops",
        "meta_desc": "Detailed guide, curriculum, and application details for the 3-Month E-Commerce Ops Internship at Arshit Group.",
        "program": "3 Months Program",
        "subtitle": "Learn the fast-paced fundamentals of online retail operations, listings management, and category support.",
        "about_p": "E-Commerce is redefining how global trade works. In this operations internship at Arshith Fresh, you will dive into the core engine of digital supermarkets and online retail. You will gain hands-on expertise in catalogue management, listings optimization, price point configurations, and customer satisfaction audits.",
        "stipend": "₹2,000 / month",
        "focus_area": "Cataloging, Listings, Analytics",
        "pills": ["Cataloging", "Listings Management", "Price Configs", "Analytics Tools"],
        "who_can_apply": [
            "Students pursuing Business Administration (BBA/MBA), Commerce (B.Com), or related studies.",
            "Individuals possessing great verbal and written communication capabilities.",
            "Enthusiasts comfortable working with spreadsheet programs (Excel, Google Sheets).",
            "Candidates having a strong interest in understanding consumers and market metrics.",
            "Highly organized individuals who pay attention to product details."
        ],
        "milestones": [
            {
                "badge": "Weeks 1 - 4",
                "title": "Catalogue & Listings Operations",
                "desc": "Learn product photography standards, listing titles drafting, specifications optimization, and search filters."
            },
            {
                "badge": "Weeks 5 - 8",
                "title": "Pricing & Inventory Control",
                "desc": "Understand safety stock limits, real-time demand variations, discounting triggers, and inventory spreadsheets audits."
            },
            {
                "badge": "Weeks 9 - 12",
                "title": "Customer Satisfaction & Performance reports",
                "desc": "Inspect consumer reviews, identify common delivery gaps, and compile weekly performance metric reports."
            }
        ],
        "hero_img": "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?auto=format&fit=crop&w=1600&q=80",
        "div_img1": "https://images.unsplash.com/photo-1511556532299-8f662fc26c06?auto=format&fit=crop&w=1600&q=80",
        "div_img2": "https://images.unsplash.com/photo-1531403009284-440f080d1e12?auto=format&fit=crop&w=1600&q=80",
        "quote1": "Customer satisfaction is the key to sustainable e-commerce.",
        "quote2": "In retail, every little detail matters to the shopper.",
        "theme_color1": "#1de9b6",
        "theme_color2": "#00c853",
        "cta_h2": "Ready to Launch Your E-Commerce Journey?",
        "cta_p": "Gain actual marketplace experience at Arshith Fresh. Slots are highly demanded."
    },
    "internship-digital-retail-pro.html": {
        "title": "Digital Retail Pro",
        "meta_desc": "Detailed guide, curriculum, and application details for the 6-Month Digital Retail Pro Internship at Arshit Group.",
        "program": "6 Months Pro Program",
        "subtitle": "Master supply chain scaling, category metrics, vendor relationships, and digital retail marketing at Arshith Fresh.",
        "about_p": "Step into a career in supply chain management. In the Digital Retail Pro Internship at Arshith Fresh, you will be given direct ownership of an entire active product category. You will lead vendor onboardings, forecast stock requirements, formulate marketing pipelines, and balance delivery loops to maintain a premium shopping ecosystem.",
        "stipend": "₹5,000 / month",
        "focus_area": "Supply Chain, Category Owner",
        "pills": ["Supply Chain Logs", "Category Owner", "Vendor Relations", "Inventory Planning"],
        "who_can_apply": [
            "Final-year BBA, MBA, Commerce, or Supply Chain Management students.",
            "Enthusiasts with strong analytical skills and advanced data capabilities.",
            "Natural problem solvers capable of negotiating with suppliers and buyers.",
            "Highly organized, detail-oriented individuals comfortable in fast environments.",
            "Candidates looking to secure a full-time Category Lead position post graduation."
        ],
        "milestones": [
            {
                "badge": "Months 1 - 2",
                "title": "Supply Chain & Logistics scaling",
                "desc": "Understand supplier structures, hub layouts, inventory tracking software, and delivery path optimization."
            },
            {
                "badge": "Months 3 - 4",
                "title": "Category Management & Vendor pricing",
                "desc": "Onboard real vendors, negotiate cost options, run seasonal marketing pipelines, and track performance margins."
            },
            {
                "badge": "Months 5 - 6",
                "title": "Capstone Category launch & PPO review",
                "desc": "Design and roll out a brand-new niche product category from scratch, balance customer demand, and present results to directors."
            }
        ],
        "hero_img": "https://images.unsplash.com/photo-1511556532299-8f662fc26c06?auto=format&fit=crop&w=1600&q=80",
        "div_img1": "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?auto=format&fit=crop&w=1600&q=80",
        "div_img2": "https://images.unsplash.com/photo-1531403009284-440f080d1e12?auto=format&fit=crop&w=1600&q=80",
        "quote1": "Operational excellence is the ultimate competitive advantage.",
        "quote2": "A perfectly balanced supply chain is a beautiful thing.",
        "theme_color1": "#ffab00",
        "theme_color2": "#f59e0b",
        "cta_h2": "Lead the Future of Online Retail Category Management",
        "cta_p": "Acquire pro-level supply chain negotiation credentials and secure your post-grad career pathway."
    }
}

template_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} Internship - Arshit Group</title>
    <meta name="description" content="{meta_desc}">
    <link rel="stylesheet" href="styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body class="light-mode">
    <header class="header">
        <div class="header-container">
            <a href="index.html" class="logo">
                <span class="logo-text">Arshit</span><span class="logo-dot">.</span>
            </a>
            
            <nav class="nav-menu">
                <ul class="nav-list">
                    <li class="nav-item"><a href="index.html#about" class="nav-link" data-i18n="nav-about">About Us</a></li>
                    <li class="nav-item dropdown">
                        <a href="index.html#business" class="nav-link"><span data-i18n="nav-business">Businesses</span> <svg class="dropdown-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg></a>
                        <ul class="dropdown-menu">
                            <li><a href="it-services.html" data-i18n="it-nav-link">IT Services & IT Consulting</a></li>
                            <li><a href="ecommerce.html" data-i18n="ec-nav-link">E-Commerce</a></li>
                            <li><a href="#">Multi sellers</a></li>
                            <li><a href="business-consulting.html" data-i18n="bc-nav-link">Business Consulting & Services</a></li>
                            <li><a href="#">Digital Marketing</a></li>
                        </ul>
                    </li>
                    <li class="nav-item dropdown">
                        <a href="index.html#news" class="nav-link"><span data-i18n="nav-news">News</span> <svg class="dropdown-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg></a>
                        <ul class="dropdown-menu">
                            <li><a href="#">Press Releases</a></li>
                            <li><a href="#">Company Updates</a></li>
                            <li><a href="#">Media Kit</a></li>
                        </ul>
                    </li>
                    <li class="nav-item dropdown">
                        <a href="index.html#careers" class="nav-link"><span data-i18n="nav-careers">Careers</span> <svg class="dropdown-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg></a>
                        <ul class="dropdown-menu">
                            <li><a href="#">Open Positions</a></li>
                            <li><a href="#">Life at Arshit</a></li>
                            <li><a href="internships.html">Internships</a></li>
                        </ul>
                    </li>
                    <li class="nav-item dropdown">
                        <a href="#" class="nav-link"><span data-i18n="nav-lang">Languages</span> <svg class="dropdown-arrow" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg></a>
                        <ul class="dropdown-menu">
                            <li><a href="#" class="lang-option" data-lang="en">English</a></li>
                            <li><a href="#" class="lang-option" data-lang="te">తెలుగు (Telugu)</a></li>
                            <li><a href="#" class="lang-option" data-lang="hi">हिंदी (Hindi)</a></li>
                            <li><a href="#" class="lang-option" data-lang="kn">ಕನ್ನಡ (Kannada)</a></li>
                        </ul>
                    </li>
                    <li class="nav-item">
                        <button id="theme-toggle" class="theme-btn" aria-label="Toggle Light/Dark Mode">
                            <svg class="sun-icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
                            <svg class="moon-icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display: none;"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
                        </button>
                    </li>
                </ul>
            </nav>
        </div>
    </header>

    <main>
        <!-- Parallax Hero -->
        <section class="hero-section has-parallax-bg" style="position: relative; min-height: 70vh; display: flex; align-items: center; justify-content: center; text-align: center; padding-top: 100px; overflow: hidden;">
            <div style="position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: url('{hero_img}') no-repeat center center/cover; transform: scale(1.05); z-index: -2; transition: transform 0.5s ease-out;" id="hero-bg-parallax"></div>
            <!-- Elegant responsive theme-adaptive overlay with Option 2 floating streaks -->
            <div class="intern-hero-overlay">
                <div class="hero-floating-elements">
                    <span class="floating-streak" style="left: 10%; animation-delay: 0s; animation-duration: 12s;"></span>
                    <span class="floating-streak silver" style="left: 30%; animation-delay: 2s; animation-duration: 16s;"></span>
                    <span class="floating-streak" style="left: 55%; animation-delay: 4s; animation-duration: 14s;"></span>
                    <span class="floating-streak silver" style="left: 75%; animation-delay: 1s; animation-duration: 18s;"></span>
                    <span class="floating-point" style="left: 20%; animation-delay: 0.5s; animation-duration: 9s;"></span>
                    <span class="floating-point silver" style="left: 45%; animation-delay: 3s; animation-duration: 11s;"></span>
                    <span class="floating-point" style="left: 65%; animation-delay: 1.5s; animation-duration: 8s;"></span>
                    <span class="floating-point silver" style="left: 85%; animation-delay: 5s; animation-duration: 13s;"></span>
                </div>
            </div>
            
            <div class="hero-content hero-animate" style="max-width: 800px; margin: 0 auto; padding: 0 20px; z-index: 1;">
                <span style="font-size: 0.9rem; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; color: {theme_color1}; display: inline-block; margin-bottom: 1rem; background: rgba(0, 221, 255, 0.1); padding: 0.5rem 1.5rem; border-radius: 50px;">{program}</span>
                <h1 class="intern-hero-title" style="font-size: clamp(2.5rem, 5vw, 4rem); margin-bottom: 1.5rem; text-shadow: 0 10px 30px rgba(0,0,0,0.5); font-weight: 700;">{title}</h1>
                <p class="intern-hero-desc hero-subtitle">{subtitle}</p>
                <div style="display: inline-block; margin-top: 1.5rem;">
                    <a href="apply.html" class="btn-buy" style="font-size: 1.1rem; padding: 1rem 2.5rem; border-radius: 50px; box-shadow: 0 10px 25px rgba(0, 221, 255, 0.3);">Apply Now</a>
                </div>
            </div>
        </section>

        <!-- Section 1: About the Internship -->
        <section class="reveal" style="padding: 8rem 5%; background: var(--bg-main); position: relative;">
            <div class="container" style="max-width: 1200px; margin: 0 auto; display: flex; flex-wrap: wrap; gap: 4rem; align-items: center;">
                <!-- Left Text -->
                <div style="flex: 1.2; min-width: 320px;">
                    <h2 style="font-size: 2.5rem; font-family: 'Outfit', sans-serif; font-weight: 800; margin-bottom: 1.5rem; color: var(--intern-text-title); display: flex; align-items: center; gap: 15px;">
                        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="{theme_color1}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"></polygon><polyline points="2 17 12 22 22 17"></polyline><polyline points="2 12 12 17 22 12"></polyline></svg>
                        About The Internship
                    </h2>
                    <p style="color: var(--intern-text-body); font-size: 1.15rem; line-height: 1.8; margin-bottom: 2rem;">
                        {about_p}
                    </p>
                </div>
                
                <!-- Right Glass Highlight Card -->
                <div style="flex: 0.8; min-width: 300px;">
                    <div style="background: var(--intern-card-bg); border: 1px solid rgba(255, 255, 255, 0.08); padding: 3rem; border-radius: 28px; box-shadow: 0 20px 45px rgba(0,0,0,0.03);">
                        <div style="margin-bottom: 2rem; border-bottom: 1px solid rgba(255, 255, 255, 0.08); padding-bottom: 1.5rem;">
                            <span style="font-size: 0.85rem; text-transform: uppercase; color: var(--text-muted); letter-spacing: 1px; font-weight: 600;">Stipend Support</span>
                            <h3 style="font-size: 2.2rem; font-family: 'Outfit', sans-serif; font-weight: 800; color: {theme_color1}; margin-top: 0.5rem;">{stipend}</h3>
                        </div>
                        <div>
                            <span style="font-size: 0.85rem; text-transform: uppercase; color: var(--text-muted); letter-spacing: 1px; font-weight: 600;">Scope / Tech Stacks</span>
                            <div style="display: flex; flex-wrap: wrap; gap: 0.8rem; margin-top: 1rem;">
                                {pills_html}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Parallax Divider 1 -->
        <div class="parallax-window-container">
            <div class="parallax-bg-window" style="background-image: url('{div_img1}');"></div>
            <div class="parallax-window-overlay"></div>
            <div class="parallax-window-content">
                <div class="parallax-glass-badge">
                    <span>"{quote1}"</span>
                </div>
            </div>
        </div>

        <!-- Section 2: Who Can Apply -->
        <section class="reveal" style="padding: 8rem 5%; background: var(--bg-main); position: relative;">
            <div class="container" style="max-width: 1200px; margin: 0 auto;">
                <h2 style="font-size: 2.5rem; font-family: 'Outfit', sans-serif; font-weight: 800; text-align: center; margin-bottom: 4rem; color: var(--intern-text-title); display: flex; align-items: center; justify-content: center; gap: 15px;">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="{theme_color2}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                    Who Can Apply
                </h2>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2.5rem;">
                    {who_can_apply_html}
                </div>
            </div>
        </section>

        <!-- Parallax Divider 2 -->
        <div class="parallax-window-container">
            <div class="parallax-bg-window" style="background-image: url('{div_img2}');"></div>
            <div class="parallax-window-overlay"></div>
            <div class="parallax-window-content">
                <div class="parallax-glass-badge">
                    <span>"{quote2}"</span>
                </div>
            </div>
        </div>

        <!-- Section 3: Curriculum / Syllabus Roadmap -->
        <section class="reveal" style="padding: 8rem 5%; background: var(--bg-main); position: relative;">
            <div class="container" style="max-width: 1200px; margin: 0 auto;">
                <h2 style="font-size: 2.5rem; font-family: 'Outfit', sans-serif; font-weight: 800; text-align: center; margin-bottom: 5rem; color: var(--intern-text-title); display: flex; align-items: center; justify-content: center; gap: 15px;">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#00ff88" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
                    Syllabus & Milestones
                </h2>
                
                <div class="premium-timeline">
                    <div class="timeline-line"></div>
                    {milestones_html}
                </div>
            </div>
        </section>

        <!-- Final Call to Action -->
        <section class="reveal" style="padding: 8rem 5%; background: var(--bg-main); text-align: center;">
            <div class="container" style="max-width: 1000px; margin: 0 auto;">
                <div class="premium-cta-portal">
                    <h2>{cta_h2}</h2>
                    <p>{cta_p}</p>
                    <a href="apply.html" class="cta-glow-btn" style="margin-bottom: 0;">Apply Now</a>
                </div>
            </div>
        </section>
    </main>

    <footer class="kinetic-footer">
        <div class="kf-container">
            <div class="kf-left">
                <div class="kf-content">
                    <h2 class="kf-slogan" data-i18n="footer-slogan">Let there<br>be change</h2>
                    
                    <div class="kf-directory">
                        <div class="kf-menu-col">
                            <h4 data-i18n="footer-ql">Quick Links</h4>
                            <ul>
                                <li><a href="index.html#about" data-i18n="nav-about">About Us</a></li>
                                <li><a href="index.html#business" data-i18n="nav-business">Our Businesses</a></li>
                                <li><a href="index.html#careers" data-i18n="nav-careers">Careers</a></li>
                                <li><a href="index.html#contact" data-i18n="nav-contact">Contact Us</a></li>
                            </ul>
                        </div>
                        <div class="kf-menu-col">
                            <h4 data-i18n="footer-div">Our Divisions</h4>
                            <ul>
                                <li><a href="ecommerce.html">Arshith Fresh</a></li>
                                <li><a href="it-services.html">Arshith Infotech</a></li>
                                <li><a href="business-consulting.html">Suntech Solutions</a></li>
                                <li><a href="#">Global Investments</a></li>
                            </ul>
                        </div>
                        <div class="kf-menu-col">
                            <h4 data-i18n="nav-contact">Contact Us</h4>
                            <ul style="list-style: none; padding: 0; margin: 0; font-size: 0.9rem; line-height: 1.6; color: rgba(255, 255, 255, 0.65);">
                                <li style="margin-bottom: 0.75rem;">
                                    <strong style="color: #ffffff; display: block; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 0.25rem;" data-i18n="contact-ho">Head Office</strong>
                                    <span data-i18n="contact-ho-desc">123 Innovation Drive, Tech Park<br>Hyderabad, TS 500081</span>
                                </li>
                                <li style="margin-bottom: 0.5rem;">
                                    <strong style="color: #ffffff;" data-i18n="contact-ph">Phone</strong>: +91 98765 43210
                                </li>
                                <li>
                                    <strong style="color: #ffffff;" data-i18n="contact-em">Email</strong>: contact@arshitgroup.com
                                </li>
                            </ul>
                        </div>
                    </div>

                    <div class="kf-socials">
                        <a href="#" class="kf-social-link" aria-label="LinkedIn">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
                        </a>
                        <a href="#" class="kf-social-link" aria-label="Twitter">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M23 3a10.9 10.9 0 0 1-3.14 1.53 4.48 4.48 0 0 0-7.86 3v1A10.66 10.66 0 0 1 3 4s-4 9 5 13a11.64 11.64 0 0 1-7 2c9 5 20 0 20-11.5a4.5 4.5 0 0 0-.08-.83A7.72 7.72 0 0 0 23 3z"></path></svg>
                        </a>
                        <a href="#" class="kf-social-link" aria-label="Instagram">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
                        </a>
                        <a href="#" class="kf-social-link" aria-label="Facebook">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg>
                        </a>
                    </div>
                </div>

                <div class="kf-bottom">
                    <p class="kf-copyright" data-i18n="footer-copy">&copy; 2026 Arshit Group of Industries. All rights reserved.</p>
                </div>
            </div>

            <div class="kf-right">
                <div class="kf-column" data-speed="0.15"><div class="kf-text-track">CHANGE CHANGE CHANGE CHANGE CHANGE CHANGE CHANGE</div></div>
                <div class="kf-column" data-speed="-0.2"><div class="kf-text-track">CHANGE CHANGE CHANGE CHANGE CHANGE CHANGE CHANGE</div></div>
                <div class="kf-column" data-speed="0.25"><div class="kf-text-track">CHANGE CHANGE CHANGE CHANGE CHANGE CHANGE CHANGE</div></div>
                <div class="kf-column" data-speed="-0.1"><div class="kf-text-track">CHANGE CHANGE CHANGE CHANGE CHANGE CHANGE CHANGE</div></div>
                <div class="kf-column" data-speed="0.3"><div class="kf-text-track">CHANGE CHANGE CHANGE CHANGE CHANGE CHANGE CHANGE</div></div>
            </div>
        </div>
    </footer>

    <script src="translations.js"></script>
    <script src="theme-selector.js"></script>
    <script>
        // --- Scroll Reveal Animation ---
        const revealElements = document.querySelectorAll('.reveal');
        
        const revealOptions = {
            root: null,
            threshold: 0.15,
            rootMargin: "0px 0px -50px 0px"
        };
        
        const revealObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                    observer.unobserve(entry.target);
                }
            });
        }, revealOptions);
        
        revealElements.forEach(el => revealObserver.observe(el));

        // --- Modern Silky Smooth Scroll-Linked Parallax for Windows ---
        window.addEventListener('scroll', () => {
            const scrolled = window.pageYOffset;
            
            // Hero parallax
            const heroBg = document.getElementById('hero-bg-parallax');
            if (heroBg) {
                heroBg.style.transform = `translateY(${scrolled * 0.4}px) scale(1.05)`;
            }
            
            // Parallax Windows
            const windows = document.querySelectorAll('.parallax-bg-window');
            windows.forEach(win => {
                const parent = win.parentElement;
                const rect = parent.getBoundingClientRect();
                
                // Only run if visible
                if (rect.top < window.innerHeight && rect.bottom > 0) {
                    // Translate the window background relative to its viewport position
                    const offset = (window.innerHeight - rect.top) * 0.15;
                    win.style.transform = `translateY(${offset - 100}px) scale(1.1)`;
                }
            });
        });
    </script>
</body>
</html>
"""

# Let's write each subpage by formatting the template
for filename, data in subpages_data.items():
    # Build pills HTML
    pills_html = ""
    for pill in data["pills"]:
        pills_html += f'<span class="meta-pill highlight-pill" style="border-color: rgba(255,255,255,0.08);">{pill}</span>\\n'

    # Build who can apply cards
    apply_icons = ["🎓", "💻", "🔥", "⏳", "🚀"]
    who_can_apply_html = ""
    for idx, item in enumerate(data["who_can_apply"]):
        icon = apply_icons[idx % len(apply_icons)]
        # Make the title brief
        title_words = item.split()
        card_title = " ".join(title_words[:2]) if len(title_words) >= 2 else "Requirement"
        
        who_can_apply_html += f'''
                    <div class="tilt-card" style="padding: 2.5rem; border-radius: 20px;">
                        <span style="font-size: 1.8rem; margin-bottom: 1rem; display: block;">{icon}</span>
                        <h4 style="font-size: 1.25rem; font-family: 'Outfit', sans-serif; font-weight: 700; color: var(--intern-text-title); margin-bottom: 0.8rem;">{card_title}</h4>
                        <p style="color: var(--intern-text-body); line-height: 1.6; font-size: 0.95rem; margin: 0;">{item}</p>
                    </div>'''

    # Build milestones HTML
    milestones_html = ""
    for idx, milestone in enumerate(data["milestones"]):
        side_class = ""
        badge_style = f'background: rgba(0, 221, 255, 0.1); color: var(--blue-light);'
        glow_point_style = ""
        
        if idx % 2 == 1:
            glow_point_style = 'style="background: var(--yass-queen); box-shadow: 0 0 15px var(--yass-queen);"'
            badge_style = f'background: rgba(255, 29, 88, 0.1); color: var(--yass-queen);'
        elif idx == 2:
            glow_point_style = 'style="background: #00ff88; box-shadow: 0 0 15px #00ff88;"'
            badge_style = f'background: rgba(0, 255, 136, 0.1); color: #00ff88;'
            
        milestones_html += f'''
                    <div class="timeline-node">
                        <div class="timeline-glow-point" {glow_point_style}></div>
                        <div class="timeline-content-card">
                            <div class="timeline-step-badge" style="{badge_style}">{milestone["badge"]}</div>
                            <h3 style="font-size: 1.5rem; font-family: 'Outfit', sans-serif; font-weight: 700; color: var(--intern-text-title); margin-bottom: 0.8rem;">{milestone["title"]}</h3>
                            <p style="color: var(--intern-text-body); line-height: 1.7; font-size: 0.98rem; margin: 0;">
                                {milestone["desc"]}
                            </p>
                        </div>
                    </div>'''

    # Format the main template
    page_content = template_html.format(
        title=data["title"],
        meta_desc=data["meta_desc"],
        program=data["program"],
        subtitle=data["subtitle"],
        about_p=data["about_p"],
        stipend=data["stipend"],
        focus_area=data["focus_area"],
        pills_html=pills_html,
        who_can_apply_html=who_can_apply_html,
        milestones_html=milestones_html,
        hero_img=data["hero_img"],
        div_img1=data["div_img1"],
        div_img2=data["div_img2"],
        quote1=data["quote1"],
        quote2=data["quote2"],
        theme_color1=data["theme_color1"],
        theme_color2=data["theme_color2"],
        cta_h2=data["cta_h2"],
        cta_p=data["cta_p"]
    )
    
    # Write the formatted output
    with open(filename, "w", encoding="utf-8") as f:
        f.write(page_content)
    print(f"Generated: {filename}")
