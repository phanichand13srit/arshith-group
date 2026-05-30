import re

# E-commerce HTML
with open('ecommerce.html', 'r', encoding='utf-8') as f:
    ec_content = f.read()

ec_sections = """        <!-- Products Section -->
        <section class="products-section reveal" style="padding: 5rem 5%;">
            <div class="container" style="max-width: 1200px; margin: 0 auto;">
                <h2 class="section-title text-center" data-i18n="ec-prod-title">Featured <span class="highlight">Organics</span></h2>
                <div class="products-grid">
                    <div class="product-card">
                        <img src="https://images.unsplash.com/photo-1587049352847-4d4b1a629b35?auto=format&fit=crop&q=80&w=200" alt="Organic Honey" class="product-img">
                        <h3 class="product-title" data-i18n="ec-prod-1">Pure Wild Honey</h3>
                        <div class="product-rating">★★★★★</div>
                        <div class="product-price">$12.99</div>
                        <button class="btn-buy" data-i18n="ec-buy">Add to Cart</button>
                    </div>
                    <div class="product-card">
                        <img src="https://images.unsplash.com/photo-1519996409144-56c88c9aa612?auto=format&fit=crop&q=80&w=200" alt="Fresh Avocados" class="product-img">
                        <h3 class="product-title" data-i18n="ec-prod-2">Fresh Hass Avocados</h3>
                        <div class="product-rating">★★★★☆</div>
                        <div class="product-price">$8.50</div>
                        <button class="btn-buy" data-i18n="ec-buy">Add to Cart</button>
                    </div>
                    <div class="product-card">
                        <img src="https://images.unsplash.com/photo-1474440692490-2e83ae13ba29?auto=format&fit=crop&q=80&w=200" alt="Cold-pressed Olive Oil" class="product-img">
                        <h3 class="product-title" data-i18n="ec-prod-3">Cold-Pressed Olive Oil</h3>
                        <div class="product-rating">★★★★★</div>
                        <div class="product-price">$24.00</div>
                        <button class="btn-buy" data-i18n="ec-buy">Add to Cart</button>
                    </div>
                </div>
            </div>
        </section>

        <!-- Customer Reviews -->
        <section class="reviews-section reveal" style="padding: 5rem 5%; background: rgba(0,0,0,0.02);">
            <div class="container" style="max-width: 1200px; margin: 0 auto;">
                <h2 class="section-title text-center" data-i18n="ec-rev-title">Happy <span class="highlight">Customers</span></h2>
                <div class="reviews-grid">
                    <div class="review-card">
                        <div class="review-quote">"</div>
                        <p class="review-text" data-i18n="ec-rev-1">"The organic produce from Arshith Fresh is simply unmatched. The delivery is always on time, and the quality is superb!"</p>
                        <div class="reviewer-info">
                            <div class="reviewer-avatar">S</div>
                            <div class="reviewer-details">
                                <h4>Sarah Jenkins</h4>
                                <p data-i18n="ec-rev-buyer">Verified Buyer</p>
                            </div>
                        </div>
                    </div>
                    <div class="review-card">
                        <div class="review-quote">"</div>
                        <p class="review-text" data-i18n="ec-rev-2">"I love the fact that everything is locally sourced. The wild honey is the best I've ever tasted."</p>
                        <div class="reviewer-info">
                            <div class="reviewer-avatar">M</div>
                            <div class="reviewer-details">
                                <h4>Michael T.</h4>
                                <p data-i18n="ec-rev-buyer">Verified Buyer</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""
ec_content = ec_content.replace('</main>', ec_sections + '    </main>')
with open('ecommerce.html', 'w', encoding='utf-8') as f:
    f.write(ec_content)

# IT Services HTML
with open('it-services.html', 'r', encoding='utf-8') as f:
    it_content = f.read()

it_sections = """        <!-- Projects Section -->
        <section class="projects-section reveal" style="padding: 5rem 5%;">
            <div class="container" style="max-width: 1200px; margin: 0 auto;">
                <h2 class="section-title text-center" data-i18n="it-proj-title">Recent <span class="highlight">Projects</span></h2>
                <div class="projects-grid">
                    <div class="project-card">
                        <div class="project-img">
                            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="3" width="20" height="14" rx="2" ry="2"></rect><line x1="8" y1="21" x2="16" y2="21"></line><line x1="12" y1="17" x2="12" y2="21"></line></svg>
                        </div>
                        <div class="project-content">
                            <h3 class="project-title" data-i18n="it-proj-1">Enterprise CRM Dashboard</h3>
                            <p class="project-desc" data-i18n="it-proj-desc-1">A fully scalable, cloud-based CRM solution developed for a top-tier financial institution.</p>
                        </div>
                    </div>
                    <div class="project-card">
                        <div class="project-img">
                            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path></svg>
                        </div>
                        <div class="project-content">
                            <h3 class="project-title" data-i18n="it-proj-2">AI Chatbot Integration</h3>
                            <p class="project-desc" data-i18n="it-proj-desc-2">Implemented a machine learning-driven customer support bot, reducing ticket response times by 80%.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Client Reviews -->
        <section class="reviews-section reveal" style="padding: 5rem 5%; background: rgba(0,0,0,0.02);">
            <div class="container" style="max-width: 1200px; margin: 0 auto;">
                <h2 class="section-title text-center" data-i18n="it-rev-title">Client <span class="highlight">Testimonials</span></h2>
                <div class="reviews-grid">
                    <div class="review-card">
                        <div class="review-quote">"</div>
                        <p class="review-text" data-i18n="it-rev-1">"Arshith Infotech delivered our backend systems flawlessly. Their technical expertise and dedication are truly world-class."</p>
                        <div class="reviewer-info">
                            <div class="reviewer-avatar">D</div>
                            <div class="reviewer-details">
                                <h4>David Chen</h4>
                                <p data-i18n="it-rev-role">CTO, TechWave Corp</p>
                            </div>
                        </div>
                    </div>
                    <div class="review-card">
                        <div class="review-quote">"</div>
                        <p class="review-text" data-i18n="it-rev-2">"The digital marketing strategies they implemented doubled our inbound leads in just three months."</p>
                        <div class="reviewer-info">
                            <div class="reviewer-avatar">A</div>
                            <div class="reviewer-details">
                                <h4>Amanda L.</h4>
                                <p data-i18n="it-rev-role2">Marketing Director</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""
