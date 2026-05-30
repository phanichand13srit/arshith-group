import re

files = ['ecommerce.html', 'it-services.html', 'business-consulting.html']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace <div class="hero-content" with <div class="hero-content hero-animate"
    # But make sure we don't add it multiple times
    if 'hero-animate' not in content:
        content = content.replace('class="hero-content"', 'class="hero-content hero-animate"')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Added hero-animate class to pages.")
