import urllib.request
import os

images = {
    "images/internship_dev.jpg": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=800&q=80",
    "images/internship_ecommerce.jpg": "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?auto=format&fit=crop&w=800&q=80",
    "images/internship_hero.jpg": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=1600&q=80"
}

if not os.path.exists("images"):
    os.makedirs("images")

print("Downloading elegant internship photos...")
for filepath, url in images.items():
    try:
        print(f"Downloading {filepath}...")
        urllib.request.urlretrieve(url, filepath)
        print(f"Successfully saved {filepath}")
    except Exception as e:
        print(f"Failed to download {filepath}: {e}")

print("Download process complete.")
