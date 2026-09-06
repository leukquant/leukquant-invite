from PIL import Image
import os

images_to_check = [
    'extracted/leukquant_logo.png',
    'extracted/top_crest.png',
    'extracted/top_crest_trans.png',
    'extracted/jit_crest.png',
    'extracted/jit_crest_trans.png',
    'extracted/nba_logo.png',
    'extracted/nba_trans.png',
    'extracted/naac_seal.png',
    'extracted/naac_trans.png',
    'extracted/mascot_perfect.png',
    'extracted/mascot_clean.png',
    'extracted/mascot_trans.png',
    'inspect/logo_thumb.png',
    'inspect/jit_hd.png',
    'inspect/naac_hd.png',
    'inspect/nba_hd.png',
]

for img_path in images_to_check:
    if os.path.exists(img_path):
        img = Image.open(img_path)
        has_alpha = img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info)
        print(f"{img_path}: Mode={img.mode}, Size={img.size}, HasAlpha={has_alpha}")
        # Check corner pixels to see background color
        img_rgba = img.convert('RGBA')
        corners = [
            img_rgba.getpixel((0, 0)),
            img_rgba.getpixel((img.size[0]-1, 0)),
            img_rgba.getpixel((0, img.size[1]-1)),
            img_rgba.getpixel((img.size[0]-1, img.size[1]-1))
        ]
        print(f"   Corners (RGBA): {corners}")
