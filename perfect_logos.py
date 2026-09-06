from PIL import Image, ImageFilter
import numpy as np
import os
import base64
import json

def perfect_matte(img_path, output_path, bg_cutoff=0.18):
    img = Image.open(img_path).convert('RGBA')
    arr = np.array(img, dtype=np.float32)
    
    r, g, b, a = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2], arr[:, :, 3]
    
    # Paper ivory reference is roughly (246, 240, 225)
    # Brightness / luminance
    lum = 0.299 * r + 0.587 * g + 0.114 * b
    
    # Color saturation: difference between max channel and min channel
    max_c = np.maximum(np.maximum(r, g), b)
    min_c = np.minimum(np.minimum(r, g), b)
    sat = (max_c - min_c) / np.maximum(max_c, 1.0)
    
    # Paper background has high luminance (lum > 210) and low saturation (sat < 0.18)
    # Target ink/gold either has lower luminance (navy, text, darks) or higher saturation (gold, orange, blue)
    is_paper = (lum > 215) & (sat < bg_cutoff)
    
    # Soft alpha feathering based on distance to paper color
    paper_dist = np.sqrt((r - 246.0)**2 + (g - 240.0)**2 + (b - 225.0)**2)
    
    # Smooth step transition: 0 when paper_dist < 15, 255 when paper_dist > 45
    alpha_scale = np.clip((paper_dist - 15.0) / 30.0, 0.0, 1.0)
    
    # Additional cutoff for pure background
    alpha_scale[is_paper & (lum > 230)] = 0.0
    
    new_a = np.minimum(a, alpha_scale * 255.0)
    arr[:, :, 3] = new_a
    
    res = Image.fromarray(np.uint8(arr), 'RGBA')
    bbox = res.getbbox()
    if bbox:
        res = res.crop(bbox)
        
    res.save(output_path, 'PNG', optimize=True)
    print(f"Perfected: {output_path} (Size: {res.size})")
    return res

os.makedirs('clean_assets', exist_ok=True)

perfect_matte('extracted/top_crest.png', 'clean_assets/top_crest.png', bg_cutoff=0.14)
perfect_matte('extracted/jit_crest.png', 'clean_assets/jit_crest.png', bg_cutoff=0.15)
perfect_matte('extracted/nba_logo.png', 'clean_assets/nba_logo.png', bg_cutoff=0.14)
perfect_matte('extracted/naac_seal.png', 'clean_assets/naac_seal.png', bg_cutoff=0.14)
perfect_matte('extracted/leukquant_logo.png', 'clean_assets/leukquant_logo.png', bg_cutoff=0.16)

# For navbar logo, use clean logo_thumb or leukquant_logo
if os.path.exists('inspect/logo_thumb.png'):
    thumb = Image.open('inspect/logo_thumb.png').convert('RGBA')
    thumb.save('clean_assets/leukquant_navbar_logo.png', 'PNG')

# Ultra-clean HD Mascot
mascot = Image.open('extracted/mascot_clean.png').convert('RGBA')
aspect = mascot.height / mascot.width
mascot_hd = mascot.resize((480, int(480 * aspect)), Image.Resampling.LANCZOS)
mascot_hd.save('clean_assets/mascot.png', 'PNG', optimize=True)

# Guest Photo
guest = Image.open('extracted/guest_photo.png')
guest.save('clean_assets/guest_photo.png', 'PNG')

print("All logos perfected!")
