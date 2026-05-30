import re

with open('styles.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove specific light-mode color overrides that use var(--text-dark)
content = re.sub(r'body\.light-mode [^{]+\{\s*color:\s*var\(--text-dark\);\s*\}', '', content)

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(content)

print("Cleaned up redundant light mode color overrides.")
