from PIL import Image
import os

for f in sorted(os.listdir('inspect')):
    if f.endswith(('.png', '.jpg')):
        p = os.path.join('inspect', f)
        img = Image.open(p)
        print(f"File: {f} | Size: {img.size} | Mode: {img.mode}")
