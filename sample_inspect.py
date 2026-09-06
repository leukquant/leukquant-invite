from PIL import Image
import os

files = [
    'inspect/logo_thumb.png',
    'inspect/mascot_activity_thumb.png',
    'inspect/mascot_new_thumb.png',
    'inspect/thumb_4.jpg',
    'inspect/thumb_5.jpg',
    'inspect/thumb_6.jpg',
    'inspect/www.jeppiaarinstitute.org.png',
    'inspect/www.jeppiaarinstitute.org (1).png',
    'inspect/www.jeppiaarinstitute.org (2).png',
    'inspect/www.jeppiaarinstitute.org (3).png',
    'inspect/www.jeppiaarinstitute.org (4).png',
]

for f in files:
    if os.path.exists(f):
        img = Image.open(f)
        print(f"=== {f} ===")
        print(f"Size: {img.size}, Mode: {img.mode}")
        # Sample center colors
        cx, cy = img.size[0]//2, img.size[1]//2
        print(f"Center pixel: {img.getpixel((cx, cy))}")
