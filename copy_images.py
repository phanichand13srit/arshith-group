import os
import shutil

# Source and destination paths
src_dir = r"C:\Users\Phani Chand\.gemini\antigravity\brain\06f6ab38-b490-441c-b659-03c0daa7ddbd"
dest_dir = r"c:\Users\Phani Chand\OneDrive\Desktop\15-05-2026 task 6 (updated) phanichand\images"

# Image mappings (source filename -> destination filename)
image_mappings = {
    "media__1779031619648.png": "Screenshot 2026-05-16 185518.png",
    "media__1779031619789.png": "Screenshot 2026-05-16 185542.jpg",
    "media__1779031619835.png": "Screenshot 2026-05-16 185600.jpg",
    "media__1779031619892.png": "Screenshot 2026-05-16 185614.jpg"
}

print("=" * 60)
print("             ARSHIT GROUP - IMAGE COPIER SERVICE")
print("=" * 60)

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)
    print(f"[+] Created destination directory: {dest_dir}")

copied_count = 0
for src_name, dest_name in image_mappings.items():
    src_path = os.path.join(src_dir, src_name)
    dest_path = os.path.join(dest_dir, dest_name)
    
    if os.path.exists(src_path):
        try:
            shutil.copy2(src_path, dest_path)
            print(f"[+] Successfully copied:\n    From: {src_path}\n    To:   {dest_path}\n")
            copied_count += 1
        except Exception as e:
            print(f"[-] Error copying {src_name}: {e}")
    else:
        print(f"[-] Source file not found: {src_path}")

print("=" * 60)
print(f"Completed! Copied {copied_count} of {len(image_mappings)} images successfully.")
print("=" * 60)
input("Press Enter to close this window...")