it_content = it_content.replace('</main>', it_sections + '    </main>')
with open('it-services.html', 'w', encoding='utf-8') as f:
    f.write(it_content)

# Business Consulting HTML
with open('business-consulting.html', 'r', encoding='utf-8') as f:
    bc_content = f.read()

bc_sections = """        <!-- Projects Section -->
        <section class="projects-section reveal" style="padding: 5rem 5%;">
            <div class="container" style="max-width: 1200px; margin: 0 auto;">
                <h2 class="section-title text-center" data-i18n="bc-proj-title">Success <span class="highlight">Stories</span></h2>
                <div class="projects-grid">
                    <div class="project-card">
                        <div class="project-img">
                            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
                        </div>
                        <div class="project-content">
                            <h3 class="project-title" data-i18n="bc-proj-1">Global Market Expansion</h3>
                            <p class="project-desc" data-i18n="bc-proj-desc-1">Guided a regional manufacturing firm into European markets, resulting in a 40% revenue increase.</p>
                        </div>
                    </div>
                    <div class="project-card">
                        <div class="project-img">
                            <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>
                        </div>
                        <div class="project-content">
                            <h3 class="project-title" data-i18n="bc-proj-2">Merger & Acquisition Strategy</h3>
                            <p class="project-desc" data-i18n="bc-proj-desc-2">Facilitated a $50M acquisition, ensuring cultural alignment and operational synergy.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Client Reviews -->
        <section class="reviews-section reveal" style="padding: 5rem 5%; background: rgba(0,0,0,0.02);">
            <div class="container" style="max-width: 1200px; margin: 0 auto;">
                <h2 class="section-title text-center" data-i18n="bc-rev-title">Executive <span class="highlight">Testimonials</span></h2>
                <div class="reviews-grid">
                    <div class="review-card">
                        <div class="review-quote">"</div>
                        <p class="review-text" data-i18n="bc-rev-1">"Suntech Solutions provided the strategic clarity we desperately needed. Their advisory transformed our operational efficiency."</p>
                        <div class="reviewer-info">
                            <div class="reviewer-avatar">R</div>
                            <div class="reviewer-details">
                                <h4>Robert K.</h4>
                                <p data-i18n="bc-rev-role">CEO, Global Logistics</p>
                            </div>
                        </div>
                    </div>
                    <div class="review-card">
                        <div class="review-quote">"</div>
                        <p class="review-text" data-i18n="bc-rev-2">"An incredible partnership. Their insights into financial risk management saved us millions during the market downturn."</p>
                        <div class="reviewer-info">
                            <div class="reviewer-avatar">E</div>
                            <div class="reviewer-details">
                                <h4>Elena G.</h4>
                                <p data-i18n="bc-rev-role2">CFO, Apex Holdings</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
"""
bc_content = bc_content.replace('</main>', bc_sections + '    </main>')
with open('business-consulting.html', 'w', encoding='utf-8') as f:
    f.write(bc_content)

print("Added sections to all three pages.")
