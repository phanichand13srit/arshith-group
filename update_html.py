import os
import re

html_files = ["index.html", "business-consulting.html", "ecommerce.html", "it-services.html"]

for file_path in html_files:
    if not os.path.exists(file_path):
        continue
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update body to default to light mode
    content = re.sub(r'<body(?![^>]*class="light-mode")', r'<body class="light-mode"', content, count=1)

    # 2. Extract language selector
    lang_selector_match = re.search(r'<div class="language-selector">.*?</div>', content, flags=re.DOTALL)
    if lang_selector_match:
        lang_selector_html = lang_selector_match.group(0)
        
        # Remove from footer
        content = content.replace(lang_selector_html, '')
        
        # Wrap in li.nav-item
        nav_lang_html = f'''<li class="nav-item">
                        {lang_selector_html}
                    </li>'''
        
        # Insert into nav-list before theme toggle
        if 'id="theme-toggle"' in content and '<div class="language-selector">' not in content.split('id="theme-toggle"')[0]:
            content = re.sub(r'(<li class="nav-item">\s*<button id="theme-toggle")', r'' + nav_lang_html + r'\n                    \1', content)

    # 3. Remove inline theme logic
    theme_regex = r"const themeToggle = document\.getElementById\('theme-toggle'\);.*?\}\);"
    content = re.sub(theme_regex, "", content, flags=re.DOTALL)

    # 4. Remove inline language logic
    lang_regex = r"// --- i18n Translation Logic ---.*"
    # Actually it goes until the end of the script tag, let's just find the pattern
    # It might end with </script>
    lang_logic_pattern = r"// --- i18n Translation Logic ---.*?(?=</script>)"
    content = re.sub(lang_logic_pattern, "", content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Done updating HTML files.")
