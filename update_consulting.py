import re

with open('business-consulting.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace body class
content = content.replace('<body>', '<body class="theme-consulting">')

# Replace the grid with consulting-layout
grid_start = content.find('<div class="services-grid">')
grid_end = content.find('</div>\n            </div>\n        </section>', grid_start)

if grid_start != -1 and grid_end != -1:
    old_grid = content[grid_start:grid_end]
    
    # We can just manually construct the new grid block
    new_grid = """<div class="consulting-layout">
                    <div class="consulting-row">
                        <div class="consulting-icon-box">
                            <div class="service-icon blue" style="width: 100px; height: 100px;"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg></div>
                        </div>
                        <div class="consulting-content">
                            <h3 data-i18n="bc-srv-st">Strategic Planning</h3>
                            <p data-i18n="bc-srv-st-desc">Develop long-term blueprints that align with your corporate vision, adapt to market shifts, and maximize ROI.</p>
                        </div>
                    </div>
                    
                    <div class="consulting-row">
                        <div class="consulting-icon-box">
                            <div class="service-icon pink" style="width: 100px; height: 100px;"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg></div>
                        </div>
                        <div class="consulting-content">
                            <h3 data-i18n="bc-srv-hr">Human Resources</h3>
                            <p data-i18n="bc-srv-hr-desc">Optimize workforce management, talent acquisition, and corporate culture to drive employee satisfaction.</p>
                        </div>
                    </div>
                    
                    <div class="consulting-row">
                        <div class="consulting-icon-box">
                            <div class="service-icon yellow" style="width: 100px; height: 100px;"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"></polyline></svg></div>
                        </div>
                        <div class="consulting-content">
                            <h3 data-i18n="bc-srv-op">Operations Management</h3>
                            <p data-i18n="bc-srv-op-desc">Streamline processes, reduce overhead costs, and implement efficient workflow methodologies.</p>
                        </div>
                    </div>
                    
                    <div class="consulting-row">
                        <div class="consulting-icon-box">
                            <div class="service-icon purple" style="width: 100px; height: 100px;"><svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 12h4l2-9 5 18 3-10h6"></path></svg></div>
                        </div>
                        <div class="consulting-content">
                            <h3 data-i18n="bc-srv-fa">Financial Advisory</h3>
                            <p data-i18n="bc-srv-fa-desc">Gain insights through risk assessment, investment strategies, and corporate restructuring.</p>
                        </div>
                    </div>"""
    
    content = content[:grid_start] + new_grid + content[grid_end:]

with open('business-consulting.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated business-consulting.html layout.")
