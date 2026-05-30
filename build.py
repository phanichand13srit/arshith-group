import re

with open('it-services.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ecommerce.html
ec_content = content.replace('<title>IT Services & Consulting - Arshit Group</title>', '<title>E-Commerce Solutions - Arshit Group</title>')
ec_main = """    <main>
        <section class="hero-section" style="min-height: 55vh; display: flex; align-items: center; justify-content: center; text-align: center; padding-top: 100px;">
            <div class="hero-content" style="max-width: 800px; margin: 0 auto; padding: 0 20px;">
                <h1 data-i18n="ec-hero-title" style="font-size: clamp(2.5rem, 5vw, 4rem); margin-bottom: 1.5rem;">Empowering Your<br>Digital Storefront</h1>
                <p data-i18n="ec-hero-desc" style="font-size: 1.1rem; color: var(--text-muted);">End-to-end scalable e-commerce solutions for businesses of all sizes.</p>
            </div>
        </section>

        <section class="services-section reveal" id="services" style="padding: 5rem 5%;">
            <div class="container" style="max-width: 1200px; margin: 0 auto;">
                <h2 class="section-title text-center" data-i18n="ec-services-title">Powerful <span class="highlight">Features</span></h2>
                <div class="services-grid">
                    <div class="service-card">
                        <div class="service-icon blue"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path></svg></div>
                        <h3 data-i18n="ec-srv-mv">Multi-Vendor Marketplaces</h3>
                        <p data-i18n="ec-srv-mv-desc">Build robust platforms that support multiple sellers, diverse inventory, and seamless payouts.</p>
                    </div>
                    <div class="service-card">
                        <div class="service-icon pink"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="1" y="4" width="22" height="16" rx="2" ry="2"></rect><line x1="1" y1="10" x2="23" y2="10"></line></svg></div>
                        <h3 data-i18n="ec-srv-pg">Secure Payment Gateways</h3>
                        <p data-i18n="ec-srv-pg-desc">Integrate safe, reliable, and swift payment processing compatible with global financial networks.</p>
                    </div>
                    <div class="service-card">
                        <div class="service-icon yellow"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg></div>
                        <h3 data-i18n="ec-srv-im">Inventory Management</h3>
                        <p data-i18n="ec-srv-im-desc">Automate your stock tracking, alerts, and supply chain logistics in real-time.</p>
                    </div>
                    <div class="service-card">
                        <div class="service-icon purple"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg></div>
                        <h3 data-i18n="ec-srv-seo">SEO & Analytics</h3>
                        <p data-i18n="ec-srv-seo-desc">Data-driven insights to maximize traffic, boost conversion rates, and understand customer behavior.</p>
                    </div>
                </div>
            </div>
        </section>

        <section class="contact-section reveal" style="padding: 6rem 5%; background: var(--glass-bg); border-top: 1px solid var(--glass-border); border-bottom: 1px solid var(--glass-border);">
            <div class="container" style="max-width: 800px; margin: 0 auto; text-align: center;">
                <h2 style="font-size: 2.2rem; margin-bottom: 1rem; color: inherit;" data-i18n="ec-lead-title">Start Selling Online</h2>
                <p style="color: var(--text-muted); margin-bottom: 2.5rem; font-size: 1.1rem; line-height: 1.6;" data-i18n="ec-lead-desc">Join hundreds of businesses leveraging Arshith Fresh's e-commerce ecosystem to reach millions of customers globally.</p>
                <a href="index.html#contact" class="btn-contact" style="display: inline-block; text-decoration: none;" data-i18n="it-btn-partner">Partner With Us</a>
            </div>
        </section>
    </main>"""
ec_content = re.sub(r'<main>.*?</main>', ec_main, ec_content, flags=re.DOTALL)
with open('ecommerce.html', 'w', encoding='utf-8') as f:
    f.write(ec_content)

# business-consulting.html
bc_content = content.replace('<title>IT Services & Consulting - Arshit Group</title>', '<title>Business Consulting & Services - Arshit Group</title>')
bc_main = """    <main>
        <section class="hero-section" style="min-height: 55vh; display: flex; align-items: center; justify-content: center; text-align: center; padding-top: 100px;">
            <div class="hero-content" style="max-width: 800px; margin: 0 auto; padding: 0 20px;">
                <h1 data-i18n="bc-hero-title" style="font-size: clamp(2.5rem, 5vw, 4rem); margin-bottom: 1.5rem;">Strategic Guidance For<br>Unmatched Growth</h1>
                <p data-i18n="bc-hero-desc" style="font-size: 1.1rem; color: var(--text-muted);">Expert consulting services designed to optimize operations, navigate challenges, and accelerate success.</p>
            </div>
        </section>

        <section class="services-section reveal" id="services" style="padding: 5rem 5%;">
            <div class="container" style="max-width: 1200px; margin: 0 auto;">
                <h2 class="section-title text-center" data-i18n="bc-services-title">Our <span class="highlight">Expertise</span></h2>
                <div class="services-grid">
                    <div class="service-card">
                        <div class="service-icon blue"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg></div>
                        <h3 data-i18n="bc-srv-st">Strategic Planning</h3>
                        <p data-i18n="bc-srv-st-desc">Develop long-term blueprints that align with your corporate vision, adapt to market shifts, and maximize ROI.</p>
                    </div>
                    <div class="service-card">
                        <div class="service-icon pink"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg></div>
                        <h3 data-i18n="bc-srv-hr">Human Resources</h3>
                        <p data-i18n="bc-srv-hr-desc">Optimize workforce management, talent acquisition, and corporate culture to drive employee satisfaction.</p>
                    </div>
                    <div class="service-card">
                        <div class="service-icon yellow"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg></div>
                        <h3 data-i18n="bc-srv-op">Operations Management</h3>
                        <p data-i18n="bc-srv-op-desc">Streamline processes, reduce overhead costs, and implement efficient workflow methodologies.</p>
                    </div>
                    <div class="service-card">
                        <div class="service-icon purple"><svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 12h4l2-9 5 18 3-10h6"></path></svg></div>
                        <h3 data-i18n="bc-srv-fa">Financial Advisory</h3>
                        <p data-i18n="bc-srv-fa-desc">Gain insights through risk assessment, investment strategies, and corporate restructuring.</p>
                    </div>
                </div>
            </div>
        </section>

        <section class="contact-section reveal" style="padding: 6rem 5%; background: var(--glass-bg); border-top: 1px solid var(--glass-border); border-bottom: 1px solid var(--glass-border);">
            <div class="container" style="max-width: 800px; margin: 0 auto; text-align: center;">
                <h2 style="font-size: 2.2rem; margin-bottom: 1rem; color: inherit;" data-i18n="bc-lead-title">Transform Your Business</h2>
                <p style="color: var(--text-muted); margin-bottom: 2.5rem; font-size: 1.1rem; line-height: 1.6;" data-i18n="bc-lead-desc">Partner with Suntech Solutions to unlock your organization's true potential through tailored consulting services.</p>
                <a href="index.html#contact" class="btn-contact" style="display: inline-block; text-decoration: none;" data-i18n="it-btn-partner">Partner With Us</a>
            </div>
        </section>
    </main>"""
bc_content = re.sub(r'<main>.*?</main>', bc_main, bc_content, flags=re.DOTALL)
with open('business-consulting.html', 'w', encoding='utf-8') as f:
    f.write(bc_content)

print("Created ecommerce.html and business-consulting.html")
