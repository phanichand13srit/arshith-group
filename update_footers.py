import os

files = ['index.html', 'it-services.html', 'ecommerce.html', 'business-consulting.html']

old_footer = """                    <ul class="footer-links">
                        <li><a href="#">Arshith Fresh</a></li>
                        <li><a href="#">Arshith Infotech</a></li>
                        <li><a href="#">Suntech Solutions</a></li>
                        <li><a href="#">Global Investments</a></li>
                    </ul>"""

new_footer = """                    <ul class="footer-links">
                        <li><a href="ecommerce.html">Arshith Fresh</a></li>
                        <li><a href="it-services.html">Arshith Infotech</a></li>
                        <li><a href="business-consulting.html">Suntech Solutions</a></li>
                        <li><a href="#">Global Investments</a></li>
                    </ul>"""

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace(old_footer, new_footer)
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Footers updated in all files.")
