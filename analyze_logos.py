from PIL import Image, ImageEnhance
import os

def analyze_logo(path):
    img = Image.open(path).convert('RGBA')
    w, h = img.size
    print(f"=== {path} ({w}x{h}) ===")
    # Count how many non-transparent pixels have near-ivory background color (R>220, G>210, B>190)
    ivory_count = 0
    total_opaque = 0
    for y in range(h):
        for x in range(w):
            r, g, b, a = img.getpixel((x, y))
            if a > 30:
                total_opaque += 1
                if r > 210 and g > 200 and b > 180 and abs(r - g) < 25 and abs(g - b) < 35:
                    ivory_count += 1
    print(f"Total opaque pixels: {total_opaque}, Ivory halo/background pixels: {ivory_count} ({ivory_count*100/max(1, total_opaque):.1f}%)")

analyze_logo('extracted/leukquant_logo.png')
analyze_logo('inspect/logo_thumb.png')
analyze_logo('extracted/jit_crest.png')
analyze_logo('extracted/jit_crest_trans.png')
analyze_logo('extracted/nba_logo.png')
analyze_logo('extracted/nba_trans.png')
analyze_logo('extracted/naac_seal.png')
analyze_logo('extracted/naac_trans.png')
analyze_logo('extracted/top_crest.png')
