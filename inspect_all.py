from PIL import Image
import os

for f in os.listdir('inspect'):
    if f.endswith(('.png', '.jpg')):
        p = os.path.join('inspect', f)
        img = Image.open(p)
        print(f"{f}: size={img.size}, mode={img.mode}")
